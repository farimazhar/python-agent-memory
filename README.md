# Python Agent Memory 🧠

A lightweight, modular, and persistent memory system for AI Agents built with Python, ChromaDB, and OpenAI.

### How It Works? ⚙️

The working is based on 3 simple steps:

**1. Embedding (Text to Numbers)**
When you call `remember()`, the text is not saved as plain text. ChromaDB converts the text into a high-dimensional vector (a list of numbers) using an embedding model.
Example: `"Fari lives in gujrat"` -> `[0.23, 0.89, 0.12, ...]`

**2. Storage (Vector Database)**
These vectors are stored locally in a persistent ChromaDB database on your machine. No cloud, no data leak. It also stores metadata like user name and timestamp.

**3. Semantic Recall (Meaning-based Search)**
When you call `recall("Where does Fari live?")`, your query is also converted into a vector. The system then calculates cosine similarity between your query vector and all stored vectors and returns the top 3 closest matches.
This is why it can find "Pesh
