# Admission Prediction App using FastAPI
This is a Python Web Application that is serves as an example on integrating
ML models to FastAPI to allow other applications to interact with the ML model
via an API endpoint. The FastAPI provides the API functionality and the ngrok
services allows us to deploy to the web for global access.

### Technologies Used:
- FastAPI - Used this for building API that interact with the model and giving us the prediction
- Unicorn - Used as a ASGI Web Server for Hosting the FastAPI Application
- Ngrok - Used to expose the local endpoint to globally hosted endpoint. 
- Pydantic - Used as a Data Validation Library for FastAPI POST requests.
- Scikit-Learn - Used for loading trained model into memory and predict the result
- Pandas, Numpy - Shape the inputs in desired format for the Predictive model.

## Pre-requisites to run the Project
To run this project, you need few things:
- Installed Python 3.9+
- Python IDE of your choice (Pycharm in my case)

## How to run the Project
#### Clone this project
Use `git clone` to clone this repository to your local system.
```shell
git clone https://github.com/syedsadiquh/Admission-Prediction-FastAPI.git
```

#### Create a Virtual Python Environment
Although virtual python environment (venv) is not necessary for running this project. 
It is recommended to use a virtual environment as ngrok and other packages are 
specific to this project and may clash with other versions.
<br>To create a new python venv. First, open the cloned repo in your favourite IDE
and open the terminal. Run this command while being in the project's directory.
```shell
python -m venv venv
```
Now, that the venv is created with name 'venv'. Activate it using specific command for your OS:
<br>Macos `source activate venv/bin/activate`
<br>Windows (in CMD) `env/Scripts/activate.bat`
<br>Windows (in powershell) `env/Scripts/Activate.ps1`

#### Install dependencies
Install the required packages for this project.
Run:
```shell
pip install -r requirements.txt
```

#### Setting up Ngrok account
Signup/Login for Ngrok account (free or paid). 
Get your AuthToken from ngrok.

#### Setting up the Environment
Create a `.env` file in the root of the project.
Paste the AuthToken obtained from ngrok as 'NGROK_AUTHTOKEN'
```env
NGROK_AUTHTOKEN = xxxxxxxxxxxxxxx_xxxxxxxxxxx
```
NOTE: Replace "xxxxxxx...." with your AuthToken.

#### Setting up the Domain
If you don't have a static domain, Please omit the domain parameter in forward()<br>
i.e. use as `listener = ngrok.forward(addr=APPLICATION_PORT, authtoken_from_env = True)`<br>
Ngrok will provide a random url for your project that can be viewed at your ngrok dashboard.

If you have a static domain, replace the provided domain to your static domain.

#### Run the Project
The final Project Structure should look like :
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py
│   └── student.py
├── ml_model
│   ├── admission_prediction_model.h5
│   └── useModel.py
├── requirements.txt
├── test_main.http
└── venv
    ├── bin ...
    ├── lib ...
    └── pyvenv.cfg
```
NOTE: The `main.py` has been inside a app directory with empty `__init__.py` for Docker support. 
It is not mandatory to follow this structure. Changes to the commands are to be made accordingly.

To Run the Project:
```shell
./venv/bin/python -m uvicorn app.main:app --reload
```
The project's Swagger Docs can be view at http://127.0.0.1:8000/docs

## How to use the Project
This Project can be used as an example for using FastAPI to utilize the 
trained models for prediction. It utilizes ngrok for providing an global 
endpoint that can be integrated to different application and use the 
trained model as per their requirement. 

## Swagger Docs Screenshots

