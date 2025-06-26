from fastapi import APIRouter
from ..models import TextRequest, SentimentResponse
from ..services.sentiment_service import sentiment_service

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: TextRequest):
    """
    Analyzes the sentiment of the given text (positive/negative/neutral)
    and returns a confidence score.
    """
    sentiment_result = sentiment_service.get_sentiment(request.text)
    return sentiment_result