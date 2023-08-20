import time
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

openai.api_key = "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"

max_tokens = 1000
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    ai_response = generate_response(user_input)
    return jsonify({'response': ai_response})

def generate_response(user_input):
    global conversation_history

    try:
        conversation_history.append("User: " + user_input)
        conversation_text = "\n".join(conversation_history[-50:])
        formatted_prompt = "Conversation History:\n" + conversation_text

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=formatted_prompt,
            max_tokens=max_tokens - len(formatted_prompt.split())
        )

        new_text = response.choices[0].text.strip()
        conversation_history.append("AI: " + new_text)
        return new_text
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Waiting for 60 seconds before retrying...")
        time.sleep(60)
        return generate_response(user_input)
    except openai.error.TooManyTokensError as e:
        print("Token limit exceeded. Truncating conversation history and retrying...")
        tokens_to_remove = len(conversation_history[0].split())
        conversation_history = conversation_history[tokens_to_remove:]
        return generate_response(user_input)

if __name__ == '__main__':
    app.run(debug=True)
