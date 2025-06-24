# FastAPI Text Summarizer API
A high-performance RESTful API for abstractive text summarization, built with FastAPI and powered by state-of-the-art Hugging Face Transformer models.

This API allows users to send raw text and receive a concise, human-readable summary.
Key features include:
- **Abstractive Summarization:** Generates new sentences for summaries, not just extracting existing ones.
- **Fast Inference:** Leverages optimized Transformer models for quick responses.
- **Robust Input Validation:** Ensures data integrity using Pydantic.
- **Interactive Documentation:** Automatic API documentation via Swagger UI.

Built with:
- Python 3.9+
- FastAPI
- Hugging Face Transformers (with the sshleifer/distilbart-cnn-12-6 model)
- Pydantic
- Uvicorn

### Prerequisites
- Python 3.9+ installed
- Git installed
### Installation Steps
1. **Clone the repository:**
`git clone https://github.com/Aryakatre1/text-summarizer-fastapi.git`
`cd text-summarizer-fastapi`
2. **Create and activate a virtual environment:**
`python -m venv venv`
`.\venv\Scripts\activate` (for Windows PowerShell)
3. **Install dependencies:**
`pip install -r requirements.txt`
4. **Run the API server:**
`uvicorn main:app --reload`
The API will be accessible at http://127.0.0.1:8000.


Once the server is running, you can interact with the API using its interactive documentation or a tool like Postman.
### Interactive Documentation (Swagger UI)
Open your browser and navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Here you can test the \/summarize` endpoint directly.`
### Example Request (using Postman or curl)
**Endpoint:** POST /summarize
**Headers:** Content-Type: application/json
**Body (JSON):**
JSON

{
  "text": "Paste your long text here that you want to summarize. Make sure it's substantial enough for the summarization model to work effectively."
}
**Response Example:**
JSON

{
  "summary": "Your generated summary will appear here."
}

Future plans for this project include:
- Implementing support for batch summarization.
- Adding authentication/API key management for secure access.
- Exploring different summarization models for comparison and performance optimization.
- Deploying to a cloud platform (e.g., Google Cloud Run) for public accessibility.
- Building a simple frontend web application to consume the API.

Connect with me on [LinkedIn](https:www.linkedin.com/in/arya-katre-829b82260).
Email: [your.email@example.com](mailto:katrearya459@gmail.com)