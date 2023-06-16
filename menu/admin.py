from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from menu.models import (
    UserAccount,
    Recipe,
    TypeOfDish,
    Game,
    TypeUser
)


@admin.register(UserAccount)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("type_user",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("type_user",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "type_user",
                    )
                },
            ),
        )
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.register(TypeOfDish)
admin.site.register(Game)
admin.site.register(TypeUser)
