from fastapi import FastAPI
from pydantic import BaseModel
from backend.query_handler import handle_query  # Use absolute import

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_database(request: QueryRequest):
    response = handle_query(request.query)
    return {"message": response}