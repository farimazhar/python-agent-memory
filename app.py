from memory import PythonAgentMemory

def main():
    print("Python Agent Memory Initialized")
    
    agent = PythonAgentMemory()
    
    # Seed memory
    agent.remember("The user is Fari from Peshawar")
    agent.remember("GitHub username is Farimazhar")

    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        
        # Command to store memory
        if user_input.lower().startswith("remember:"):
            content = user_input[9:].strip()
            agent.remember(content)
            print("Agent: Stored in long-term memory.")
        else:
            # Command to recall memory
            memories = agent.recall(user_input)
            print(f"Agent Recall: {memories}")

if __name__ == "__main__":
    main()
