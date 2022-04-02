from django.http import HttpResponse

# Views
def polls(request):
    return HttpResponse("Hello, you're at the polls index.")
