# knowledge-base-search-engine
A Retrieval-Augmented Generation (RAG) based search engine that allows users to upload documents (PDF/TXT) and query them for synthesized answers using LLM.

## Deliverables :
github link : `https://github.com/pavan-parimi/knowledge-base-search-engine`

Demo video link : `https://drive.google.com/file/d/1fbfQK0XT1lAik4OHST8hpZM4OaF9dOgP/view?usp=drivesdk`

## Features
- Document ingestion: Upload multiple PDF and TXT files
- Embeddings: Uses OpenAI embeddings for vectorization
- Vector store: FAISS for efficient similarity search
- LLM: OpenAI GPT for answer synthesis
- API: FastAPI backend
- Frontend: Simple web interface for upload and query
## Setup
1. Ensure Python 3.11+ is installed.
2. Clone or download the project.
3. Navigate to the project directory.
4. Create virtual environment:
   ```
   py -3 -m venv venv
   ```
5. Activate the environment:
   ```
   call venv\Scripts\activate.bat
   ```
6. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
7. Set your OpenAI API key:
   ```
   set OPENAI_API_KEY=your_api_key_here
   ```
8. Run the application:
   ```
   uvicorn main:app --reload
   ```
9. Open your browser to `start http://127.0.0.1:5000`
## Usage
1. Upload documents using the upload form (select multiple PDF/TXT files).
2. Once uploaded, enter a query in the query field and click Search.
3. The synthesized answer will be displayed.
## API Endpoints
- `POST /upload`: Upload files (multipart/form-data)
- `POST /query`: Query with JSON body {"query": "your question"}
- `GET /`: Serve the frontend
