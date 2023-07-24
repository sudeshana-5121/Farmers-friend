from django.contrib import admin

# Register your models here.
from .models import LoanSchemeForFarmers
from .models import CropInfo
from .models import extendeduser
from .models import MarketPrices
from .models import WillPlant
from .models import Contact
admin.site.register(LoanSchemeForFarmers)
admin.site.register(CropInfo)
admin.site.register(extendeduser)
admin.site.register(MarketPrices)
admin.site.register(WillPlant)
admin.site.register(Contact)