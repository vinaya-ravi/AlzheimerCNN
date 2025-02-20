from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Load your trained model
model = load_model("models/ConvolutionalNeuralNetwork_model.h5")

# Define class labels
class_labels = ["Non Demented", "Very Mild Dementia", "Mild Dementia", "Moderate Dementia"]
@app.get("/")
def read_root():
    return {"message": "Welcome to the Alzheimer Detection API!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Load the uploaded image
    image = Image.open(file.file).resize((128, 128))
    image_array = np.array(image) / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(image_array)
    predicted_class = class_labels[np.argmax(predictions)]

    confidence = float(round(100 * np.max(predictions), 2))
    return {"class": predicted_class, "confidence": confidence}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to ["http://localhost:3000"] for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

