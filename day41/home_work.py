import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __int__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def buy(self):
        """Buy an article by changing its count minus one"""
        df.loc[df["id"] == self.article_id, "in stock"] = df.loc[df["id"] == self.article_id, "in stock"] - 1
        df.to_csv("hotels.csv", index=False)

    def in_stock(self):
        """Checks if the article is in stock"""
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        return in_stock


class Receipt:
    def __int__(self, article_object):
        self.article = article_object

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.article_id}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{self.article.article_name}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.article_price}", ln=1)
        return pdf.output("receipt.pdf")


print(df)
article_id = input("Enter the id of the article to buy: ")
article = Article(article_id)

if article.in_stock():
    article.buy()
    receipt = Receipt(article)
    print(receipt.generate())
else:
    print("No such article in stock.")




