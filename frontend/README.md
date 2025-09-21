# YÖK Atlas RAG Chatbot - Frontend

This is the React frontend for the YÖK Atlas RAG Chatbot, designed with a Gemini-like interface.

## Features

- **Modern React Interface**: Built with React 18 and Vite
- **Gemini-like Design**: Clean, modern UI with custom styling
- **Real-time Chat**: Interactive chat interface with typing indicators
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **API Integration**: Seamlessly connects to FastAPI backend

## Setup

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Start Development Server**:
   ```bash
   npm run dev
   ```

3. **Build for Production**:
   ```bash
   npm run build
   ```

## Configuration

- **Port**: 3000 (configurable in `vite.config.js`)
- **API Proxy**: Requests to `/ask` are automatically proxied to `http://127.0.0.1:8000`
- **Styling**: Tailwind CSS with custom Gemini-inspired theme

## Project Structure

```
frontend/
├── public/
│   └── index.html          # Main HTML template
├── src/
│   ├── components/         # React components
│   │   ├── ChatBox.jsx     # Main chat interface
│   │   ├── InputBar.jsx    # Message input component
│   │   ├── MessageBubble.jsx # Individual message display
│   │   └── TypingIndicator.jsx # Loading indicator
│   ├── App.jsx             # Main application component
│   ├── main.jsx            # Application entry point
│   └── index.css           # Global styles
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite configuration with proxy
├── tailwind.config.js      # Tailwind CSS configuration
└── postcss.config.js       # PostCSS configuration
```

## API Integration

The frontend automatically proxies API requests to the FastAPI backend:
- Frontend runs on `http://localhost:3000`
- API calls to `/ask` are proxied to `http://127.0.0.1:8000/ask`
- No CORS issues due to Vite proxy configuration

## Development

Make sure your FastAPI backend is running on `http://127.0.0.1:8000` before starting the frontend development server.

