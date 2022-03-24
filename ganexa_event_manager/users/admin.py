from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ganexa_event_manager.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "last_name", 'first_name', "is_superuser", 'user_actions']
    search_fields = ["username", "last_name"]

    def user_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Create Clubs</a>&nbsp;',
            '#'
            #reverse('admin:account-deposit', args=[obj.pk]),
            #reverse('admin:account-withdraw', args=[obj.pk]),
        )
    user_actions.short_description = 'User actions'
    user_actions.allow_tags = True
