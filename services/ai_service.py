
from groq import Groq

from config import Config


def generate_ai_response(message, chat_history=None):
    """Generate an AI response using Groq API."""

    if not Config.GROQ_API_KEY:
        raise ValueError(
            "Groq API key is missing. Check your .env file."
        )

    try:
        # Create Groq client
        client = Groq(
            api_key=Config.GROQ_API_KEY
        )

        # Prepare conversation history
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Give clear, accurate and easy-to-understand answers."
                )
            }
        ]

        if chat_history:
            for chat in chat_history:
                role = chat["role"]

                if role not in ("user", "assistant"):
                    continue

                messages.append({
                    "role": role,
                    "content": chat["content"]
                })

        # Add latest user message
        messages.append({
            "role": "user",
            "content": message
        })

        # Generate response
        response = client.chat.completions.create(
            model=Config.GROQ_MODEL,
            messages=messages,
            temperature=0.7,
            max_completion_tokens=2048
        )

        reply = response.choices[0].message.content

        if not reply:
            raise RuntimeError(
                "Groq returned an empty response."
            )

        return reply

    except Exception as e:
        print("Groq API Error:", repr(e))
        raise
