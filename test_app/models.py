from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class book_manager(models.Manager):
    def custom(self, work):
        namee =self.get_queryset().filter(name__contains=work)
        authorr=self.get_queryset().filter(author__contains=work)
        Publisherr =self.get_queryset().filter(Publisher__contains=work)

        e = book.objects.none()
        f = e.union(namee, authorr, Publisherr)
        return f


class book(models.Model):
    name = models.CharField(max_length=505, default='نام کتاب')
    author = models.CharField(max_length=505, default='نویسنده')
    Publisher = models.CharField(max_length=50005, default='ناشر')
    description = models.TextField(default='توضیحاتی ندارد')
    image = models.ImageField(default='image/Pottawatomie County State Lake #2 in Manhattan, KS.png')
    file = models.FileField(default=False, null=True, blank=True)

    objects = book_manager()

    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
