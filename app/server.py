from fastapi import FastAPI
from .main import ping, perform

app = FastAPI()

@app.get('/')
async def read_root():
    return perform()

@app.get('/ping')
async def read_ping():
    return ping()
