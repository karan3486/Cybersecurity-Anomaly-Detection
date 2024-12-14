from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
client = OpenAI()
# Configure your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get the response from the model
def get_answer(question):
  response=client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "system", "content": '''You are a cybersecurity expert specializing in anomaly detection and webserver log 
               analysis. Your task is to analyze webserver access logs to identify whether each entry represents normal activity or a 
               potential attack. 
               Provide a detailed explanation for your decision, citing specific anomalies, suspicious patterns, or known malicious indicators. 
               Consider factors such as unusual IP behavior, access to sensitive paths, outdated protocols, error codes, and response sizes.

For each log entry:
1. Classify it as "Normal Activity" or "Potential Attack."
2. Justify your classification with a concise explanation.
3. Highlight any further actions that might be needed, such as IP blocking or deeper investigation.

Be methodical and precise in your analysis.
Note : Just give me Class name only and not any explanations.
'''}, 
              {"role": "user", "content": question}]
  )
  return response.choices[0].message.content

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle chatbot messages
@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = get_answer(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
