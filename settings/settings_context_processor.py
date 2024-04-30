from .models import Settings
from django.core.cache import cache
# Create your views here.

def get_setting(request):
    setting_data = Settings.objects.last()
    cache.get_or_set("setting_data", setting_data, 100)


    # #check data in cache
    # try:
    #     setting_data = cache.get('settin_data')
    #     print('new data')
    # except Exception:
    #     print('new cache')
    #     setting_data = Settings.objects.last()
    #     cache.set('settin_data' ,setting_data ,100)

    return {'setting_data':setting_data}