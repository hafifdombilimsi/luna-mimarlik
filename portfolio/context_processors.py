from .models import SiteSettings

def global_settings(request):
    # Veritabanındaki ilk ayar kaydını çekiyoruz
    settings = SiteSettings.objects.first()
    # Tüm şablonlara 'site_info' adıyla gönderiyoruz
    return {'site_info': settings}