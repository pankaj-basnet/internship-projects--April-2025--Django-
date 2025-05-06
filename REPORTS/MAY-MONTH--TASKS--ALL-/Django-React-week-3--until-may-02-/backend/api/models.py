from django.db import models
# from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
# from django.db import models
# from common.models import AbstractModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

import uuid


class UserManager(BaseUserManager):

    def _create_user(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, **kwargs):
        kwargs["is_admin"] = False
        return self._create_user(password, **kwargs)

    def create_superuser(self, password, **kwargs):
        kwargs["is_admin"] = True
        return self._create_user(password, **kwargs)



class AbstractModel(models.Model):

    uuid = models.UUIDField(
        _("UUID"),
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
    )

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]



class User(AbstractModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _("Email"),
        max_length=128,
        unique=True,
        db_index=True,
    )
    name = models.CharField(_("Name"), max_length=32, blank=True)
    password = models.CharField(_("Password"), max_length=128)
    is_active = models.BooleanField(
        _("Active"),
        help_text=_("Designates whether this user can access their account."),
        default=True,
    )
    is_admin = models.BooleanField(
        _("Admin"),
        help_text=_("Designates whether the user can log into this admin site."),
        default=False,
    )

    bio = models.TextField(blank=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.name})"

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def get_all_permissions(self, obj=None):
        return []

    class Meta(AbstractModel.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
