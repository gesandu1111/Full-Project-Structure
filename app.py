from flask import Flask, render_template, request, jsonify
from ai import ask_ai
from memory import clear_memory
from config import SYSTEM_NAME, SYSTEM_VERSION, ENABLE_COMMANDS

app = Flask(__name__)

# --- Web Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_msg = data.get("message", "")
    ai_reply = ask_ai(user_msg)
    return jsonify({"reply": ai_reply})

# --- Optional CLI mode ---
def cli_mode():
    print(f"🤖 {SYSTEM_NAME} v{SYSTEM_VERSION} STARTED")
    print("Type /help for commands")

    while True:
        user_input = input("\nYOU > ").strip()

        if ENABLE_COMMANDS and user_input.startswith("/"):
            if user_input == "/help":
                print("\n🧠 COMMANDS\n--------------------------------")
                print("/help      - show commands")
                print("/clear     - clear memory")
                print("/history   - show chat history")
                print("/time      - show system time")
                print("/exit      - exit system")
                print("--------------------------------")
            elif user_input == "/clear":
                clear_memory()
                print("Memory cleared.")
            elif user_input == "/exit":
                print("Exiting system...")
                break
            else:
                print("Unknown command. Type /help for commands.")
        else:
            ai_response = ask_ai(user_input)
            print(f"\nAI > {ai_response}")

if __name__ == "__main__":
    # Uncomment one of the following lines:
    
    # CLI mode
    # cli_mode()

    # Web UI mode
    app.run(debug=True)
