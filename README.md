📋 Extracting Data from JSON
A Python script that fetches JSON data from a remote URL, parses it, calculates the total sum of all count values, and counts how many times each name appears.

🔍 What It Does
Takes a URL as input from the user
Fetches the JSON file from that URL over the internet
Parses the JSON and finds all comments
Calculates the total sum of all count values
Counts how many times each name appears in the comments


🛠️ Technologies Used
json — to parse JSON data
urllib.request — to fetch data from a URL
ssl — to handle HTTPS connections


▶️ How to Run
When prompted, enter the URL:
Enter url here: https://py4e-data.dr-chuck.net/comments_2203407.json

📦 Example JSON Structure
json{
  "comments": [
    { "name": "Romina", "count": 97 },
    { "name": "Laurie", "count": 45 },
    { "name": "Romina", "count": 12 }
  ]
}
