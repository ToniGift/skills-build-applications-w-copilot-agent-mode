from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the Octofit API!",
        "url": "https://zany-space-orbit-655g4pwggqgh5gpr.github.dev/"
    })
