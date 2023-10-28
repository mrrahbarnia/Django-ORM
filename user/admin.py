from django.contrib import admin
# from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as UserAuthAdmin
from django.contrib.auth import get_user_model

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False

# # Register your models here.
# class UserAdmin(UserAuthAdmin):

#     def add_view(self, *args, **kwargs):
#         self.inlines = []
#         return super(UserAdmin, self).add_view(*args, **kwargs)

#     def change_view(self, *args, **kwargs):
#         self.inlines = [UserProfileInline]
#         return super(UserAdmin, self).change_view(*args, **kwargs)
    

# admin.site.unregister(get_user_model())
# admin.site.register(get_user_model(), UserAdmin)


# First approach
# class NewUserAdmin(admin.ModelAdmin):
#     fieldsets = (
#         *UserAuthAdmin.fieldsets,
#         (
#             'New Fields',
#             {
#                 'fields': (
#                     'age',
#                     'nickname'
#                 ),
#             },
#         ),
#     )

# admin.site.register(get_user_model(), NewUserAdmin)


# Second approach
fields = list(UserAuthAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'nickname', 'email', 'age')})

UserAuthAdmin.fieldsets = tuple(fields)
admin.site.register(get_user_model(), UserAuthAdmin)