from fastapi import FastAPI
from app.app import ping, perform

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": perform()}

@app.get('/ping')
async def read_ping():
    return {"message": ping()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
