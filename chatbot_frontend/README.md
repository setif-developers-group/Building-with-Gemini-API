# Personal Chatbot Frontend

A beautiful, modern React frontend for the Gemini-powered personal chatbot.

## Features

✨ **Modern UI/UX**
- Sleek dark theme with gradient accents
- Smooth animations and transitions
- Responsive design for all devices
- Typing indicators and loading states

🎨 **Design Highlights**
- Custom glassmorphism effects
- Animated background gradients
- Smooth message animations
- Custom scrollbar styling

💬 **Chat Features**
- Real-time messaging
- Message history
- Auto-scroll to latest message
- Error handling with user feedback
- Keyboard shortcuts (Enter to send)

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- FastAPI backend running on `http://localhost:8000`

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and visit:
```
http://localhost:5173
```

## Backend Integration

The frontend connects to the FastAPI backend at `http://localhost:8000/chat`.

Make sure your backend is running before starting the frontend:

```bash
# In the services/chatbot directory
uvicorn main:app --reload
```

### API Endpoint

**POST** `/chat`

Request body:
```json
{
  "messages": [
    {
      "role": "user",
      "message": "Hello!"
    }
  ]
}
```

Response:
```json
{
  "role": "model",
  "message": "Hi! How can I help you today?"
}
```

## Project Structure

```
frontend/
├── src/
│   ├── App.tsx          # Main chatbot component
│   ├── App.css          # Component styles
│   ├── index.css        # Global styles & design system
│   └── main.tsx         # App entry point
├── package.json
├── vite.config.ts       # Vite configuration with proxy
└── README.md
```

## Customization

### Colors

Edit the CSS variables in `src/index.css`:

```css
:root {
  --accent-primary: #6366f1;
  --accent-secondary: #8b5cf6;
  --bg-primary: #0a0e1a;
  /* ... more variables */
}
```

### Chat Header

Modify the chat header in `src/App.tsx`:

```tsx
<div className="chat-header">
  <div className="chat-header-avatar">🤖</div>
  <div className="chat-header-info">
    <h2>Your Name Here</h2>
    {/* ... */}
  </div>
</div>
```

## Building for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Technologies Used

- **React** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **CSS3** - Styling with custom properties
- **Fetch API** - HTTP requests

## Troubleshooting

### CORS Issues

If you encounter CORS errors, make sure:
1. The backend is running on `http://localhost:8000`
2. The Vite proxy is configured correctly in `vite.config.ts`

### Backend Connection Failed

Make sure:
1. The FastAPI backend is running
2. The backend is accessible at `http://localhost:8000`
3. The `/chat` endpoint is working correctly

### Port Already in Use

If port 5173 is already in use, Vite will automatically use the next available port. Check the terminal output for the actual URL.

## Workshop Notes

This is part of the **Building with Gemini API** workshop. Students should:

1. ✅ Complete the system instruction in `services/chatbot/utils.py`
2. ✅ Fill in personal information (name, projects, skills, etc.)
3. ✅ Test the chatbot with various questions
4. 🎨 (Optional) Customize the UI colors and styling

## License

MIT
