from django.shortcuts import render

# Create your views here.

def get_book(request):
    books = [
        {
            "id": 1,
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "price": 120,
            "description": "A handbook of agile software craftsmanship"
        },
        {
            "id": 2,
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt",
            "price": 95,
            "description": "Journey to mastery in software development"
        },
        {
            "id": 3,
            "title": "Design Patterns",
            "author": "Erich Gamma",
            "price": 150,
            "description": "Reusable object-oriented design solutions"
        },
        {
            "id": 4,
            "title": "You Don’t Know JS",
            "author": "Kyle Simpson",
            "price": 80,
            "description": "Deep dive into JavaScript core concepts"
        },
        {
            "id": 5,
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "price": 110,
            "description": "Clear, concise Python programming guide"
        }
    ]

    return render(request, 'books.html', {'books': books})