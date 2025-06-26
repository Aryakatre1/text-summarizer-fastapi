from fastapi import APIRouter
from ..models import TextRequest, SummaryResponse
from ..services.summarization_service import summarization_service

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: TextRequest):
    """
    Summarizes the given text using a pre-trained Hugging Face model.
    """
    summary_text = summarization_service.get_summary(request.text)
    return {"summary": summary_text}