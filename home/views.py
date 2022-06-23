from django.shortcuts import render, redirect
from .models import Hotel_Room_Application_Record

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def records(request):
    posts = Hotel_Room_Application_Record.objects.all().order_by('-timestamp')
    context = {
        'posts': posts
    }
    return render(request, 'home/booking_records.html', context)

def details(request, ID):
    detail = Hotel_Room_Application_Record.objects.get(id=ID)
    context = {
        'posts':detail
    }
    return render(request, 'home/details.html', context )

def book_room(request):
    if request.method == 'POST':
        roomnumber = request.POST.get('Roomnumber')
        amountpaid = request.POST.get('Amountpaid')
        occupantname = request.POST.get('Occupantname')
        occupantemail = request.POST.get('Occupantemail')
        occupantoccupation = request.POST.get('Occupantoccupation')
        nightNumber = request.POST.get('NightNumber')
        startdate = request.POST.get('Startdate')
        enddate = request.POST.get('Enddate')
        admin_user = request.user

        new_records = Hotel_Room_Application_Record(Room_number=roomnumber, Amount_paid_in_Naira=amountpaid, Occupant_Name=occupantname, Occupant_email=occupantemail, Occupant_occupation=occupantoccupation, Number_of_night=nightNumber, Start_date=startdate, End_date=enddate, Registered_by=admin_user)

        new_records.save()
        return redirect('home:recordview')
    return render(request, 'home/book_room.html')