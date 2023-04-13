from django.contrib import admin
from .models import BlogPost,CustomerDetails,Comments
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(CustomerDetails)
admin.site.register(Comments)
