import requests

url = "https://hips.hearstapps.com/clv.h-cdn.co/assets/17/26" \
      "/1600x1040/gallery-1498838810-gettyimages-461493851.jpg"

response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)


