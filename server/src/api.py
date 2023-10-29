from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.util.responsemodel import ResponseModel
from src.util.milvus_model import MilvusModel

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

"""
Takes in the query question
Returns 
- youtube link
- transcript (bonus: ran through openai to make it more readable)
- start time
- end time
"""
@app.get(f"{API_V1_ENDPOINT}/query", response_model=ResponseModel)
async def test(question: str = Query()):
    return_message = MilvusModel.search(question)
    return ResponseModel(success=True, message={"test": return_message, "question": question})