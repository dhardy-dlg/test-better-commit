from fastapi import FastAPI

app = FastAPI()

# app
@app.get("/")
async def root():
    return {"message": "Hello World"}
