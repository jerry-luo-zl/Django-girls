'''
===========================================================
This is the part for the defination of the administration
===========================================================
'''

from django.contrib import admin
from import Post

# to make model visible on the admin page, we must register the model
admin.site.register(models.Post)


