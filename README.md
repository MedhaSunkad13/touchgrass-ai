# 🌱 TouchGrass AI

**Spend less time on screens and more time outside.**

TouchGrass AI is a beginner-friendly AI-powered application that generates personalized outdoor activity plans based on a user's chosen activity and mood. It encourages people to take a break from screens and reconnect with the real world.

The application uses a locally running open-weight AI model through Ollama to generate activity descriptions and practical steps.

## ✨ Features

- 🌿 Choose from eight outdoor activities.
- 😊 Personalize suggestions based on your mood.
- ⏱️ Specify how much time you have available.
- 🤖 Generate activity descriptions and steps using local AI.
- 📵 Encourage screen-free outdoor experiences.
- 🛡️ Check generated content before displaying it.
- 🎨 Simple, user-friendly interface built with Streamlit.

## 🛠️ Tech Stack

- **Language:** Python
- **User interface:** Streamlit
- **AI runtime:** Ollama
- **AI model:** Gemma 3 1B
- **Structured output:** JSON

## 🧠 How It Works

1. The user enters their available time and mood.
2. The user selects an outdoor activity.
3. The application sends the selected activity and mood to Gemma through Ollama.
4. The model generates a description and practical activity steps in JSON format.
5. Python checks the generated content and cleans the steps.
6. Streamlit displays the activity plan, the user's available time, and a screen-free reminder.

The application uses a **hybrid AI approach**: the language model generates personalized content, while Python handles important application behavior, formatting, and checks.

## 🌱 Why Local AI?

TouchGrass AI uses an open-weight model that can run locally through Ollama instead of relying on a hosted proprietary AI API.

This approach makes the project easier to experiment with, reduces dependence on external inference services, and can keep the activity-generation prompt on the user's machine when using the local setup.

## 🚀 Getting Started

### Prerequisites

Install the following:

- Python 3.12
- [Ollama](https://ollama.com/download)
- [Git](https://git-scm.com/downloads) (optional, for cloning the repository)

### 1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd touchgrass-ai

Replace https://github.com/MedhaSunkad13/touchgrass-ai with your actual repository URL.

Alternatively, download the repository and open its folder in a terminal.

### 2. Create and activate a virtual environment

You can use Conda:

conda create -n touchgrass python=3.12
conda activate touchgrass

### 3. Install Python dependencies

pip install -r requirements.txt

### 4. Download the AI model

ollama pull gemma3:1b

Keep Ollama running on your computer.

### 5. Run the application

From the project directory, run:

streamlit run app.py

Open the local URL shown in your terminal, usually:

`http://localhost:8501`

## 📁 Project Structure

```text
touchgrass-ai/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔮 Future Improvements

- Improve the reliability and quality of generated activity plans.
- Add more outdoor activities.
- Improve validation and recovery when AI output is invalid.
- Add optional accessibility and weather-aware suggestions.

## 💚 Project Goal

TouchGrass AI explores how open-weight AI can encourage healthier screen habits by helping people discover simple, personalized ways to spend more time outdoors.

Built with Python, Streamlit, and Gemma through Ollama.
