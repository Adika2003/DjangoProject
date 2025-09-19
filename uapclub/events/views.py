from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def event_list(request):
    events = Event.objects.filter(published=True).order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if not request.user.is_staff:
        messages.error(request, 'Only staff can create events.')
        return redirect('events:event_list')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            ev = form.save(commit=False)
            ev.created_by = request.user
            ev.save()
            messages.success(request, 'Event created.')
            return redirect('events:event_detail', pk=ev.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

