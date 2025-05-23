from django.shortcuts import render, redirect
from plane_app.models import Airline, Manufacturer
from django.http import HttpResponseServerError

from plane_app.services.airplane_service import AirplaneService

airplane_service = AirplaneService()

def airplane_list(request):
    try:
        airplanes = airplane_service.get_all_airplanes()
        return render(request, 'airplane_list.html', {'airplanes': airplanes})
    except:
        return render(request, 'error.html', {'message': 'Помилка в опрацюванні запиту. Спробуйте пізніше.'})

def airplane_detail(request, airplane_id=None):
    try:
        airplane = None
        if airplane_id:
            airplane = airplane_service.get_airplane(airplane_id)

        if request.method == 'POST':
            data = {
                'model': request.POST['model'],
                'capacity': request.POST['capacity'],
                'airline_id': request.POST['airline'],
                'manufacturer_id': request.POST['manufacturer'],
                'year_produced': request.POST['year_produced']
            }

            if airplane:
                airplane_service.update_airplane(airplane_id, data)
            else:
                airplane_service.create_airplane(data)

            return redirect('airplane_list')

        airlines = Airline.objects.all()
        manufacturers = Manufacturer.objects.all()

        return render(request, 'airplane_detail.html', {
            'airplane': airplane,
            'airlines': airlines,
            'manufacturers': manufacturers
        })
    except :
        return render(request, 'error.html', {'message': 'Помилка в опрацюванні запиту. Спробуйте пізніше.'})

def airplane_delete(request, airplane_id):
    try:
        airplane_service.delete_airplane(airplane_id)
        return redirect('airplane_list')
    except:
        return render(request, 'error.html', {'message': 'Помилка в опрацюванні запиту. Спробуйте пізніше.'})

def airplane_view(request, airplane_id):
    try:
        airplane = airplane_service.get_airplane(airplane_id)
        return render(request, 'airplane_view.html', {'airplane': airplane})
    except ValueError:
        return render(request, 'error.html', {'message': 'Помилка в опрацюванні запиту. Спробуйте пізніше.'})

