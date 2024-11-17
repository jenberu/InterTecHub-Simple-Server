from django.http import JsonResponse ,HttpResponse

def my_name(request):
    return HttpResponse("Jemberu Kassie")
def my_hobby(request):
    return JsonResponse({"hobby": "Exploring technology related things"})
def my_dream(request):
    return HttpResponse("My dream is to build impactful technology solutions .")