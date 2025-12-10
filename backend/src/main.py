#--- IGNORE ---
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # portul Vite pentru frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# aici importi si incluzi router-ele
# from src.api.routes import router
# app.include_router(router)
