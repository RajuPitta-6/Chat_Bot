
from predict import ChatBot
chatbot = ChatBot()

print(f"{'=='*6} Welcome to Chat Bot! {'=='*6}")
print("Enter exit to quit")
while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Thank you for using Chat Bot!")
        break
    else:
        responce = chatbot.predict(message)
    print("Bot : ",responce)