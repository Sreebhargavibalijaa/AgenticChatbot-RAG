# 🧠 Agentic Chatbot with RAG and Memory

This project implements a conversational **agentic chatbot** that leverages **Retrieval-Augmented Generation (RAG)** and **conversation memory** to respond intelligently using documents as its knowledge base.

Powered by:
- 🧠 **LangChain** for chaining LLMs + tools
- 📄 **FAISS** for vector-based document retrieval
- 🔁 **ConversationBufferMemory** for contextual, coherent dialogues
- 💬 **OpenAI GPT-4** for high-quality language generation

---

## ✨ Features

- **RAG-based intelligent responses**: Retrieves relevant content chunks from a document store before generating answers.
- **Memory-powered conversations**: Maintains history of the dialogue using `ConversationBufferMemory`.
- **Modular & scalable**: Clean code structure suitable for extensions (e.g., tools, APIs, custom agents).
- **Interactive CLI interface**: Simple and human-like conversation flow in your terminal.

---
yaml

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/agentic-chatbot-rag.git
cd agentic-chatbot-rag
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
You’ll need:

langchain

openai

faiss-cpu

tiktoken

Optional: Create a virtual environment with venv or conda before installing.

3. Set your OpenAI API Key
bash

export OPENAI_API_KEY=your-key-here
Or add it in the code inside main.py.

4. Run the Chatbot
bash

python main.py
📝 How it Works
Document Loading: Text documents are loaded and split into manageable chunks.

Vector Store Creation: Chunks are embedded using OpenAI and stored in a FAISS index.

Retrieval: On each user query, relevant documents are retrieved.

Answer Generation: Retrieved context + query are passed to GPT-4 for response.

Memory: Previous interactions are stored and reused to maintain chat history.

📚 Sample Conversation
bash

🤖 Welcome to the Agentic RAG Chatbot!
🧑 You: What is LangChain?
🤖 Chatbot: LangChain is a framework that helps developers integrate language models like GPT with external tools, documents, and APIs.
🧑 You: How do you remember my previous question?
🤖 Chatbot: I'm using ConversationBufferMemory, which helps retain past interactions so we can have contextual conversations.
🧩 Customize & Extend
🔧 Swap the LLM (ChatOpenAI) with another like Anthropic, Gemini, or LLaMA.

🛠 Add custom tools using LangChain Agents (e.g., calculator, web browser).

🌐 Deploy to Streamlit or FastAPI for web interface.

📄 License
MIT License © 2025 [Your Name]

🤝 Contributing
Pull requests are welcome! If you have ideas for better memory handling, more tools, or a UI – feel free to open an issue or submit a PR.

🙌 Acknowledgements
LangChain

FAISS

OpenAI

python


---

Let me know if you'd like to add:
- A logo or demo GIF
- Deployment instructions (Docker/Streamlit)
- Hugging Face Space or Colab links

I'm happy to help!







