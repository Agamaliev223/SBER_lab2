from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
from zoneinfo import ZoneInfo

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"]   # Allows all headers
)

@app.get('/')
async def root():
    return {'response': "Проверка связи"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)