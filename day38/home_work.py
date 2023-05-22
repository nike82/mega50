import requests
import selectorlib
from datetime import datetime
import time

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def scrape(url):
    """Scrape the source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract_hw.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    now = datetime.now()
    data = now.strftime("%Y-%m-%d-%H-%M-%S")
    with open("data_hw.txt", "a") as file:
        full_content = f"{data},{extracted}\n"
        file.write(full_content)


if __name__ == "__main__":
    count = 0
    while count != 5:
        count += 1
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(2)


# df = pd.read_csv("data_hw.txt")
# figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "date", "y": "temperature"})
# st.plotly_chart(figure)
