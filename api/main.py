import base64
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request: Request):
    principal_name = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME", "Not available")

    return {
        "X-MS-CLIENT-PRINCIPAL-NAME": principal_name,
    }
