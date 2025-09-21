# YÖK Atlas RAG Chatbot

A FastAPI backend with React frontend that provides information about Turkish universities and programs using RAG (Retrieval-Augmented Generation) technology.

## Project Structure

```
puplica/
├── frontend/              # React frontend application
│   ├── src/              # Frontend source code
│   │   ├── components/   # React components
│   │   │   ├── ChatBox.jsx
│   │   │   ├── InputBar.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   └── TypingIndicator.jsx
│   │   ├── App.jsx       # Main application component
│   │   ├── main.jsx      # Application entry point
│   │   └── index.css     # Global styles
│   ├── public/           # Static assets
│   │   └── index.html    # HTML template
│   ├── package.json      # Frontend dependencies
│   ├── vite.config.js    # Vite configuration with API proxy
│   ├── tailwind.config.js # Tailwind CSS configuration
│   └── postcss.config.js # PostCSS configuration
├── data/                  # Data files
│   ├── program_ids.csv   # Program ID mappings
│   ├── yokatlas_data.json # University data
│   └── yokatlas_index.faiss # FAISS index
├── utils/                 # Python utilities
├── constants/             # Python constants
├── app.py                 # FastAPI backend
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Features

- **Modern React Frontend**: Clean, responsive interface with Gemini-like design
- **FastAPI Backend**: High-performance Python API with RAG technology
- **Real-time Chat**: Interactive chat interface with typing indicators
- **Turkish Language Support**: Optimized for Turkish university data
- **API Proxy**: Seamless frontend-backend communication

## Quick Start

### Backend Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend
python app.py
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Development

The project is organized with clear separation of concerns:

- **Frontend**: React with Vite, located in `frontend/` directory
- **Backend**: FastAPI with Python utilities in root directory
- **API Integration**: Vite proxy automatically forwards `/ask` requests to backend

## API Endpoints

- `POST /ask` - Send a question to the chatbot

## Technologies Used

### Frontend
- React 18
- Vite
- Tailwind CSS
- Custom Gemini-inspired styling

### Backend
- FastAPI
- Python
- FAISS (vector search)
- Hugging Face Transformers

## Running the Application

1. **Start the backend** (from root directory):
   ```bash
   python app.py
   ```

2. **Start the frontend** (from frontend directory):
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access the application**: Open `http://localhost:3000` in your browser

The frontend will automatically proxy API requests to the backend running on `http://127.0.0.1:8000`.