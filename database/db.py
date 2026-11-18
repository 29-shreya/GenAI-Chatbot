
import sqlite3
from pathlib import Path

from config import Config


def get_connection():
    """Create a database connection."""

    database_path = Path(Config.DATABASE_PATH)

    database_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(database_path)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create the chat_messages table."""

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_message(role, content):
    """Save a chat message."""

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO chat_messages (role, content)
        VALUES (?, ?)
        """,
        (role, content)
    )

    connection.commit()
    connection.close()


def get_chat_history(limit=50):
    """Get recent chat messages."""

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT id, role, content, created_at
        FROM chat_messages
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    ).fetchall()

    connection.close()

    return [dict(row) for row in reversed(rows)]


def clear_chat_history():
    """Delete all chat messages."""

    connection = get_connection()

    connection.execute("DELETE FROM chat_messages")

    connection.commit()
    connection.close()
