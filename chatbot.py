def chatbot():
    print("Hello! I am a simple rule-based chatbot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a few lines of code, but I'm doing great!")
        elif 'task' in user_input or 'internship' in user_input:
            print("Chatbot: Good luck completing your AI internship tasks!")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you try asking something else?")

if __name__ == "__main__":
    chatbot()
