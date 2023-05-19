import streamlit as st
import plotly.express as px
from pathlib import Path
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob


def get_month(file_name_):
    month_map = {"01": "Jan", "10": "Oct"}
    month_ = file_name_.split("-")[1]
    date_ = file_name_.split("-")[2]
    return f"{month_map[month_]} {date_}"


def read_file(file_path_):
    with open(file_path_) as file:
        content_ = file.read()
    return content_


def get_score(content_):
    analyzer = SentimentIntensityAnalyzer()
    score_ = analyzer.polarity_scores(content_)
    return score_


file_paths = glob.glob("files/*.txt")
file_paths.sort()
scores = []

for file_path in file_paths:
    content = read_file(file_path)
    file_name = Path(file_path).stem
    month = get_month(file_name)
    score = get_score(content)
    score.update(date=month)
    scores.append(score)
print(scores)

date_list = []
pos_list = []
neg_list = []
d = {}
for item in scores:
   neg, neu, pos, compound, date = item["neg"], item["neu"], item["pos"], item["compound"], item["date"]
   date_list.append(date)
   pos_list.append(pos)
   neg_list.append(neg)

st.title("Diary Tone")
st.subheader("Positivity")
figure_pos = px.line(x=date_list, y=pos_list, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_pos)
st.subheader("Negativity")
figure_neg = px.line(x=date_list, y=neg_list, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_neg)

# print(date_list)
# print(pos_list)
# print(neg_list)
# import glob
# import streamlit as st
# import plotly.express as px
#
# from nltk.sentiment import SentimentIntensityAnalyzer
#
# filepaths = sorted(glob.glob("files/*.txt"))
#
# analyzer = SentimentIntensityAnalyzer()
#
# negativity = []
# positivity = []
# for filepath in filepaths:
#     with open(filepath) as file:
#         content = file.read()
#     scores = analyzer.polarity_scores(content)
#     positivity.append(scores["pos"])
#     negativity.append(scores["neg"])
#
# dates = [name.strip(".txt").strip("files/") for name in filepaths]
#
# st.title("Diary Tone")
# st.subheader("Positivity")
# pos_figure = px.line(x=dates, y=positivity,
#                      labels={"x": "Date", "y": "Positivity"})
# st.plotly_chart(pos_figure)
#
# st.subheader("Negativity")
# neg_figure = px.line(x=dates, y=negativity,
#                      labels={"x": "Date", "y": "Negativity"})
# st.plotly_chart(neg_figure)