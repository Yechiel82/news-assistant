from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.app import ping, perform

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
OPENAI_KEY = os.getenv('OPENAI_KEY')

app = FastAPI()

@app.get('/')
async def read_root():
    with open('index.html', 'r') as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get('/ping')
async def read_ping():
    return {"message": ping()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
