from django.contrib import admin
from .models import Profile,Neighbourhood,Businesses,Posts
# Register your models here.

admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Businesses)
admin.site.register(Posts)

