from django.db import models
from django.urls import reverse


class Books(models.Model):
    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Название"
    )
    author = models.TextField(blank=True, null=True)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.BigIntegerField()
    message_id = models.BigIntegerField()
    document_id = models.BigIntegerField(null=True)
    date = models.DateTimeField(verbose_name="Дата создания")
    name_link = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255, null=True)
    file_size = models.BigIntegerField()
    photo = models.BooleanField()
    photo_link = models.ImageField(max_length=255, blank=True, null=True)
    photo_thumbnail = models.ImageField(max_length=255, blank=True, null=True)
    photo_resize = models.ImageField(max_length=255, blank=True, null=True)
    public_tg = models.BooleanField(blank=True, null=True)
    date_tg = models.DateTimeField(blank=True, null=True)
    public_site = models.BooleanField(blank=True, null=True)
    date_site = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    yadisk = models.TextField(null=True)
    type_file = models.CharField(max_length=6, blank=True, null=True)
    year = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"
        ordering = ["-date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})
