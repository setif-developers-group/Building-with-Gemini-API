import { useState, useRef, useEffect } from 'react'
import './App.css'

interface Message {
  role: 'user' | 'model'
  message: string
}

interface ChatHistory {
  messages: Message[]
}

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to bottom when new messages arrive
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages, isLoading])

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return

    const userMessage: Message = {
      role: 'user',
      message: inputValue.trim()
    }

    // Add user message to chat
    setMessages(prev => [...prev, userMessage])
    setInputValue('')
    setIsLoading(true)
    setError(null)

    try {
      // Prepare chat history
      const chatHistory: ChatHistory = {
        messages: [...messages, userMessage]
      }

      // Call the FastAPI backend
      const response = await fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(chatHistory)
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const botMessage: Message = await response.json()

      // Add bot response to chat
      setMessages(prev => [...prev, botMessage])
    } catch (err) {
      console.error('Error sending message:', err)
      setError('Failed to send message. Make sure the backend is running on http://localhost:8000')
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1 className="app-title">Personal Chatbot</h1>
        <p className="app-subtitle">Powered by Gemini API</p>
      </header>

      <div className="chat-container">
        {/* Chat Header */}
        <div className="chat-header">
          <div className="chat-header-avatar">🤖</div>
          <div className="chat-header-info">
            <h2>Personal Chatbot</h2>
            <div className="chat-header-status">
              <span className="status-indicator"></span>
              <span>Online</span>
            </div>
          </div>
        </div>

        {/* Messages Area */}
        <div className="messages-area">
          {messages.length === 0 && (
            <div className="welcome-message">
              <div className="welcome-message-icon">💬</div>
              <h3>Welcome to Your Personal AI Assistant!</h3>
              <p>
                Start a conversation by typing a message below.
                Ask me anything about my background, skills, projects, or interests!
              </p>
            </div>
          )}

          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              <div className="message-avatar">
                {msg.role === 'user' ? '👤' : '🤖'}
              </div>
              <div className="message-content">
                {msg.message}
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="message bot">
              <div className="message-avatar">🤖</div>
              <div className="message-content">
                <div className="typing-indicator">
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                </div>
              </div>
            </div>
          )}

          {error && (
            <div className="error-message">
              ⚠️ {error}
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="input-area">
          <div className="input-wrapper">
            <input
              type="text"
              className="message-input"
              placeholder="Type your message..."
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              disabled={isLoading}
            />
          </div>
          <button
            className="send-button"
            onClick={sendMessage}
            disabled={isLoading || !inputValue.trim()}
          >
            {isLoading ? (
              <>
                <span>Sending</span>
                <span>...</span>
              </>
            ) : (
              <>
                <span>Send</span>
                <span>📤</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
