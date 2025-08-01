from django.shortcuts import render

def analytics_dashboard(request):
    return render(request, 'sales_analytics/index.html')
