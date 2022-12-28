# Import necessary libraries
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

# Define the URL of the website to crawl
url = "https://www.igeneratedigital.com.au"

# Send an HTTP request to the server and retrieve the HTML content of the webpage
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Extract the relevant information from the HTML content
content = soup.find("div", {"class": "content"}).text

# Perform a sentiment analysis on the extracted text using TextBlob
sentiment = TextBlob(content).sentiment.polarity

# Output the results of the sentiment analysis
print(f"The sentiment of the content on {url} is {sentiment:.2f}")
