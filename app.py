from fastapi import FastAPI

app = FastAPI()

# Your routes and middleware go here
@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}
