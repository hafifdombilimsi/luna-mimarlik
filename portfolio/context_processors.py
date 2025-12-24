from .models import Category

def menu_categories(request):
    # Veritabanından sadece 'show_in_menu' kutusu işaretli olanları çek
    categories = Category.objects.filter(show_in_menu=True)
    return {'menu_categories': categories}