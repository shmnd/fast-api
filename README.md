# FastAPI CRUD Application

A basic CRUD (Create, Read, Update, Delete) API built with FastAPI.

## Setup

1.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:

-   Swagger UI: http://127.0.0.1:8000/docs
-   ReDoc: http://127.0.0.1:8000/redoc

## Testing

Run the verification script to test all endpoints:

```bash
python verify_api.py
```
# fast-api
