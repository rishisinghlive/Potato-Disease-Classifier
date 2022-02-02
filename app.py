import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

model = tf.keras.models.load_model('potatoes.h5')
class_names = ['Early blight', 'Late blight', 'Potato healthy']

st.title('Potato Disease Classifier')

image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
if image_file is not None:
    image = Image.open (image_file)
    st.image(image, caption='Uploaded Image')
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    resize_image = tf.image.resize(input_arr,(256, 256))
    input_array = np.array([resize_image])

if st.button('submit'):
    score = model.predict(input_array)
    st.write('This is:', class_names[np.argmax(score)])
    st.write('The Probability of This plant of being',
             str(class_names[np.argmax(score)]),'is',
             str(np.round(np.max(score)*100))+'%')
