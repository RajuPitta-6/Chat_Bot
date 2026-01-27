import streamlit as st
from streamlit.components.v1 import html

from SRC.backend import get_response


def init_history() -> None:
    """
    Ensure conversation history exists in session state.
    Each entry is a dict: {"role": "user" | "assistant", "content": str}
    """
    if "history" not in st.session_state:
        st.session_state.history = []


def build_chat_html(messages) -> str:
    """
    Build a ChatGPT-style chat window as a full HTML document.
    Uses light theme, centered chat, bubbles, and auto-scroll.
    """
    # Build message bubbles
    message_blocks = []

    if not messages:
        # Initial bot prompt
        message_blocks.append(
            """
            <div class="chat-message bot">
                <div class="avatar">B</div>
                <div class="message-bubble">
                    Hi, I'm your dermatology chat assistant. Describe your skin concern or ask a question to begin.
                </div>
            </div>
            """
        )
    else:
        for msg in messages:
            role = msg.get("role", "assistant")
            content = msg.get("content", "")

            # Basic HTML escaping
            content = (
                content.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            role_class = "user" if role == "user" else "bot"
            avatar_text = "U" if role == "user" else "B"

            message_blocks.append(
                f"""
                <div class="chat-message {role_class}">
                    <div class="avatar">{avatar_text}</div>
                    <div class="message-bubble">{content}</div>
                </div>
                """
            )

    messages_html = "\n".join(message_blocks)

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <style>
            body {{
                margin: 0;
                padding: 0;
                font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
                    sans-serif;
                background: #f9fafb;
            }}

            .outer-wrapper {{
                display: flex;
                justify-content: center;
                padding: 0.5rem 0.75rem 1.25rem 0.75rem;
            }}

            .chat-window {{
                width: 100%;
                max-width: 600px;
                background: #ffffff;
                border-radius: 20px;
                border: 1px solid #e5e7eb;
                box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
                padding: 1.1rem 1.35rem;
                box-sizing: border-box;
            }}

            .chat-container {{
                max-height: 50vh;
                overflow-y: auto;
                padding-right: 0.35rem;
                scroll-behavior: smooth;
            }}

            .chat-message {{
                display: flex;
                margin-bottom: 0.75rem;
                gap: 0.5rem;
            }}

            .chat-message.user {{
                flex-direction: row-reverse;
            }}

            .avatar {{
                width: 32px;
                height: 32px;
                border-radius: 999px;
                background: #e5e7eb;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.85rem;
                font-weight: 600;
                color: #374151;
                flex-shrink: 0;
            }}

            .chat-message.user .avatar {{
                background: #111827;
                color: #f9fafb;
            }}

            .message-bubble {{
                max-width: 85%;
                padding: 0.75rem 1rem;
                border-radius: 18px;
                font-size: 0.95rem;
                line-height: 1.5;
                word-wrap: break-word;
                white-space: pre-wrap;
            }}

            .chat-message.user .message-bubble {{
                background: #111827;
                color: #f9fafb;
                border-bottom-right-radius: 6px;
            }}

            .chat-message.bot .message-bubble {{
                background: #f3f4f6;
                color: #111827;
                border-bottom-left-radius: 6px;
            }}

            /* Custom scrollbar (WebKit) */
            .chat-container::-webkit-scrollbar {{
                width: 6px;
            }}
            .chat-container::-webkit-scrollbar-track {{
                background: transparent;
            }}
            .chat-container::-webkit-scrollbar-thumb {{
                background-color: #d1d5db;
                border-radius: 999px;
            }}
        </style>
    </head>
    <body>
        <div class="outer-wrapper">
            <div class="chat-window">
                <div id="chat-container" class="chat-container">
                    {messages_html}
                </div>
            </div>
        </div>
        <script>
            const chatEl = document.getElementById("chat-container");
            if (chatEl) {{
                chatEl.scrollTop = chatEl.scrollHeight;
            }}
        </script>
    </body>
    </html>
    """
    return full_html


def main() -> None:
    st.set_page_config(page_title="Dermatology Chat Bot", page_icon="💬", layout="centered")

    init_history()

    # Header (no raw HTML here; just Streamlit widgets)
    st.title("Dermatology Chat Bot")
    st.caption("Powered by Raju Pitta")

    # Input area at the bottom, submit on single Enter press.
    # IMPORTANT: handle input BEFORE rendering the chat so the new
    # message appears immediately in this run, not the next one.
    user_input = st.chat_input("Type your message here...")

    if user_input and user_input.strip():
        user_text = user_input.strip()
        # Add user message to history
        st.session_state.history.append({"role": "user", "content": user_text})

        # Get bot response from backend
        try:
            response = get_response(user_text)
        except Exception as e:
            response = (
                "Sorry, something went wrong while processing your message.\n\n"
                f"Error: {e}"
            )

        st.session_state.history.append(
            {"role": "assistant", "content": str(response)}
        )

    # Now render the chat with the up-to-date history
    chat_html = build_chat_html(st.session_state.history)
    html(chat_html, height=420, scrolling=True)


if __name__ == "__main__":
    main()