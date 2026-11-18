# GenAI Chatbot – AI-Powered Conversational Assistant

A web-based Generative AI chatbot built using Python, Flask, and Groq API. The application allows users to interact with an AI assistant, receive intelligent responses, and maintain conversation history using SQLite.

## Features

- AI-powered conversational responses using Groq API
- Interactive web-based chat interface
- Conversation history storage using SQLite
- Load previous conversations
- Clear chat history
- Markdown rendering for headings, lists, tables, and code
- Input validation and error handling
- REST API endpoints
- Automated testing using Pytest

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and REST API |
| Groq API | AI response generation |
| SQLite | Conversation history storage |
| HTML | Frontend structure |
| CSS | User interface styling |
| JavaScript | Frontend interactions |
| Pytest | Automated testing |
| Git and GitHub | Version control |

## Project Structure

```text
GenAI-Chatbot/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
│
├── database/
│   └── db.py
│
├── routes/
│   └── chat_routes.py
│
├── services/
│   └── ai_service.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_app.py
│
└── instance/
    └── chatbot.db
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/GenAI-Chatbot.git
```

### 2. Open the project directory

```bash
cd GenAI-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Groq API key

Create a `.env` file in the project root.

Add your own API key and model configuration:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_available_groq_model
```

Get an API key from:

https://console.groq.com/keys

**Important:** Never upload your `.env` file or share your API key publicly.

### 7. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Open chatbot interface |
| GET | `/health` | Check application status |
| POST | `/api/chat` | Send a message to AI |
| GET | `/api/history` | Retrieve conversation history |
| DELETE | `/api/history` | Clear conversation history |

## Running Automated Tests

Execute:

```bash
python -m pytest -v
```

### Test Results

The project has successfully passed all six automated tests:

- Home page test
- Health endpoint test
- Chat endpoint test
- Empty message validation test
- Chat history test
- Clear history test

**Latest recorded result: 6 passed.**

## Future Improvements

- User authentication
- Multiple chat sessions
- Streaming AI responses
- Export conversation history
- Improved responsive interface

## Author

**Shreya Patil**

Computer Science and Engineering – AI & ML

GitHub: https://github.com/29-shreya

## License

This project is intended for educational and portfolio purposes.