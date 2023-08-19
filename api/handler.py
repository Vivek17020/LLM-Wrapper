import os
import openai
from flask import Flask, request, jsonify

app = Flask(_name_)

openai.api_key = os.getenv("")  # Set your OpenAI API key here

@app.route("/", methods=["POST"])
def generate_text():
    try:
        data = request.get_json()
        prompt = data["prompt"]
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        
        generated_text = response.choices[0].text.strip()
        
        return jsonify({"generated_text": generated_text})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
