from django.contrib import admin

# Register your models here.
from .models import Sale
from .models import Answer

admin.site.register(Sale)
admin.site.register(Answer)