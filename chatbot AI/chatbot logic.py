import re
import random

class RuleBasedChatbot:
    	def__init__(self):
        # Dictionary of intents. 
        # Keys are Regular Expression patterns.
        # Values are lists of possible responses.
        self.rules = {
            r'.*\b(hello|hi|hey|greetings|good morning|good evening)\b.*': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Greetings! How may I assist you?"
            ],
            r'.*\b(how are you|how do you do|how are things)\b.*': [
                "I'm just a bundle of predefined code, but I'm doing great! How about you?",
                "Functioning within normal parameters! How can I help you?"
            ],
            r'.*\b(what is your name|who are you)\b.*': [
                "I am RuleBot, a simple pattern-matching chatbot.",
                "You can call me RuleBot. I am here to answer your questions based on my programming."
            ],
            r'.*\b(what can you do|help|capabilities)\b.*': [
                "I can chat with you, answer basic questions about Artificial Intelligence, and demonstrate rule-based logic.",
                "I'm programmed to respond to greetings, questions about my identity, and fundamental queries about AI and Machine Learning."
            ],
            r'.*\b(what is ai|what is artificial intelligence)\b.*': [
                "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.",
                "AI refers to computer systems capable of performing complex tasks that historically only a human could do, like reasoning or problem-solving."
            ],
            r'.*\b(what is machine learning|what is ml)\b.*': [
                "Machine learning is a subset of AI that focuses on building systems that learn from data, rather than being explicitly programmed.",
                "ML is the science of getting computers to act without being explicitly programmed, usually by feeding them data to recognize patterns."
            ],
            r'.*\b(who created you|who made you|creator)\b.*': [
                "I was created by a dedicated intern at CODSOFT!",
                "A CODSOFT AI intern programmed me using Python and Streamlit."
            ],
            r'.*\b(thank you|thanks|appreciate it)\b.*': [
                "You're very welcome!",
                "Glad I could help!",
                "Anytime!"
            ],
            r'.*\b(bye|goodbye|see you|exit|quit)\b.*': [
                "Goodbye! Have a great day!",
                "See you later! Feel free to chat again if you need anything."
            ]
        }

    	def get_response(self, user_input):
        # Convert user input to lowercase to make pattern matching case-insensitive
        user_input = user_input.lower()

        # Iterate through the rules dictionary
        for pattern, responses in self.rules.items():
            # If the user's input matches a regex pattern
            if re.search(pattern, user_input):
                # Return a random response from the matched category
                return random.choice(responses)
        
        # Fallback response if no patterns match
        return "I'm sorry, I don't quite understand that. My knowledge is limited to specific predefined rules. Could you try rephrasing your question?"
