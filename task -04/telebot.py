import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Retrieve tokens from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

# Function to fetch book details from Google Books API
async def get_books(genre):
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

# Define command handler for /start
async def start_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome to PagePal! Send me a genre, and I\'ll recommend some books for you.')

# Define message handler for text messages
async def recommend_books(update: Update, context: CallbackContext) -> None:
    genre = update.message.text
    books = await get_books(genre)

    if books:
        for book in books:
            message = (
                f"*Title:* {book['title']}\n"
                f"*Author(s):* {book['authors']}\n"
                f"*Description:* {book['description']}\n"
                f"*Published Date:* {book['published_date']}\n"
                f"*Language:* {book['language']}\n"
                f"[Preview]({book['preview_link']})\n"
            )
            await update.message.reply_text(message, parse_mode='Markdown')
    else:
        await update.message.reply_text('No books found for this genre.')

# Main function to start the bot
def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recommend_books))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

