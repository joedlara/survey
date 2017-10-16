from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'form/index.html')

def results(request):
	return render(request, 'form/results.html')

def show(request):
	try:
		request.session['submitted'] += 1

	except:
		request.session['submitted'] = 0
	if request.method == "POST":

		request.session['name'] = request.POST['name']
		request.session['dojo'] = request.POST['dojo']
		request.session['language'] = request.POST['language']
		request.session['comments'] = request.POST['comments']
	return redirect('/results')



