from flask import Flask, render_template, request, jsonify
from agents.langchain_executor import invoke
from CapaDatos.models import Chat


app = Flask(__name__)
chat = Chat()


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/send_message", methods=["POST"])
# def send_message():
#     user_input = request.form["message"]
#     response = invoke(chat_history=chat, query=user_input)
#     print(jsonify({"message": response}))
#     return jsonify({"message": response})
@app.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.form["message"]
    print(f"[TEST] Usuario escribió: {user_input}")
    response = invoke(chat_history=chat, query=user_input)
    print(f"[TEST] Respuesta del agente: {response}")
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
