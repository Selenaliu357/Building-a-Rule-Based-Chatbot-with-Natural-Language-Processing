'''
Building a Rule-Based Chatbot with Natural Language Processing:

1. Installing Necessary Libraries

First we need to install the NLTK library which will help us with text processing tasks 
such as tokenization and part-of-speech tagging.

We can install the NLTK library using this command: pip install nltk 


2. Importing Required Libraries

re: Used for regular expressions which help in matching patterns in user input.
Chat: A class from NLTK used to build rule-based chatbots.
reflections: A dictionary to map pronouns. 
             For example, "I" → "you" making conversations more natural.

'''

import nltk
import re
from nltk.chat.util import Chat, reflections


def setup_nltk():
    '''
    Download required NLTK data
    punkt: Used for tokenization which breaking down text into words or sentences.
    averaged_perceptron_tagger: PoS tagger helps to identify the grammatical 
                                parts of speech in a sentence.

    '''
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

'''
Defining Patterns and Responses:

Rule-based chatbot recognize patterns in user input and respond accordingly.
Here we will define a list of patterns and respective responses that the chatbot
will use to interact with users. These patterns are written using regular expressions 
which allow the chatbot to match complex user queries and provide relevant responses.

'''
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?",
                       "Hi there! How may I assist you?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name?", ["I am your friendly chatbot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"(.*) (help|assist) (.*)", ["Sure! How can I assist you with %3?"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?",
               "Could you please elaborate?"]]
]


'''
Defining the Chatbot Class:

Now, let’s create a class to handle the chatbot’s functionality. 
This class will use the Chat object from NLTK to match patterns and generate responses.

'''

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)
    

'''
Interacting with the Chatbot:

Here we create a function that allows users to interact with the chatbot. 
It keeps asking for input until the user types "exit".

'''

def chat_with_bot(chatbot):
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    setup_nltk()

    chatbot = RuleBasedChatbot(pairs)
    chat_with_bot(chatbot)