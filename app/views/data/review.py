from django.shortcuts import render, redirect, get_object_or_404
from app.models.data.models import  Review
from app.forms.forms import  ReviewForm

# Review Views
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'app/review/review_list.html', {'reviews': reviews})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'app/review/review_form.html', {'form': form})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'app/review/review_form.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'app/review/review_confirm_delete.html', {'review': review})