from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/callback")
def callback():
    # Handle the OAuth callback here
    return {"status": "callback received"}

