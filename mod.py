# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the
#   desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create,
#   modify, and delete the table
# Feel free to rename the models, but don't rename db_table values
# or field names.
from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.BigIntegerField()
    message_id = models.BigIntegerField()
    document_id = models.BigIntegerField()
    date = models.DateTimeField()
    name_link = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    photo = models.BooleanField()
    photo_link = models.CharField(max_length=255, blank=True, null=True)
    public_tg = models.BooleanField(blank=True, null=True)
    date_tg = models.DateTimeField(blank=True, null=True)
    public_site = models.BooleanField(blank=True, null=True)
    date_site = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "books"


class CheckPosts(models.Model):
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.BigIntegerField()
    message_id = models.BigIntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "check_posts"
