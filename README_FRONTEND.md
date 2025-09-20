# YÖK Atlas RAG Chatbot - React Frontend

A modern, Gemini-style chat interface for the YÖK Atlas RAG chatbot built with React, Vite, and Tailwind CSS.

## Features

- 🎨 **Modern UI**: Gemini-inspired design with clean, responsive interface
- 💬 **Real-time Chat**: Smooth messaging experience with typing indicators
- 📱 **Responsive**: Works perfectly on desktop and mobile devices
- ⚡ **Fast**: Built with Vite for lightning-fast development and builds
- 🎯 **Type-safe**: Built with modern React patterns and hooks

## Quick Start

### Prerequisites

- Node.js (version 16 or higher)
- npm or yarn
- Your FastAPI backend running on `http://127.0.0.1:8000`

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up CORS in your FastAPI backend:**
   - Follow the instructions in `CORS_SETUP.md`
   - Make sure your FastAPI server is running on `http://127.0.0.1:8000`

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   - Navigate to `http://localhost:3000`
   - Start chatting with your YÖK Atlas RAG bot!

## Project Structure

```
src/
├── components/
│   ├── ChatBox.jsx          # Main chat container
│   ├── MessageBubble.jsx    # Individual message rendering
│   ├── InputBar.jsx         # Bottom input area with send button
│   └── TypingIndicator.jsx  # Animated loading indicator
├── App.jsx                  # Main application component
├── main.jsx                 # React entry point
└── index.css                # Global styles with Tailwind
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## API Integration

The frontend communicates with your FastAPI backend through:

- **Endpoint**: `POST http://127.0.0.1:8000/ask`
- **Request**: `{ "question": "your question here" }`
- **Response**: `{ "question": "...", "answer": "..." }`

## Customization

### Styling
- Modify `tailwind.config.js` for theme customization
- Update `src/index.css` for global styles
- Component-specific styles are in individual `.jsx` files

### API Configuration
- Change the API URL in `src/App.jsx` if your backend runs on a different port
- Update CORS settings in your FastAPI backend accordingly

## Features in Detail

### Chat Interface
- **User messages**: Right-aligned blue bubbles
- **Bot responses**: Left-aligned gray bubbles with larger text
- **Error messages**: Red bubbles for server errors
- **Typing indicator**: Animated dots while waiting for response

### Input Bar
- **Placeholder text**: "Sorunu buraya yaz..."
- **Send button**: Circular button with arrow icon
- **Keyboard shortcuts**: Enter to send, Shift+Enter for new line
- **Loading state**: Disabled during API calls

### Responsive Design
- **Mobile-first**: Optimized for all screen sizes
- **Touch-friendly**: Large touch targets for mobile
- **Smooth scrolling**: Auto-scroll to latest messages

## Troubleshooting

### CORS Issues
- Ensure CORS middleware is properly configured in your FastAPI backend
- Check that your backend is running on the correct port
- Verify the API URL in the frontend matches your backend

### Build Issues
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Check Node.js version compatibility
- Ensure all dependencies are properly installed

### API Connection Issues
- Verify your FastAPI backend is running
- Check browser console for error messages
- Test API endpoint directly with curl or Postman

## Production Deployment

1. **Build the project:**
   ```bash
   npm run build
   ```

2. **Deploy the `dist` folder** to your hosting service

3. **Update CORS settings** in your FastAPI backend to include your production domain

## Contributing

Feel free to submit issues and enhancement requests!

