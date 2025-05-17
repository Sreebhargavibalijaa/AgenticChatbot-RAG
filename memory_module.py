from langchain.memory import ConversationBufferMemory

def build_memory():
    print("🧠 Initializing conversation memory buffer...")
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return memory
