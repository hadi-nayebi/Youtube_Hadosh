import openai
from burr.core import action, State, ApplicationBuilder

# Import the actions and app from chatbot_with_sentiment.py
from chatbot_with_sentiment import human_input, ai_response, analyze_sentiment, app

def run_chatbot():
    print("Welcome to the Chatbot with Sentiment Analysis!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
        
        *_, state = app.run(halt_after=["analyze_sentiment"], inputs={"prompt": user_input})
        
        print("\nAI:", state["response"])
        print("Sentiment:", state["sentiment"])
        print(f"Chat history: {len(state['chat_history'])} items")

if __name__ == "__main__":
    run_chatbot()
