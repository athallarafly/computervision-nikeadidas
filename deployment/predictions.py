import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from io import BytesIO
import requests

# Load the Keras model
model = tf.keras.models.load_model('model_2.h5', compile=False)

# Define class names for interpretation
class_names = ['Adidas', 'Nike']

def preprocess_image(image):
    # Resize the image to the required input size (e.g., 150x150 for your model)
    img = image.resize((150, 150))
    
    # Convert the image to an array of pixel values
    img_array = np.asarray(img)
    
    # Normalize pixel values to be in the range [0, 1]
    img_array = img_array / 255.0
    
    # Expand dimensions to create a batch (add a dimension for batch size)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict_class(image):
    processed_image = preprocess_image(image)

    # Make predictions using the loaded Keras model
    predictions = model.predict(processed_image)

    # Apply threshold to predictions
    model_pred_final = np.where(predictions >= 0.35, 1, 0)

    # Get the predicted class label
    predicted_class = class_names[model_pred_final[0][0]]

    return predicted_class

def run():
    st.title('Prediction Image')
    st.write('Predict image like Adidas or Nike')

    option = st.radio("Choose Input Method:", ("File Upload", "Image URL"))

    if option == "File Upload":
        uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Open the image from the file uploader
            img = Image.open(uploaded_file)

            # Display the image
            st.image(img, caption='Uploaded Image', use_column_width=True)

            if st.button('Predict'):
                # Get the predicted class label
                predicted_class = predict_class(img)

                # Display the predicted class
                st.write(f'Prediction is a : {predicted_class}')
    else:
        url = st.text_input("Enter Image URL:")

        if url:
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))

                # Display the image
                st.image(img, caption='Uploaded Image', use_column_width=True)

                if st.button('Predict'):
                    # Get the predicted class label
                    predicted_class = predict_class(img)

                    # Display the predicted class
                    st.write(f'Prediction is a : {predicted_class}')
            except Exception as e:
                st.write(f"Error: {e}")

# Run the Streamlit app
if __name__ == '__main__':
    run()