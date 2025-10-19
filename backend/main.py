from fastapi import FastAPI
import time
from pydantic import BaseModel
from llm import llm_use
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # URLs allowed to make requests
    allow_credentials=True,         # allow cookies/auth headers
    allow_methods=["*"],            # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],            # allow all headers
)

class Request(BaseModel):
    message : str 
    role : str 
    time : str


class Response(BaseModel):
    message: str
    role : str 
    time : str

@app.get("/")
async def root():
    return {"message": "Hello World "}

@app.get("/health")
async def health():
    return {"message": "Everything working fine"}

@app.post("/test" , response_model=Response)
async def test(request : Request):
    time.sleep(3)
    return {"message" : f"Sample response for testing backend with attached sent stuff {request.message +  request.time } " , "time" : "1PM" , "role": "assistant"}

@app.post("/query" , response_model=Response)
async def query(request:Request):
    result = llm_use(request.message)
    return {"message" : result , "time" : "1PM" , "role": "assistant"}


















