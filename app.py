
from flask import Flask, render_template, jsonify

from database.db import initialize_database
from routes.chat_routes import chat_bp


def create_app():
    """Create and configure the Flask application."""

    app = Flask(__name__)

    # Initialize SQLite database
    initialize_database()

    # Register chatbot API routes
    app.register_blueprint(chat_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy",
            "message": "GenAI Chatbot API is running."
        })

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
