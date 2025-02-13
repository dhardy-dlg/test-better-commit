from fastapi import FastAPI

app = FastAPI(
    title="My Custom API",
    docs_url="/custom-docs",  # Custom URL for Swagger UI
    redoc_url="/custom-redoc",  # Custom URL for ReDoc
)

# app
@app.get("/")
async def root():
    return {"message": "Hello World"}
