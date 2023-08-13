# Garbage Detection and Location Tracking API 🔑
## Introduction 👀
By identifying garbage in photos and recording the locations where it is found, this project's FastAPI-built API seeks to address the issue of incorrect waste disposal. It uses MongoDB to store the location information and the Hugging Face API to detect images.
## Tech Stack 🌐
- FastAPI: A cutting-edge, quick web framework for Python 3.7+ API development.
- MongoDB is a well-liked NoSQL database for holding and managing structured data.
- Hugging Face API: An AI research company that offers potent models and APIs for computer vision and natural language processing workloads.
- Python: The project's overall programming language.
## How it Works 🛠️
1. '/check/' and '/check_once/' are the API's two primary endpoints.
2. A coordinate (latitude and longitude) file and an image file are sent to the '/check/' endpoint. For garbage detection, it transmits the image to the Hugging Face API. The location data is saved in MongoDB if the AI algorithm identifies garbage with a particular level of confidence.
3. Direct position tracking without image detection is done with the '/check_once/' endpoint.
4. Timestamped location information is stored in MongoDB.
5. By making the endpoints for submitting data and receiving responses visible, the API establishes a connection with the frontend.
## API endpoints 🔚
- 'GET /' is a straightforward endpoint that delivers the message "Hello, world!"
- 'GET /blogs': This command retrieves blog data from the MongoDB database.
- "POST /check/": Accepts a coordinates and an image file. identifies any junk in the image and records its position.
- 'POST /check_once/': Accepts coordinates and saves the position.
## Connecting Mongodb 🍃
-For security purposes, the environment variables store the MongoDB URI.
- The 'pymongo' library is used by the API to establish a connection with the MongoDB server.
- For storing various forms of data, "blogs" and "location" are employed as two collections.

## Hugging Face API for Image Detection 🔎
- The API sends the image to the Hugging Face API for garbage detection.
- If garbage is detected with a certain confidence score, the location is stored in MongoDB.

## Running the API ⏳
1. Set up your MongoDB URI and Hugging Face API key in the `.env` file.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the API using `python main.py`.

## How It Connects to the Frontend 🖥️
- The frontend (not included here) can make HTTP requests to the API endpoints to send data and receive responses.
- The API responses can be processed by the frontend to display information to users.

## ScreenShot
![Images](images/WasteX_backend_ScreenShot.PNG)

## Postman Workspace 📁
[Postman Workspace Link 🔗](https://wastex.postman.co/workspace/Team-Workspace~2dd390f7-a202-4730-8ac2-b2c630ca84d6/overview)


