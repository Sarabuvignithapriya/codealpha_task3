#program on basic chatbot
def chatbot_response(user_input):
    user_input = user_input.lower()

#instructions giving by user    
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just an ai, but thanks for asking!"
    elif "i need some help" in user_input:
        return "sure!,what do you need help with?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."
#defining a chat function
def chat():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(chatbot_response(user_input))
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
#calling chat function
if __name__ == "__main__":
    chat()