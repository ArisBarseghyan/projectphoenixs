from django.shortcuts import render


def account_view(request):
    user = request.user
    return render(request, 'login/profile.html', {'user':user})
