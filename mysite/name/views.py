from django.http import HttpResponse


def name(request):
    return HttpResponse("Tigran")

def surename(request):
	return HttpResponse("Danielyan")
