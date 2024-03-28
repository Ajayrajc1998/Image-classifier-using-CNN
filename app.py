import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
import requests

def download_model():
    model_url = "https://github.com/Ajayrajc1998/Image-classifier-using-CNN/raw/main/model.h5"
    model_path = "model.h5"
    response = requests.get(model_url)
    response.raise_for_status()
    with open(model_path, "wb") as f:
        f.write(response.content)
    return model_path

def load_model():
    model_path = download_model()
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

def image_prediction(image_path):
  import cv2
  import numpy as np
  resized_image = cv2.resize(image, (256, 256))
  resized_image = resized_image / 255.0  # Normalize
  prediction = model.predict(np.expand_dims(resized_image, axis=0))[0]
  return prediction
#   if prediction > 0.5:
#     #print(f'Miner')
#     return 'Miner'
#   else:
#       #print(f'Healthy')
#       return 'Healthy'

# Streamlit UI
st.title("Image Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and display the image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Make prediction
    if st.button("Predict"):
        prediction = image_prediction(image)
        if prediction > 0.5:
            st.write("Prediction: Miner")
        else:
            st.write("Prediction: Healthy")