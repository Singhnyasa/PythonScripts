import nltk
from nltk.chat.util import Chat, reflections   # <-- Import Chat (capital C)

pairs = [
    [
        r"(.*)help(.*)", ["Sure! How can I assist you today?"]
    ],
    [
        r"(.*)price of(.*)", ["The price of %2 is $50."]
    ],
    [
        r"quit", ["Goodbye! Have a nice day."]
    ]
]

def basic_chatbot():
    print("Welcome to Customer support (type 'quit' to exit)")
    chatbot = Chat(pairs, reflections)   # <-- Use Chat, not chat
    chatbot.converse()

basic_chatbot()
