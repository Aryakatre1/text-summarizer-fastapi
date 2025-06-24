# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load the summarization model globally to avoid loading it on every request
# This will take some time when the application starts for the first time
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    print(f"Error loading summarization model: {e}")
    summarizer = None # Set to None if loading fails, handle this in the endpoint

# Define a Pydantic model for request body validation
class TextInput(BaseModel):
    text: str

# Existing "Hello World" endpoint (optional, you can remove it if you want)
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Simple Text Summarizer API!"}

# New endpoint for summarization
@app.post("/summarize")
async def summarize_text(input_data: TextInput):
    # Basic error handling: check if the model loaded successfully
    if summarizer is None:
        raise HTTPException(status_code=500, detail="Summarization model not loaded. Please check server logs.")

    # Basic error handling: check for empty input text
    if not input_data.text or input_data.text.strip() == "":
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    try:
        # Perform summarization
        # You can adjust max_length and min_length as needed
        summary_result = summarizer(input_data.text, max_length=130, min_length=30, do_sample=False)
        summary = summary_result[0]['summary_text']
        return {"summary": summary}
    except Exception as e:
        # Catch any unexpected errors during summarization
        raise HTTPException(status_code=500, detail=f"An error occurred during summarization: {str(e)}")

# To run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

