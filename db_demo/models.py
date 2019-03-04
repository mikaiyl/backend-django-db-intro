from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User

# Your models go here!


class Category(models.Model):
    title = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self',
                                  blank=True,
                                  null=True, on_delete=models.CASCADE)


class Contributor(models.Model):
    page_id = models.ForeignKey('Page', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)


class Page(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=124)
    body = models.TextField()
    is_published = models.SmallIntegerField()
    is_flagged = models.SmallIntegerField()
    tags = models.ManyToManyField('Tag')


class Permission(models.Model):
    title = models.CharField(max_length=45)


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # avatar = models.ImageField()
    avatar = models.CharField(max_length=45)
    body = models.TextField()


class Role(models.Model):
    title = models.CharField(max_length=45)


class Tag(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=50)
