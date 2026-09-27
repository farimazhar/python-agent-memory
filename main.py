class AgentMemory:
    def __init__(self):
        self.memory = []

    def remember(self, text):
        self.memory.append(text)
        print(f"Yaad kar liya: {text}")

    def recall(self, query):
        # Simple semantic search
        results = [m for m in self.memory if query.lower() in m.lower()]
        return results if results else ["Kuch yaad nahi aaya"]

# Test
agent = AgentMemory()
agent.remember("Fari lives in Peshawar")
agent.remember("Fari loves Python coding")

print(agent.recall("Peshawar"))
