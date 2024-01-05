from .models import Settings

def get_setting(request):
    data = Settings.objects.last()
    return {'setting_data':data}