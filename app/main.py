from dotenv import load_dotenv

from fastapi import FastAPI
import ngrok
import uvicorn

from app.student import Student
from ml_model.useModel import UseModel

# Loading the .env file
load_dotenv()
# Setting up the Desired port for server.
APPLICATION_PORT = 8000

# setting up the connection to the static domain on same port as uvicorn
listener = ngrok.forward(addr=APPLICATION_PORT, domain="mole-model-drake.ngrok-free.app", authtoken_from_env = True)

# FastAPI app init
app = FastAPI()

# initializing the model
model = UseModel()


# Home of the API
@app.get("/")
async def root():
    return {"message": "Hello Welcome to the Admission prediction Application"}

# get request to say hello based on the path.
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Post method to perdict the
@app.post('/predict')
async def predict(student: Student):
    result = model.predict(student.gre, student.toefl, student.university_rating, student.sop, student.lor, student.cgpa, student.research)
    return {
        "data": {
            "Name": student.name,
            "Admission chances": f"{result*100}%",
        }
    }


if __name__ == "__main__":
    listener = ngrok.forward(addr=APPLICATION_PORT, domain="mole-model-drake.ngrok-free.app", authtoken_from_env = True)
    print(listener.url())
    uvicorn.run("main:app", host="0.0.0.0", port=APPLICATION_PORT, reload=True)
    ngrok.disconnect()