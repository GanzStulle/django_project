from django.shortcuts import render

posts = [
        {
            'author':'Alan Walker',
            'title': 'First Post',
            'content': 'First content',
            'date_posted': 'August 27 2020'
        },
        {
            'author':'John Wick',
            'title': 'Second Post',
            'content': 'Second content',
            'date_posted': 'August 28 2020'
        }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})
