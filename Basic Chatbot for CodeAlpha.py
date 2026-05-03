def start_chatbot():
    print("--- CodeAlpha Basic Chatbot ---")
    print("Hello! I am a simple rule-based bot. (Type 'quit' to exit)")

    while True:
        # 1. Get user input and convert to lowercase for easy matching
        user_input = input("You: ").lower()

        # 2. Rule-Based Logic using if-elif statements
        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you today?")
            
        elif "your name" in user_input:
            print("Bot: I am the CodeAlpha Task 4 Chatbot.")
            
        elif "how are you" in user_input:
            print("Bot: I'm just a script, but I'm functioning perfectly! How about you?")
            
        elif "python" in user_input:
            print("Bot: Python is a great language! I am actually written in Python.")
            
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}.")
            
        elif "quit" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
            
        else:
            # Default response if no rules match
            print("Bot: I'm sorry, I don't understand that. Could you try asking something else?")

if __name__ == "__main__":
    start_chatbot()
