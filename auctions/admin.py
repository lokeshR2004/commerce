from django.contrib import admin

# Register your models here.
from .models import User, Category, Listing, Comment, Bid


# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Bid)