from rag_pipeline import build_rag_agent
import os

def main():
    print("="*60)
    print("🤖 Welcome to the Agentic RAG Chatbot!")
    print("Type 'exit' anytime to end the conversation.")
    print("="*60)

    # Initialize the RAG Agent with Memory
    agent = build_rag_agent()

    while True:
        user_input = input("🧑 You: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("🤖 Chatbot: Goodbye! 👋")
            break

        response = agent.run(user_input)
        print(f"🤖 Chatbot: {response}")
        print("-" * 60)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"  # Set this properly
    main()
