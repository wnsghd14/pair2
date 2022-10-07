from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request, "reviews/index.html")

def reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews,
    }
    return render(request, "reviews/reviews.html", context)

def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:home')

    else:
        review_form = ReviewForm()
    
    context = {
        "review_form" : review_form,
    }
    return render(request, "reviews/create.html", context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)

    context = {
        'review' : review,
    }
    return render(request, 'reviews/detail.html', context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:home')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail',review.pk)

    else:
        review_form = ReviewForm(instance=review)
    
    context = {
        "review_form" : review_form,
    }
    return render(request, "reviews/update.html", context)