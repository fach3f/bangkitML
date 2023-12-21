# Machine Learning Model Serving with Flask

This project demonstrates how to deploy a machine learning model locally using Flask. The model predicts gym equipment based on an input image.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- pip

## Setup

Clone the project repository:

```bash
git clone https://github.com/Fitmate-capstone/back-end-ml.git
cd back-end-ml
```

Create Virtual Environment and activate the Virtual Environment:

```
python -m venv .venv
```

- Windows:

```
.venv\Scripts\activate
```

- Linux:

```
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Model

Before deploying the model, ensure you have a pre-trained model file (model.h5) and a label file (labels.txt).

## Running the Flask App Locally

Start the Flask app:

```
flask run
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
                []
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
