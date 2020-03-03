from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
# Create your views here.

def get_name(request):
	if request.method == 'POST':
		print(request.POST)
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = NameForm()

	return render(request, 'learn/name.html', {'form': form})

