from django.contrib import admin
from .models import Project, Slider, Category, Service, ProjectImage, Transformation

# 1. Galeri Resimleri (Yan yana küçük kutular halinde)
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 # Başlangıçta 1 boş satır göster
    verbose_name = "Galeri Resmi"
    verbose_name_plural = "Galeri Resimleri"

# 2. Değişim Hikayesi / Before-After (Alt alta geniş kutular halinde)
class TransformationInline(admin.StackedInline):
    model = Transformation
    extra = 0 # Başlangıçta boş gösterme, "Ekle" deyince gelsin
    verbose_name = "Değişim Hikayesi (Before/After)"
    verbose_name_plural = "Değişim Hikayeleri"

# 3. Proje Yönetimi (Hepsi Bir Arada)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, TransformationInline] # İkisini de buraya ekledik!
    list_display = ('title', 'category') # is_active hatasını da kaldırdık
    list_filter = ('category',)

# Kayıt İşlemleri
admin.site.register(Project, ProjectAdmin)
admin.site.register(Slider)
admin.site.register(Category)
admin.site.register(Service)
# Transformation'ı ayrıca register etmeye gerek yok, Project'in içinde çıkacak zaten.

from .models import Project, Slider, Category, Service, ProjectImage, Transformation, SiteSettings # SiteSettings eklendi

# ... Diğer admin kodların ...

# Site Ayarlarını Admin'e Ekle
class SiteSettingsAdmin(admin.ModelAdmin):
    # Admin panelinde gereksiz "Ekle" butonu çıkmasın diye bir engel koyabiliriz
    # ama şimdilik basit tutalım. Arkadaşına "Sadece 1 tane oluştur ve onu düzenle" demen yeterli.
    def has_add_permission(self, request):
        # Eğer zaten 1 tane kayıt varsa, yenisini ekletme (Singleton Mantığı)
        if self.model.objects.count() >= 1:
            return False
        return True

admin.site.register(SiteSettings, SiteSettingsAdmin)