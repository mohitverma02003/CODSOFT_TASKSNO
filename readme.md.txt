# Rule-Based Chatbot

This project is a simple, rule-based conversational chatbot developed in Python using Streamlit for the user interface. It demonstrates fundamental Natural Language Processing (NLP) techniques by utilizing Regular Expressions (`re`) to identify user intent and map it to predefined responses.

## Features
- **Pattern Matching:** Uses regular expressions to handle variations in user input (e.g., detecting "hi", "hello", or "hey").
- **Randomized Responses:** Selects from multiple predefined answers to make the conversation feel less repetitive.
- **Modern UI:** Built with Streamlit for a clean, interactive chat interface.
- **No External APIs:** Runs 100% locally without requiring paid LLM APIs or internet access for message processing.

## Technologies
- Python 3.8+
- Streamlit
- Regex (`re` module)

## Setup and Installation

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt