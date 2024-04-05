from flask import Flask, render_template, request, jsonify
from Pirate import interact_with_chatgpt as translate_to_pirate
from DitzyBlonde import interact_with_chatgpt as translate_to_blonde
from WildWest import interact_with_chatgpt as translate_to_cowboy
from Yoda import interact_with_chatgpt as translate_to_yoda
from Shakespeare import interact_with_chatgpt as translate_to_shakespeare
from FourtiesMafia import interact_with_chatgpt as translate_to_fourtiesmafia
from Lamar import interact_with_chatgpt as translate_to_lamar
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    style = data['style']
    if style == 'pirate':
        translated_text = translate_to_pirate(text)
    elif style == 'cowboy':
        translated_text = translate_to_cowboy(text)
    elif style == 'shakespeare':
        translated_text = translate_to_shakespeare(text)
    elif style == 'ditzyblonde':
        translated_text = translate_to_blonde(text)
    elif style == 'fourtiesmafia':
        translated_text = translate_to_fourtiesmafia(text)
    elif style == 'yoda':
        translated_text = translate_to_yoda(text)
    elif style == 'lamar':
        translated_text = translate_to_lamar(text)
    return jsonify(translated=translated_text)

@socketio.on('message')
def handle_message(data):
    # Assume the 'theme' and 'text' are passed in the data
    text = data['text']
    theme = data['theme']
    translated_text = ''  # Placeholder for the translated text

    # Now apply the theme to the text
    if theme == 'pirate':
        translated_text = translate_to_pirate(text)
    elif theme == 'cowboy':
        translated_text = translate_to_cowboy(text)
    elif theme == 'shakespeare':
        translated_text = translate_to_shakespeare(text)
    elif theme == 'ditzyblonde':
        translated_text = translate_to_blonde(text)
    elif theme == 'fourtiesmafia':
        translated_text = translate_to_fourtiesmafia(text)
    elif theme == 'yoda':
        translated_text = translate_to_yoda(text)
    elif theme == 'lamar':
        translated_text = translate_to_lamar(text)

    # Broadcast the translated text
    socketio.emit('message', {'text': translated_text})

if __name__ == '__main__':
    socketio.run(app, debug=False)
