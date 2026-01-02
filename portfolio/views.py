from django.shortcuts import render, get_object_or_404
from .models import Project, Slider, Category # Service ve Blog modellerini silebilirsin kullanmıyorsan

def home(request):
    # Ana sayfada sadece Slider kaldı (veya statik yazılar)
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'portfolio/home.html', {
        'sliders': sliders,
    })

def portfolio(request):
    # Projeleri artık burada gösteriyoruz
    projects = Project.objects.all()
    categories = Category.objects.all() # Filtreleme yapmak istersen diye
    return render(request, 'portfolio/portfolio.html', {
        'projects': projects,
        'categories': categories
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def kvkk(request):
    return render(request, 'portfolio/kvkk.html')

# Blog fonksiyonlarını (blog_index, blog_detail) silebilirsin.
# category_projects fonksiyonu da artık opsiyonel, portfolyo sayfasında hepsi olacaksa silebilirsin.