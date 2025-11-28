# Building with Gemini API 🚀

A hands-on workshop project to learn how to build AI-powered applications using Google's Gemini API.

## 📋 Project Overview

This repository contains a **Personal AI Chatbot** project that demonstrates:
- ✅ Integration with Google Gemini API
- ✅ FastAPI backend for handling chat requests
- ✅ Modern React frontend with beautiful UI
- ✅ Real-time conversational AI
- ✅ Customizable system instructions

## 🏗️ Project Structure

```
Building-with-Gemini-API/
├── services/
│   └── chatbot/           # FastAPI backend
│       ├── main.py        # FastAPI app with CORS
│       ├── utils.py       # Gemini API integration
│       ├── schema.py      # Pydantic models
│       └── .env           # API keys (create this)
├── chatbot_frontend/      # React + TypeScript frontend
│   ├── src/
│   │   ├── App.tsx       # Main chatbot component
│   │   ├── App.css       # Component styles
│   │   └── index.css     # Design system
│   └── package.json
└── README.md
```

## 🎯 Workshop Goals

By the end of this workshop, you will:
1. ✅ Understand how to use the Gemini API
2. ✅ Create a personalized AI chatbot
3. ✅ Build a FastAPI backend
4. ✅ Connect a React frontend to your API
5. ✅ Deploy your chatbot (optional)

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Step 1: Setup Backend

```bash
# Navigate to the chatbot service
cd services/chatbot

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn python-decouple google-genai

# Create .env file with your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Start the backend server
uvicorn main:app --reload
```

The backend will be running at `http://localhost:8000`

### Step 2: Setup Frontend

```bash
# In a new terminal, navigate to chatbot_frontend
cd chatbot_frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be running at `http://localhost:5173`

### Step 3: Customize Your Chatbot

Open `services/chatbot/utils.py` and fill in the TODO sections with your personal information:

```python
system_instruction = """
# TODO: Define who you are and what you do
You are [YOUR ROLE HERE]

# TODO: Fill in your personal details
- Name: [YOUR NAME]
- Title: [YOUR TITLE]
- Skills: [YOUR SKILLS]
# ... and more!
"""
```

## 📚 Workshop Exercises

### Exercise 1: Complete the System Instruction ✏️

**Location:** `services/chatbot/utils.py`

Fill in the TODO sections with:
- Your name and role
- Your responsibilities
- Personal information (education, skills, projects)
- Career goals and interests

**Time:** 15-20 minutes

### Exercise 2: Test Your Chatbot 🧪

1. Start both backend and frontend
2. Ask your chatbot questions like:
   - "What projects have you worked on?"
   - "What are your skills?"
   - "Tell me about your education"
3. Verify the responses match your system instruction

**Time:** 10 minutes

### Exercise 3: Customize the UI (Optional) 🎨

**Location:** `frontend/src/index.css`

Try changing:
- Color scheme (edit CSS variables)
- Chatbot avatar emoji
- Welcome message
- Button styles

**Time:** 15 minutes

## 🔧 API Documentation

### Backend Endpoints

#### `GET /`
Health check endpoint

**Response:**
```json
{
  "message": "Hello World"
}
```

#### `POST /chat`
Send a message to the chatbot

**Request:**
```json
{
  "messages": [
    {
      "role": "user",
      "message": "Hello, who are you?"
    }
  ]
}
```

**Response:**
```json
{
  "role": "model",
  "message": "Hi! I'm [Your Name]'s AI assistant..."
}
```

## 🎨 Frontend Features

- **Modern Dark Theme** with gradient accents
- **Smooth Animations** for messages and interactions
- **Typing Indicators** when the bot is thinking
- **Auto-scroll** to latest messages
- **Error Handling** with user-friendly messages
- **Responsive Design** for mobile and desktop

## 🛠️ Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Google Gemini API** - AI language model
- **Pydantic** - Data validation
- **python-decouple** - Environment variable management

### Frontend
- **React** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **CSS3** - Modern styling with custom properties

## 📖 Learning Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

## 🐛 Troubleshooting

### Backend Issues

**Error: "GEMINI_API_KEY not found"**
- Make sure you created the `.env` file in `services/chatbot/`
- Verify your API key is correct

**Error: "Module not found"**
- Run `pip install -r requirements.txt` (if exists)
- Or manually install: `pip install fastapi uvicorn python-decouple google-genai`

### Frontend Issues

**CORS Error**
- Make sure the backend is running on `http://localhost:8000`
- Check that CORS middleware is configured in `main.py`

**Connection Failed**
- Verify both backend and frontend are running
- Check the browser console for detailed error messages

## 🎓 Workshop Tips

1. **Start Simple**: Get the basic chatbot working first
2. **Test Often**: Test after each change to catch issues early
3. **Be Creative**: Make the chatbot reflect your personality
4. **Ask Questions**: Don't hesitate to ask for help
5. **Have Fun**: Experiment with different prompts and styles!

## 📝 Next Steps

After completing the workshop, you can:
- 🚀 Deploy your chatbot to production
- 🎨 Add more UI features (voice input, file uploads)
- 🤖 Implement function calling for dynamic actions
- 📊 Add conversation history persistence
- 🔐 Add user authentication

## 📄 License

MIT License - Feel free to use this project for learning and personal use!

## 🤝 Contributing

This is a workshop project, but suggestions and improvements are welcome!

---

**Happy Coding! 🎉**

Made with 🤖 for the SETIF Developers Group Workshop