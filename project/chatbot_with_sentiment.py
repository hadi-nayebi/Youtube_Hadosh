import openai
from burr.core import action, State, ApplicationBuilder

client = openai.Client()

@action(reads=[], writes=["prompt", "chat_history"])
def human_input(state: State, prompt: str) -> State:
    chat_item = {
        "content": prompt,
        "role": "user"
    }
    return state.update(prompt=prompt).append(chat_history=chat_item)

@action(reads=["chat_history"], writes=["response", "chat_history"])
def ai_response(state: State) -> State:
    content = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=state["chat_history"],
    ).choices[0].message.content
    chat_item = {
        "content": content,
        "role": "assistant"
    }
    return state.update(response=content).append(chat_history=chat_item)

@action(reads=["response"], writes=["sentiment"])
def analyze_sentiment(state: State) -> State:
    prompt = f"Analyze the sentiment of this text. Respond with only one word - positive, negative, or neutral: {state['response']}"
    sentiment = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    ).choices[0].message.content.strip().lower()
    return state.update(sentiment=sentiment)

app = (
    ApplicationBuilder()
    .with_actions(human_input, ai_response, analyze_sentiment)
    .with_transitions(
        ("human_input", "ai_response"),
        ("ai_response", "analyze_sentiment"),
        ("analyze_sentiment", "human_input")
    ).with_state(chat_history=[])
    .with_entrypoint("human_input")
    .build()
)

*_, state = app.run(halt_after=["analyze_sentiment"], inputs={"prompt": "What do you think about artificial intelligence?"})
print("AI response:", state["response"])
print("Sentiment:", state["sentiment"])
print(len(state["chat_history"]), "items in chat")
