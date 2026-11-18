
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatBox = document.getElementById("chatBox");
const sendButton = document.getElementById("sendButton");
const clearButton = document.getElementById("clearButton");
const typingIndicator = document.getElementById("typingIndicator");


// Display chat messages
function addMessage(text, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender === "user" ? "user-message" : "assistant-message"
    );

    const contentDiv = document.createElement("div");

    contentDiv.classList.add("message-content");

    // Render Markdown only for AI responses
    if (sender === "assistant" && typeof window.renderMarkdown === "function") {

        contentDiv.innerHTML = window.renderMarkdown(text);

    } else {

        // Keep user messages as plain text for security
        contentDiv.textContent = text;

    }

    messageDiv.appendChild(contentDiv);

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Load previous chat history
async function loadHistory() {

    try {

        const response = await fetch("/api/history");

        const data = await response.json();

        if (!response.ok) {
            throw new Error("Could not load chat history.");
        }

        chatBox.innerHTML = "";

        if (data.messages && data.messages.length > 0) {

            data.messages.forEach(message => {
                addMessage(message.content, message.role);
            });

        } else {

            addMessage(
                "Hello! 👋 I am your AI assistant. How can I help you today?",
                "assistant"
            );

        }

    } catch (error) {

        console.error("History Error:", error);

    }

}


// Send message to AI
chatForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    messageInput.value = "";

    sendButton.disabled = true;

    typingIndicator.classList.remove("hidden");

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        addMessage(data.reply, "assistant");

    } catch (error) {

        addMessage(
            "Error: " + error.message,
            "assistant"
        );

    } finally {

        sendButton.disabled = false;

        typingIndicator.classList.add("hidden");

        messageInput.focus();

    }

});


// Clear chat history
clearButton.addEventListener("click", async function() {

    const confirmed = confirm(
        "Are you sure you want to clear the chat history?"
    );

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch("/api/history", {
            method: "DELETE"
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not clear history.");
        }

        chatBox.innerHTML = "";

        addMessage(
            "Chat history cleared. Ask me anything!",
            "assistant"
        );

    } catch (error) {

        alert(error.message);

    }

});


// Load previous messages when the page opens
loadHistory();
