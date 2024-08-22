import requests
import streamlit as st



API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-turbo"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs":st.text_input('Enter Prompt'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate'):
    st.image(image)
