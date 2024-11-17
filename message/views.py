from django.http import JsonResponse ,HttpResponse

def home(request):
    return JsonResponse({"hobby-url": "http://127.0.0.1:8000/messages/hobby",
                         "name-url":"http://127.0.0.1:8000/messages/name",
                         "dream-url":"http://127.0.0.1:8000/messages/dream"})
def my_name(request):
    return HttpResponse("Jemberu Kassie")
def my_hobby(request):
    return JsonResponse({"hobby": "Exploring technology related things"})
def my_dream(request):
    return HttpResponse("My dream is to build impactful technology solutions .")