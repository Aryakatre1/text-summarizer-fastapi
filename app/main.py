from fastapi import FastAPI
from .routers import summarizer, sentiment 

app = FastAPI(
    title="AI Text Analysis API",
    description="A backend API for text summarization and sentiment analysis using Hugging Face models.",
    version="0.1.0",
)

app.include_router(summarizer.router)
app.include_router(sentiment.router) 