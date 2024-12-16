from django.shortcuts import render, redirect, get_object_or_404
from app.models.data.models import  Publisher
from app.forms.forms import PublisherForm

# Publisher Views
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'library/publisher_list.html', {'publishers': publishers})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'library/publisher_form.html', {'form': form})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'library/publisher_form.html', {'form': form})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'library/publisher_confirm_delete.html', {'publisher': publisher})
