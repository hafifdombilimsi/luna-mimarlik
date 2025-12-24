from .models import Project, Category, Slider, BlogPost, Service
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm 

def home(request):
    # Projeleri al
    projects = Project.objects.all()
    
    # Sliderları al (Sadece aktif olanları getir)
    sliders = Slider.objects.filter(is_active=True)

    services = Service.objects.all()
    
    # İkisini birden gönder
    return render(request, 'portfolio/home.html', {'projects': projects, 'sliders': sliders, 'services': services})

# Yeni ekleyeceğimiz fonksiyon:
def project_detail(request, pk):
    # Veritabanında bu ID'ye (pk) sahip projeyi bul, yoksa 404 hatası ver.
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    if request.method == 'POST':
        # Kullanıcı butona bastıysa formu dolduruyoruz
        form = ContactForm(request.POST)
        if form.is_valid(): # Her şey kurallara uygun mu?
            form.save() # Veritabanına kaydet
            return render(request, 'portfolio/contact.html', {'success': True})
    else:
        # Sayfa ilk açıldığında boş form göster
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})

def category_projects(request, pk):
    # Tıklanan kategoriyi bul
    category = get_object_or_404(Category, pk=pk)
    # Sadece bu kategoriye ait projeleri bul
    projects = Project.objects.filter(category=category)
    return render(request, 'portfolio/category_projects.html', {'category': category, 'projects': projects})

# Tüm yazıları listeleme
def blog_index(request):
    posts = BlogPost.objects.filter(is_active=True)
    return render(request, 'portfolio/blog_index.html', {'posts': posts})

# Tek bir yazıyı okuma
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def kvkk(request):
    return render(request, 'portfolio/kvkk.html')