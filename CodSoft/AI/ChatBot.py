#Program Of ChatBot With Rule-Based 

from datetime import datetime 
current_time = datetime.now() 
while True: 
    user_input = input("Enter your message: ") 
    if user_input == "greet": 
        print("hi!how may i help you?") 
    elif user_input == "date and time": 
    # Default format: YYYY-MM-DD HH:MM:SS.ffffff 
        print(f"Current time: {current_time}") 
    elif user_input == "devloper": 
        print("Team Mr Battery") 
    elif user_input == "bye": 
        print("ok bye") 
    elif user_input == "exit":
        quit()
    else: 
        print("sorry i am not responding for this") 