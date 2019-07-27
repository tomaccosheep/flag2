from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Color, Flag, FavoriteColor, FavoriteFlag
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
	colors = Color.objects.all()
	context = {'colors': colors}
	return render(request, 'get_flags/index.html', context)

def index_api(request):
	colors = Color.objects.all()
	url = 'http://localhost:8000/get_flags/flags_api/'
	context = {'colors': colors, 'url': url}
	return render(request, 'get_flags/index_api.html', context)

def get_flags(request):
	color_list = request.POST.getlist('colors')
	if len(color_list) == 0:
		return HttpResponseRedirect(reverse('get:index'))
	flags = Flag.objects
	for color in color_list:
		flags = flags.filter(color=color)
	print(flags)
	context = {'flags': flags}
	return render(request, 'get_flags/flags.html', context)

def get_flags_api(request):
    color_list = request.GET.getlist('colors')
    print(color_list)
    if len(color_list) == 0:
        return HttpResponse('No Colors Selected')
    flags = Flag.objects
    name_error = False
    try:
        for color in color_list:
            flags = flags.filter(color=Color.objects.get(name=color))
    except Color.DoesNotExist:  # DoesNotExist:
        name_error = True
        flags = []
    print(flags)
    flag_list = [flag.country for flag in flags]
    context = {'flags': flag_list, 'name_error': name_error}
    return JsonResponse(context)

@csrf_exempt
def fav_country(request):
	active_user = request.user
	request_dict = json.loads(request.body)
	active_country = request_dict.get('country', None)
	# active_country = request.GET['country']
	print(active_user, active_country)
	fav_flag = FavoriteFlag(user=active_user, flag=Flag.objects.get(country=active_country))
	fav_flag.save()
	return HttpResponse('good')
