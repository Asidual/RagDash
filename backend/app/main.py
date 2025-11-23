from fastapi import FastAPI
import uvicorn 

app = FastAPI(version="0.1.0", description="App che si occuperà di implementare una RAG")


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=False) # Avvio del server uvicorn