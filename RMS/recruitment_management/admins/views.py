from django.shortcuts import render
from .models import PlacementDrive

def admin_dashboard(request):
    # Sample data, replace with actual logic
    context = {
        'placement_drives': PlacementDrive.objects.all(),
    }
    return render(request, 'admin_dashboard.html', context)

