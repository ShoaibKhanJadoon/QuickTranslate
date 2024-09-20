
from fastapi import FastAPI, Request
from pydantic import BaseModel
import translator as t
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now; you can restrict to specific domains.
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.).
    allow_headers=["*"],  # Allow all headers.
)


class TranslationRequest(BaseModel):
    text: str
    target_lang: str

@app.post("/translate/")
def translate(request: TranslationRequest):
    translated_text = t.translate_text(request.text,  request.target_lang)
    return {"translated_text": translated_text}