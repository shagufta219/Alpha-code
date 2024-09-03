import random

# Dictionary of chatbot responses
responses = {
    'hello': ['Hi, how are you?', 'Hello! How can I help you?', 'Hey, what\'s up?'],
    'how are you': ['I\'m good, thanks!', 'I\'m doing great, thanks for asking!', 'I\'m just a chatbot, I don\'t have feelings, but thanks for asking!'],
    'what is your name': ['My name is ChatBot', 'I\'m an AI, I don\'t have a personal name', 'You can call me Bot'],
    'exit': ['Goodbye!', 'See you later!', 'Bye!']
}

def get_response(user_input):
    """Get a response from the chatbot based on the user's input"""
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return 'I didn\'t understand that. Can you please rephrase?'

def main():
    print('Welcome to the chatbot! Type "exit" to quit.')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            print('ChatBot:', get_response(user_input))
            break
        print('ChatBot:', get_response(user_input))

if __name__ == '__main__':
    main()