from django.shortcuts import render
from textblob import TextBlob
from .forms import CommentForm
from .models import Comment
import requests

# Helper function to summarize text using OpenRouter
def get_ai_summary(text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mistral-small-3.1-24b-instruct:free",
        "messages": [
            {"role": "user", "content": f"Make a summary for this comment: {text}"}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        summary = data['choices'][0]['message']['content']
        return summary
    except requests.RequestException as e:
        # Log the error and return fallback
        print(f"Error contacting OpenRouter: {e}")
        return "Summary not available"

def analyze_view(request):
    result = None
    summary = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            
            # TextBlob sentiment analysis
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity
            if polarity > 0:
                result = "Positive 😊"
            elif polarity < 0:
                result = "Negative 😡"
            else:
                result = "Neutral 😐"

            # Get AI summary
            summary = get_ai_summary(text)

            # Save comment to DB
            Comment.objects.create(text=text, sentiment=result, summary=summary)
    else:
        form = CommentForm()

    comments = Comment.objects.order_by('-created_at')[:5]

    return render(request, 'pages/sentiment.html', {
        'form': form,
        'result': result,
        'comments': comments,
        'summary': summary
    })
