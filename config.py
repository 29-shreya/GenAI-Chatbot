
import os
from pathlib import Path
from dotenv import load_dotenv

# Main project directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Config:

    # Groq API configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-20b"
    )

    # SQLite database
    DATABASE_PATH = BASE_DIR / "instance" / "chatbot.db"

    # Application settings
    MAX_MESSAGE_LENGTH = 5000

    HISTORY_CONTEXT_LIMIT = 20
