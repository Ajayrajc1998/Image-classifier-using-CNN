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

# Streamlit UI
st.title("Image Classification of Coffee Plant Leaves")

st.markdown("### Test Data Image Folder")
st.markdown("You can access the test data images from the following link:")
st.markdown("[Test Data Image Folder](https://drive.google.com/drive/folders/1W6Ih82BelCySBF9_v722TWENPxit2rmM?usp=sharing)")

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