import tkinter as tk
from tkinter import scrolledtext
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve tokens from environment variables
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

# Function to fetch book details
def get_books(genre):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&key={GOOGLE_BOOKS_API_KEY}&maxResults=5"
    response = requests.get(url)
    data = response.json()

    books = []
    if 'items' in data:
        for item in data['items']:
            title = item['volumeInfo'].get('title', 'No title available')
            authors = ", ".join(item['volumeInfo'].get('authors', 'Unknown author'))
            description = item['volumeInfo'].get('description', 'No description available')
            published_date = item['volumeInfo'].get('publishedDate', 'Unknown date')
            language = item['volumeInfo'].get('language', 'Unknown language')
            preview_link = item['volumeInfo'].get('previewLink', 'No preview available')

            books.append({
                "title": title,
                "authors": authors,
                "description": description,
                "published_date": published_date,
                "language": language,
                "preview_link": preview_link
            })
    return books

def send_message():
    genre = entry_genre.get()
    books = get_books(genre)
    
    output_text.delete(1.0, tk.END)
    if books:
        for book in books:
            message = (
                f"Title: {book['title']}\n"
                f"Author(s): {book['authors']}\n"
                f"Description: {book['description']}\n"
                f"Published Date: {book['published_date']}\n"
                f"Language: {book['language']}\n"
                f"Preview: {book['preview_link']}\n\n"
            )
            output_text.insert(tk.END, message)
    else:
        output_text.insert(tk.END, 'No books found for this genre.')

# Set up the GUI
root = tk.Tk()
root.title("Book Recommendation Bot")

tk.Label(root, text="Enter Genre:").pack(pady=10)

entry_genre = tk.Entry(root, width=50)
entry_genre.pack(pady=5)

tk.Button(root, text="Get Recommendations", command=send_message).pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack(pady=10)

root.mainloop()

