from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.util.responsemodel import ResponseModel

app: FastAPI = FastAPI()

API_V1_ENDPOINT = "/api/v1"

# Set up CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=ResponseModel)
async def default():
    return ResponseModel(success=True, message={"hi": "test"})

@app.get(f"{API_V1_ENDPOINT}/", response_model=ResponseModel)
async def test():
    return ResponseModel(success=True, message={"test": "passed"})