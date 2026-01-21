Chatbot Project

Step 1: Train the Model (Required)
Before using the chatbot, you must train the model.
python SRC/Train.py   
This script:  
Trains the chatbot model  
Saves the trained model and vectorizer  
⚠️ The chatbot will NOT work without this step.

Step 2: Run the Chatbot  
After the model is trained and saved, run the chatbot. 
python SRC/Chat_bot.py  
This script:  
Loads the saved model  
Uses it to chat with the user  
Does NOT retrain the model  

Note:  
Train.py is only for training and saving the model  
Chat_bot.py is only for using the trained model  
Train once. Chat many times.  