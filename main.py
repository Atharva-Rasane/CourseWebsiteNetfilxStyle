from flask import Flask, request, jsonify
# from transformers import AutoTokenizer, AutoModelForCausalLM
from flask import Flask, render_template
# from transformers import pipeline
# import requests
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

# Load the GPT-Neo model
# model_name = "EleutherAI/gpt-neo-2.7B"
# model_name = "EleutherAI/gpt-neox-20b"
# model_name = "EleutherAI/polyglot-ko-5.8b"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
# generator = pipeline('text-generation', model=model_name)
client = Groq(
    api_key="ENTER API KEY HERE",
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/search')
def search():
    return render_template('search.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = "Student asks "+request.json.get('message') + ", Teacher replies"
#     print("Inputting")
#     # inputs = tokenizer(user_input, return_tensors="pt")
#     print("thinking")
#     outputs = generator(user_input, do_sample=True, min_length=50)
#     # outputs = model.generate(**inputs)
#     print("speaking")
#     # response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     response = outputs[0]['generated_text']
#     print(response)
#     return jsonify({"response": response[len(user_input):]})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = "Student asks "+request.json.get('message') + ", Teacher replies"
    print("Inputting")
    print("thinking")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    print(response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
