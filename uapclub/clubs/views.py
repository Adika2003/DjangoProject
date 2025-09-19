from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
from .forms import ClubForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/index.html', {'clubs': clubs})

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})

def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request, 'clubs/club_detail.html', {'club': club})

@login_required
def club_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Only staff can create clubs.')
        return redirect('clubs:club_list')
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Club created.')
            return redirect('clubs:club_list')
    else:
        form = ClubForm()
    return render(request, 'clubs/club_form.html', {'form': form})

