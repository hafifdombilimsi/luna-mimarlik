from django.db import models

# Kategori Tablosu (Örn: Villa, Ofis, Konut)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    show_in_menu = models.BooleanField(default=False, verbose_name="Menüde Gösterilsin mi?")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

# Proje Tablosu (Örn: Göktürk Villa Projesi)
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    description = models.TextField(verbose_name="Proje Açıklaması")
    # Kategori silinirse projeler de silinsin mi? CASCADE bunu sağlar.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")
    # Resimler nereye yüklenecek?
    image = models.ImageField(upload_to='projects/', verbose_name="Proje Görseli")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

# İletişim Formu Modeli
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    message = models.TextField(verbose_name="Mesajınız")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")

    def __str__(self):
        return self.name + " - " + self.email
    
    class Meta:
        verbose_name = "Gelen Mesaj"
        verbose_name_plural = "Gelen Mesajlar"

# Slider (Manşet) Modeli
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="Slogan (Başlık)")
    subtitle = models.CharField(max_length=200, verbose_name="Alt Başlık", blank=True, null=True)
    image = models.ImageField(upload_to='sliders/', verbose_name="Slider Görseli")
    order = models.IntegerField(default=0, verbose_name="Sıralama (Küçükten büyüğe)")
    is_active = models.BooleanField(default=True, verbose_name="Yayında mı?")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider Yönetimi"
        ordering = ['order'] # Veritabanından çekerken otomatik sıraya dizer

# Blog Yazıları Modeli
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Yazı Başlığı")
    content = models.TextField(verbose_name="Yazı İçeriği")
    image = models.ImageField(upload_to='blog/', verbose_name="Kapak Görseli")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yayınlanma Tarihi")
    is_active = models.BooleanField(default=True, verbose_name="Yayında mı?")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog Yazısı"
        verbose_name_plural = "Blog Yönetimi"
        ordering = ['-created_at'] # En yeni yazı en üstte görünsün diye (-) işareti koyduk

# Öncesi / Sonrası Modeli
class Transformation(models.Model):
    # Hangi projeye ait olduğu:
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='transformations')
    title = models.CharField(max_length=100, verbose_name="Oda Adı (Örn: Mutfak)")
    image_before = models.ImageField(upload_to='transformations/', verbose_name="Öncesi (Eski Hali)")
    image_after = models.ImageField(upload_to='transformations/', verbose_name="Sonrası (Yeni Hali)")

    def __str__(self):
        return f"{self.project.title} - {self.title}"
    
    # Hizmetler Modeli
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Hizmet Başlığı")
    description = models.TextField(verbose_name="Kısa Açıklama")
    # Kullanıcı kendi ikonunu/resmini yüklesin
    icon = models.ImageField(upload_to='services/', verbose_name="İkon (Küçük Resim)")
    order = models.IntegerField(default=0, verbose_name="Sıralama")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"
        ordering = ['order']

# Mevcut Project modelin duruyor, altına bunu ekle:

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery/', verbose_name="Detay Resmi")
    
    def __str__(self):
        return f"{self.project.title} - Resim"
    
# SİTE AYARLARI MODELİ (İletişim & Hakkımızda)
class SiteSettings(models.Model):
    # İletişim Bilgileri
    phone = models.CharField(max_length=20, verbose_name="Telefon Numarası")
    email = models.EmailField(verbose_name="E-posta Adresi")
    address = models.TextField(verbose_name="Adres")
    map_link = models.TextField(verbose_name="Google Maps Embed Linki (iframe içindeki src)", blank=True, null=True)
    
    # Sosyal Medya
    instagram = models.URLField(verbose_name="Instagram Linki", blank=True, null=True)
    linkedin = models.URLField(verbose_name="LinkedIn Linki", blank=True, null=True)
    
    # Hakkımızda Sayfası Bilgileri
    about_title = models.CharField(max_length=200, verbose_name="Hakkımızda Başlık", default="Biz Kimiz?")
    about_description = models.TextField(verbose_name="Hakkımızda Metni")
    about_image = models.ImageField(upload_to='site/', verbose_name="Hakkımızda Görseli", blank=True, null=True)

    class Meta:
        verbose_name = "Site Ayarları"
        verbose_name_plural = "Site Ayarları"

    def __str__(self):
        return "Site Genel Ayarları (Lütfen sadece 1 adet oluşturun)"