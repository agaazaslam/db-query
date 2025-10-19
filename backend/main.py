from fastapi import FastAPI
from pydantic import BaseModel
from llm import llm_use


app = FastAPI()

class Request(BaseModel):
    query : str 


@app.get("/")
async def root():
    return {"message": "Hello World "}

@app.get("/health")
async def health():
    return {"message": "Everything working fine"}


@app.post("/query")
async def query(request:Request):
    result = llm_use(request.query)
    return {"message":result} 



















