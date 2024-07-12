# Piscine-Python-Django-
A serie of modules, each module teach a new concept


# Keep your code organized
project/
    app1/
        __init__.py
        models.py
        views.py
        urls.py
    app2/
        __init__.py
        models.py
        views.py
        urls.py
    templates/
        base.html
        app1/
            index.html
            detail.html
        app2/
            index.html

# Follow the DRY principle (Don't repeat your self)
Bad code 😿
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

Good code 😸
def calculate(length, width, operation):
    if operation == 'area':
        return length * width
    elif operation == 'perimeter':
        return 2 * (length + width)