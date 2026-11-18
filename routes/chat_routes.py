
from flask import Blueprint, request, jsonify

from config import Config
from database.db import (
    save_message,
    get_chat_history,
    clear_chat_history
)
from services.ai_service import generate_ai_response


chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Please send valid JSON."
        }), 400

    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({
            "error": "Message must be text."
        }), 400

    message = message.strip()

    if not message:
        return jsonify({
            "error": "Message cannot be empty."
        }), 400

    if len(message) > Config.MAX_MESSAGE_LENGTH:
        return jsonify({
            "error": "Message is too long."
        }), 400

    try:
        history = get_chat_history(
            limit=Config.HISTORY_CONTEXT_LIMIT
        )

        reply = generate_ai_response(message, history)

        save_message("user", message)
        save_message("assistant", reply)

        return jsonify({
            "success": True,
            "reply": reply
        }), 200

    except Exception as e:

        print("\n========== GROQ API ERROR ==========")
        print(repr(e))
        print("====================================\n")

        return jsonify({
            "success": False,
            "error": "Unable to generate a response. Please check the Groq API configuration."
        }), 500


@chat_bp.route("/api/history", methods=["GET"])
def history():

    messages = get_chat_history()

    return jsonify({
        "success": True,
        "messages": messages
    }), 200


@chat_bp.route("/api/history", methods=["DELETE"])
def delete_history():

    clear_chat_history()

    return jsonify({
        "success": True,
        "message": "Chat history cleared."
    }), 200
