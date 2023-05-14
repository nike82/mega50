import requests
from send_email import send_email
# url = "https://finance.yahoo.com"

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=890603a55bfa47048e4490069ebee18c"

# Make request
request = requests.get(url)

# Get content
content = request.json()
body = ""
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"
body = body.encode("utf-8")
send_email(body)
print(body)
