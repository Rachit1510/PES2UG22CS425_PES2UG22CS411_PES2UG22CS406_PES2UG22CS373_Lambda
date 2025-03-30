from fastapi import FastAPI
import uvicorn
from mangum import Mangum  # AWS Lambda adapter for FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Lambda API!"}

@app.get("/ping")
def ping():
    return {"status": "healthy"}

handler = Mangum(app)  # This is for AWS Lambda compatibility

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run locally
