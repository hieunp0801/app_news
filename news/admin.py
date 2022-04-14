from django.contrib import admin
from news.models import *
# Register your models here.
myModels = [Post,Category,Tag]
admin.site.register(myModels)