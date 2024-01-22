
from fastapi import FastAPI

app = FastAPI()

@app.get("/question/{question}")
def read_item(question: str):
    return {"question": question}