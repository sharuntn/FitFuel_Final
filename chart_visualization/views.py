from django.shortcuts import render
from django.utils import timezone
import datetime
from foodlens.models import Intake

def chart_pg(request):
    # Get the current user
    user = request.user
    
    # Get today's date
    today = timezone.now().date()
    
    # Query the Intake model to get the calories and timestamps consumed by the user today
    intake_data = Intake.objects.filter(user=user, timestamp__date=today).values('calories', 'timestamp','quantity')
    
    # Extract calories and timestamps into separate lists
    calories_list = []
    timestamps_list = []
    for entry in intake_data:
        calories_list.append(entry['calories']*entry['quantity'])
        timestamps_list.append(entry['timestamp'])
    
    # Convert timestamps to string format
    timestamps_list = [x.strftime("%Y-%m-%d %H:%M:%S") for x in timestamps_list]

    # print(calories_list)
    # print(timestamps_list)
    
    # Return the data as a JSON response
    return render(request, 'sample_chart.html', {'calories_list': calories_list, 'timestamps_list': timestamps_list})
