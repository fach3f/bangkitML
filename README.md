# Machine Learning Model Serving with Flask
This project demonstrates how to deploy a machine learning model locally using Flask. The model predicts gym equipment based on an input image.

## Prerequisites
Before running the project, make sure you have the following installed:

Python 3.9
pip

## Setup
Clone the project repository:
```
git clone https://github.com/Fitmate/FitmateML.git
cd FitmateML
```
Install dependencies:
```
pip install -r requirements.txt
```

## Training the Model
Before deploying the model, ensure you have a pre-trained model file (model.h5) and a label file (labels.txt). If not, you need to train a model and save it in the project directory.

## Running the Flask App Locally
Start the Flask app:
```
python app.py
```
Open your web browser and go to http://localhost:8080 to check the health of the API.

## Usage
Use the /prediction endpoint to make predictions based on an input image.
```
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:8080/prediction
```
Replace path/to/your/image.jpg with the path to the image file you want to predict.

API Endpoints
Health Check
Path: /
Method: GET

Image Prediction
Path: /prediction
Method: POST
Payload: Form data with the image file.

Example Response
```
{
    "data": {
        "confidence": 0.9999995231628418,
        "exercise": {
            "data": {
                "cal_estimation": 150,
                "category": {
                    "name": "Strength"
                },
                "gif_url": "https://storage.googleapis.com/assets-fitmate/gif/dumbbel_bicep_curl_model.gif",
                "id": 1,
                "is_support_interactive": 1,
                "level": 1,
                "muscle": {
                    "name": "Arms"
                },
                "name": "Dumbbell Curl",
                "overview": "The dumbbell curl is a bicep exercise that targets the muscles in your arms.",
                "photo_url": "https://storage.googleapis.com/assets-fitmate/photo/dumbbel_bicep_curl_cover.jpg",
                "rating": 99,
                "required_equipment": {
                    "name": "Dumbells"
                },
                "step": "Stand with your feet shoulder-width apart, holding a dumbbell in each hand with your arms fully extended and palms facing forward., Keep your upper arms stationary and exhale as you curl the weights while contracting your biceps., Inhale and slowly begin to lower the dumbbells back to the starting position."
            }
        },
        "gym_equipment_prediction": "Dumbells"
    },
    "status": {
        "code": 200,
        "message": "Success Predicting"
    }
}
```
