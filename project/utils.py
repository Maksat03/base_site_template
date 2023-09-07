from django.shortcuts import render


def base_page_or_content(function):
    def wrapper(*args, **kwargs):
        request = args[0]

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return function(*args, **kwargs)
        return render(request, "base.html")
    return wrapper
