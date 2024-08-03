from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BusRoute

paginate_by = 1


def index(request):
    global paginate_by
    bus_routes = BusRoute.objects.all().order_by('number')
    paginate_by = request.GET.get('paginate_by') or paginate_by
    page_number = request.GET.get('page') or 1
    paginator = Paginator(bus_routes, paginate_by)
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj, 'paginate_by': paginate_by})
