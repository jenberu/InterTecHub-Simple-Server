from django.http import JsonResponse ,HttpResponse

def home(request):
    response_content = """
    <html>
        <body>
            <h1>Welcome to My Simple Django Server!</h1>
            <ul>
                <li><a href="/message/name">Name</a></li>

                <li><a href="/message/hobby">Hobby</a></li>
                <li><a href="/message/dream">Dream</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(response_content)
def my_name(request):
    return HttpResponse("Jemberu Kassie")
def my_hobby(request):
    return JsonResponse({"hobby": "Exploring technology related things"})
def my_dream(request):
    return HttpResponse("My dream is to build impactful technology solutions .")