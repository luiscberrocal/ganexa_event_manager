from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
import logging

logger = logging.getLogger(__name__)


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    first_name = forms.CharField(
        label=_("First name"),
        max_length=128,
        widget=forms.TextInput(
            attrs={"placeholder": _("First name")}
        ),
    )
    last_name = forms.CharField(
        label=_("Last name"),
        max_length=128,
        widget=forms.TextInput(
            attrs={"placeholder": _("Last name")}
        ),
    )

    # def signup(self, request, user):
    #     logger.debug(f'Signup method last_name: {self.cleaned_data["last_name"]}')
    #     user.last_name = self.cleaned_data['last_name']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.save()
    #     return super(UserSignupForm, self).signup(request, user)

    # def save(self, request):
    #     user = super(UserSignupForm, self).save(request)
    #     user.last_name = self.cleaned_data['last_name']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.save()
    #     logger.debug(f'>>>> Save method last_name: {self.cleaned_data["last_name"]} id: {user.id}')
    #     logger.debug(f'>>>> Save method username: {user.username} id: {user.id}')
    #     return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
