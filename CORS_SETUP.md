# CORS Setup for FastAPI Backend

To allow your React frontend to communicate with your FastAPI backend, you need to add CORS middleware to your FastAPI application.

## Step 1: Install CORS dependency

Add this to your `requirements.txt`:
```
fastapi[all]>=0.110.0
```

Or install directly:
```bash
pip install fastapi[all]
```

## Step 2: Update your app.py

Add the following imports and middleware configuration to your `app.py`:

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
# ... your other imports

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ... rest of your existing code
```

## Step 3: Restart your FastAPI server

After making these changes, restart your FastAPI server:

```bash
python app.py
```

## Alternative: More permissive CORS (for development only)

If you want to allow all origins during development (NOT recommended for production):

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Testing the connection

Once you've set up CORS and started both servers:

1. Start your FastAPI backend: `python app.py`
2. Start your React frontend: `npm run dev`
3. Open http://localhost:3000 in your browser
4. Try sending a message to test the connection

The frontend should now be able to successfully communicate with your FastAPI backend!

