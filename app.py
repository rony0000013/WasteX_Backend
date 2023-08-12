from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from bson import ObjectId
from typing import Annotated
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv()


#  URIs
MONGO_URI = str(os.getenv("MONGO_URI"))



# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["hack_database"]
blogs_collection = db["blogs"]
loc_collection = db["location"]



app = FastAPI()

# Your routes and middleware go here
@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


@app.get("/blogs")
def get_blogs():
    blogs = []
    for blog in blogs_collection.find():
        blog["_id"] = str(blog["_id"])
        blogs.append(blog)
    return {"blogs": blogs}


@app.get("/blogs/{id}")
def get_blogs( id: str):
    try:
        blog_id = ObjectId(id)
    except:
        return JSONResponse(status_code=400,  content={"message": "Invalid ID"})

    blog = blogs_collection.find_one({"_id": blog_id})
    if blog:
        blog["_id"] = str(blog["_id"])
        return {"blog": blog}
    else:
        return JSONResponse(status_code=404, content={"message": "Blog not found"})


@app.post("/check_once/")
async def create_upload_file(lat: float, long: float):
    if lat > 90 or lat < -90 or long > 180 or long < -180:
        return JSONResponse(status_code=400,  content={"message": "Invalid latitude or longitude"})
    
    result = loc_collection.insert_one({"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "lat": lat, "long": long})
    if result:
        return {"result": True, "recieved": str(result.inserted_id)}
    
    return JSONResponse(status_code=500,  content={"message": "Server Error"})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
