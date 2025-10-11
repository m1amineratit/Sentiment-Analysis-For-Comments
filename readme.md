# Sentiment Analyzer for Comments

The **Sentiment Analyzer for Comments** is a Django web app that lets users paste any comment (e.g., from YouTube, X, or Reddit) and instantly see whether it’s **Positive**, **Negative**, or **Neutral**.

It uses the **TextBlob** library for sentiment analysis and stores results in a database for quick review.

## Features

- Paste any comment and get instant sentiment analysis.
- Sentiment categories: Positive 😊, Negative 😡, Neutral 😐.
- Recent analyzed comments are displayed for review.
- Built with Django and TextBlob.

## Getting Started

1. **Clone the repository**  
   `git clone https://github.com/m1amineratit/Sentiment-Analysis-For-Comments.git`

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Apply migrations**  
   ```
   python manage.py migrate
   ```

4. **Run the development server**  
   ```
   python manage.py runserver
   ```

5. **Access the app**  
   Open [http://localhost:8000/](http://localhost:8000/) in your browser.

## Requirements

- Python 3.10+
- Django 5.2+
- TextBlob

## Project Structure

- `core/` — Main app with models, forms, views, and migrations.
- `system/` — Django project settings and configuration.
- `templates/pages/` — HTML templates.

## License

MIT License