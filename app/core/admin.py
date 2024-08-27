from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as translateToCustomerLanguage

class UserAdmin(BaseUserAdmin):
  ordering = ['id']
  list_display = ['email', 'name']# order matters
  #overriding class field - fieldsets - as by default it has some variables which we don't have like - username
  #fieldsets can be a set or a list - it just needs to be iterable
  fieldsets = (
    (
      None, #no title for this section
      {
        'fields':('email','password',)
      }
    ),
    (
      translateToCustomerLanguage('Permissions'),
      {
        'fields':('is_active','is_staff','is_superuser',)
      }
    ),
    (
      translateToCustomerLanguage('Important dates'),
      {
        'fields':('last_login',)
      }
    ),
  )
  readonly_fields = ['last_login'] #cannot modify this field

  add_fieldsets = (
    (
      None,
      {
        'classes':('wide',),#just for decoration purposes
        'fields':('email','password1','password2'),
      }
    ),
  )




admin.site.register(models.User,UserAdmin)
