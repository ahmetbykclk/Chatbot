import pyjokes

# Function to generate a random joke
def generate_joke():
    return pyjokes.get_joke()

# Main loop for the chatbot
if __name__ == "__main__":
    print("Chatbot: Hi, I'm your joke generator chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("Chatbot: Press Enter to get a random joke or type 'exit' to end: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            joke = generate_joke()
            print("Chatbot:", joke)
