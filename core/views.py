from django.shortcuts import render
from textblob import TextBlob
from .forms import CommentForm
from .models import Comment

# Create your views here.

def analyze_view(request):
    reult = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity

            if polarity > 0:
                result = "Positive 😊"
            elif polarity < 0:
                result = "Negative 😡"
            else:
                result = "Neutral 😐"

            Comment.objects.create(text=text, sentiment=result)

    else:
        form = CommentForm()
    
    comments = Comment.objects.order_by('-created_at')[0:5]
    return render(request, 'pages/sentiment.html', {'form' : form, 'result' : result, 'comments' : comments})
