LangChain Models folder
# GenAI-learning-journey
A repository documenting my daily learning journey with Generative AI and LangChain, featuring notes, examples, and hands-on experiments.

## 🚀 Setup Instructions

Follow the steps below to set up this project on your local machine:

### 1️⃣ Clone the Repository
1. Create a folder on your **Desktop** (e.g., `LangChain`).
2. Open a terminal and run:
   ```bash
   git clone https://github.com/MunawarShereen/GenAI-learning-journey.git
   cd GenAI-learning-journey

2️⃣ Set Up Virtual Environment
Create and activate a virtual environment:
py -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
Install all the required Python packages:
pip install -r requirements.txt

4️⃣ Configure Environment Variables
Create a .env file in the root directory of the project.
Add the following line (replace "your_token_here" with your actual token):
HUGGINGFACE_API_TOKEN="your_token_here"

5️⃣ Setup Hugging Face
Create an account on Hugging Face.
Generate an Access Token from your profile settings.
Optionally, create or choose a model on Hugging Face.

6️⃣ Run the Project
Finally, run the Python script of your choice:
py fileName.py
Replace fileName.py with the actual script you want to execute.


🧠 LangChain Models – Notes

LangChain provides a powerful framework for working with models in AI applications.
Broadly, there are two main categories of models in LangChain:

1️⃣ Language Models (LMs)

Language models are designed to process and generate natural language.
They are further divided into two categories:

🔹 a) LLMs (Large Language Models – Legacy)

LLMs were the first generation of language models used in LangChain.
They are designed for general-purpose text generation, such as:

✅ Generating text

✅ Summarizing documents

✅ Answering questions

✅ Writing and explaining code

🔹 b) Chat Models (Modern)

Chat models are the preferred way to work with language models today.
Unlike traditional LLMs, ChatModels are designed for multi-turn conversations.
They:

✅ Accept structured input (e.g., system, user, and assistant messages)

✅ Maintain conversational context

✅ Support multi-turn interactions

📌 Closed-Source vs Open-Source Language Models
Language models can be closed-source or open-source:
| **Type**          | **Examples**                                      | **Notes**                                      |
| ----------------- | ------------------------------------------------- | ---------------------------------------------- |
| **Closed Source** | OpenAI (GPT), Claude (Anthropic), Gemini (Google) | Hosted via API, easy to use, highly capable    |
| **Open Source**   | Hugging Face models, LLaMA, Mistral               | Self-hostable, customizable, great for privacy |

2️⃣ Embedding Models

Embedding models convert text into numerical vectors that capture meaning.
These embeddings can be used for:

✅ Semantic Search (finding similar documents)

✅ Clustering & Classification

✅ Recommendation Systems

✅ Retrieval-Augmented Generation (RAG)


✅ Key Takeaways
Language Models → Generate and process text
🔹 LLMs → Old approach, general-purpose text generation
🔹 ChatModels → Modern approach, conversational & context-aware
Embedding Models → Convert text into vectors for semantic search and retrieval
Both categories have open-source and closed-source options.

🧠 LangChain Prompts – Notes

Prompts are the foundation of interaction with language models in LangChain. They define what input is sent to the model and strongly influence the quality of the response.

1️⃣ What are Prompts?

Prompts are structured instructions that guide a language model to produce useful and relevant outputs.

They can include:
✅ Direct instructions
✅ Variables (dynamic content)
✅ Examples (few-shot learning)
✅ Conversation context (for chat models)

2️⃣ Types of Prompts in LangChain

🔹 a) String Prompts

Simple text inputs.

Directly send raw text to the model.

🔹 b) Prompt Templates

Prompts with placeholders for variables.

Allow dynamic and reusable input structures.

🔹 c) Few-Shot Prompts

Include examples of inputs and outputs.

Help the model generalize better by learning from patterns.

🔹 d) Chat Prompts

3️⃣ Why are Prompts Important?

Prompts help you:
✅ Control tone, style, and depth of answers
✅ Improve accuracy of model responses
✅ Provide additional context or constraints
✅ Break down complex tasks into smaller, structured steps

Designed for chat-based models.

Use roles such as system, user, and assistant.

