from fastapi import FastAPI

app = FastAPI()

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

