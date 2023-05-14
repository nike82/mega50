import requests
import streamlit as st

# Prepare API key and API url
api_key = "Ngt6d9k6dY2f3BZRDdpgGzgClzjiwsFbQ42Aqfnv"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
request = requests.get(url)
content = request.json()

# Extract the image title, url and, explanation
title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

# Download the image
image_path = "image.png"
request2 = requests.get(image_url)
with open(image_path, "wb") as file:
    file.write(request2.content)

st.title(title)
st.image(image_path)
st.write(explanation)


