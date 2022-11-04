from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
all_messages = []

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route("/get_messages")
def get_messages():
	return {"messages": all_messages}

def add_message(sender, text):
	new_message = {
		"sender": sender,
		"text": text,
		"time": datetime.now().strftime("%H:%M"),
	}
	all_messages.append(new_message)

@app.route("/send_message")
def send_message():
	sender = request.args["sender"]
	text = request.args["text"]
	add_message(sender, text)

	return {"result":True}

@app.route("/chat")
def chat_page():
	return render_template("form.html")

app.run()
