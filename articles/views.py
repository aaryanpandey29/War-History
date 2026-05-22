from django.http import HttpResponse


def battles(request):
    return HttpResponse("Hello, world. You're at the battles index")


def detail(request, article_id):
    return HttpResponse(
        "You are looking at the detailed battle page of %s" % article_id
    )
