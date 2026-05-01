from llm.client import chat

SYSTEM_PROMPT = """
You are a personal assistant for Steven.
Steven is a Java/DevOps/SRE engineer transitioning into AI Engineering.
You help him stay productive, achieve his daily goals, and learn new things.
Be concise, practical, and encouraging
"""

def main():

    print("\n======PERSONAL ASSISTANT======")
    print("Type 'quit' to exit\n")

    messages = [{"role": "system","content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input(">>> ").strip();
        except(KeyboardInterrupt, EOFError):
            print("\nGoodbye")
            break

        if not user_input:
            continue
            
        if user_input.lower() in ["quit", "exit"]:
            print("\nGoodbye")
            break
        
        messages.append({"role":"user","content":user_input})

        try:
            response = chat(messages)
            full_response = ""
            print("\n>>>")

            for chunk in response:
                content = chunk["message"]["content"]
                print(content, end="", flush=True)
                full_response += content
            messages.append({"role":"assistant","content":full_response})
            print("\n")

        except Exception as e:
            print(f"\nError: {e}")
            print("Make sure Ollama is running (ollama serve) and your model is pulled.\n")
            messages.pop()


if __name__ == "__main__":
    main()
