import tkinter as tk 
import nltk
from textblob import TextBlob 
from newspaper import Article

def sentiment_analysis(sentimental_txt, article):
    # Sentiment analysis
    analysis = TextBlob(article.text)
    sentimental_txt.delete('1.0','end')
    sentimental_txt.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

def summarize(url_text, title_txt, author_txt, published_txt, summary_txt, sentimental_txt):

    nltk.download('punkt')

    # Reading the URL and parsing it
    url = url_text.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Enabling UI to update current text value
    title_txt.config(state="normal")
    author_txt.config(state="normal")
    published_txt.config(state="normal")
    summary_txt.config(state="normal")
    sentimental_txt.config(state="normal")

    # Cleaning the text field to insert the new value
    title_txt.delete('1.0','end')
    title_txt.insert('1.0', article.title)

    author_txt.delete('1.0','end')
    author_txt.insert('1.0', article.authors)

    published_txt.delete('1.0','end')
    published_txt.insert('1.0', article.publish_date)

    summary_txt.delete('1.0','end')
    summary_txt.insert('1.0', article.summary)

    sentiment_analysis(sentimental_txt, article)

    # Disabling text field after showing the results
    title_txt.config(state="disable")
    author_txt.config(state="disable")
    published_txt.config(state="disable")
    summary_txt.config(state="disable")
    sentimental_txt.config(state="disable")

def user_interface():

    # UI - TK
    root = tk.Tk()
    root.title("News Summarizer")
    root.geometry("1200x600")

    title_label = tk.Label(root, text="Title")
    title_label.pack()

    title_txt = tk.Text(root, height=1, width=140)
    title_txt.config(state='disabled', bg='#dddddd')
    title_txt.pack()

    author_label = tk.Label(root, text="Author")
    author_label.pack()

    author_txt = tk.Text(root, height=1, width=140)
    author_txt.config(state='disabled', bg='#dddddd')
    author_txt.pack()

    published_date_label = tk.Label(root, text="Published Date")
    published_date_label.pack()

    published_txt = tk.Text(root, height=1, width=140)
    published_txt.config(state='disabled', bg='#dddddd')
    published_txt.pack()

    summary_label = tk.Label(root, text="Summary")
    summary_label.pack()

    summary_txt = tk.Text(root, height=20, width=140)
    summary_txt.config(state='disabled', bg='#dddddd')
    summary_txt.pack()

    sentimental_label = tk.Label(root, text="Sentimental Analysis")
    sentimental_label.pack()

    sentimental_txt = tk.Text(root, height=1, width=140)
    sentimental_txt.config(state='disabled', bg='#dddddd')
    sentimental_txt.pack()

    url_label = tk.Label(root, text="URL")
    url_label.pack()

    url_text = tk.Text(root, height=1, width=140)
    url_text.pack()

    btn = tk.Button(root, text="Summarize", command= lambda: summarize(url_text, title_txt, author_txt, published_txt, summary_txt, sentimental_txt))
    btn.pack()

    root.mainloop()

user_interface()
