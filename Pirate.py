from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)

def interact_with_chatgpt(user_input):
    """
    Function to send a prompt to ChatGPT and get the response using the updated OpenAI API.
    :param user_input: Text string provided by the user to translate into wild west speak.
    :return: Response text from ChatGPT.
    """
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Constructing the full prompt
    full_prompt = f"Translate the following into language a pirate would use. :\n\n{user_input}"

    # Sending prompt to ChatGPT using the updated API method
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Replace with the model you want to use
        prompt=full_prompt,
        max_tokens=150  # Adjust the number of maximum tokens if needed
    )

    # Extracting and returning the response text
    return response.choices[0].text.strip()

def translate_text():
    data = request.json
    user_input = data['text']
    translated_text = interact_with_chatgpt(user_input)
    return jsonify({"translated":  translated_text})

# Main script
if __name__ == "__main__":
    app.run(debug=True)