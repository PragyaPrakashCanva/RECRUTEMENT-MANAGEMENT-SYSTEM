from django.shortcuts import render
from .models import Student

def student_dashboard(request):
    # Sample data, replace with actual logic
    context = {
        'student': Student.objects.first(),
        'placement_drives': [
            {'company_name': 'Company A', 'job_role': 'Developer', 'date': '2024-07-10'},
            {'company_name': 'Company B', 'job_role': 'Designer', 'date': '2024-07-15'}
        ]
    }
    return render(request, 'student_dashboard.html', context)
