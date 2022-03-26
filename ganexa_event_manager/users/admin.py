from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from ganexa_event_manager.golf.models import GolfClub
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

    def _add_golf_clubs(self, request, user_id):
        player = self.get_object(request, user_id)
        count = GolfClub.objects.create_golf_clubs(player)
        self.message_user(request, f'Success created {count} clubs')
        url = reverse(
            'admin:users_user_changelist',
            current_app=self.admin_site.name,
        )
        return HttpResponseRedirect(url)

    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
        custom_urls = [
            path('golf-clubs-create/<int:user_id>', self.admin_site.admin_view(self._add_golf_clubs),
                 name='add-golf-clubs')
        ]
        return urls + custom_urls

    def user_actions(self, obj):
        if obj.golf_clubs.count() == 0:
            return format_html(
                '<a class="button" href="{}">Create Clubs</a>&nbsp;',
                reverse('admin:add-golf-clubs', args=[obj.pk]),
                # reverse('admin:account-withdraw', args=[obj.pk]),
            )
        else:
            return ''

    user_actions.short_description = 'User actions'
    user_actions.allow_tags = True
