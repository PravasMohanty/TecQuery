
# LangChain Demo with Google GEMINI API - Coding Version

This project is a simple **Streamlit** web app that demonstrates how to use **LangChain** with **Google GEMINI API** for generating concise explanations and simple examples of coding or technical concepts.

---

## Features

- **Google GEMINI Integration**  
  Uses `langchain_google_genai` to connect with the Google GEMINI LLM models.

- **LangChain Prompt Templates & Chains**  
  - `LLMChain` for generating concise descriptions of coding topics.
  - `SimpleSequentialChain` and `SequentialChain` for multi-step reasoning.
  - `ConversationBufferMemory` to maintain context.

- **Streamlit UI**  
  Simple input-based interface to interact with the model.

---

## Project Structure

```
.
├── myenv/                  # Virtual environment (ignored in Git)
├── .env                     # Secret environment variables (ignored in Git)
├── .gitignore               # Git ignore file
├── constants.py             # Contains GOOGLE_API_KEY or other constants
├── main.py                  # Main Streamlit app script
├── requirements.txt         # Python dependencies
```

---

## Requirements

- Python 3.9+
- Google API Key (Gemini)

---

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create a virtual environment
```bash
conda create -p venv python==3.9 -y
conda activate ./venv
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
```
*(Or directly set `google_api` inside `constants.py`)*

---

## Running the App

Run the Streamlit app:
```bash
streamlit run main.py
```

Open your browser and navigate to:
```
http://localhost:8501
```

---

## Usage

1. Enter any coding or technical topic in the input box.  
2. The app will generate:  
   - A **concise description** of the topic.  
   - A **simple example** to illustrate the concept.

---

## Example Topics
- *What is recursion?*
- *Explain REST API.*
- *Explain multithreading in Python.*

---

## Environment Variables & Secrets
- `.env` and any secret keys (like `google_api`) are **not committed** to Git.
- Use `.env.example` to specify required variables without exposing secrets.

---

## License
This project is licensed under the MIT License.
