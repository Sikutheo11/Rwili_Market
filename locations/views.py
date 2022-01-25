from django.shortcuts import render
from .models import Province ,District, Sector, Cell, Village

# Create your views here.
def location(request):

	context = {

	 'provinceloc': province.objects.all(),
	 'districtloc': district.objects.all(),
	 'sectorloc': sector.objects.all(),
	 'cellloc': cell.objects.all(),
	 'villageloc': village.objects.all()
	}

	return render(request, 'orders/payments.html', context)