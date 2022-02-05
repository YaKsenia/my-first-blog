from django.conf import settings
from django.db import models
from django.utils import timezone
from mysite.settings import MEDIA_URL
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
from django_resized import ResizedImageField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation





class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=MEDIA_URL)
    audio_file = models.FileField(blank=True)
    article = RichTextField(blank=True, null=True)
    file =  RichTextUploadingField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Murich(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=MEDIA_URL)
    video_file = models.FileField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class HuckYou(models.Model, HitCountMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = RichTextField(blank=True, null=True)
    file =  RichTextUploadingField(blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    label = models.CharField(max_length=20)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    post = models.ForeignKey(HuckYou, default=None, on_delete=models.CASCADE, related_name='images')
    image = ResizedImageField(size=[600, 400], upload_to=get_image_filename, blank=True, null=True)
    #image = models.ImageField(upload_to=get_image_filename,
     #                         verbose_name='Image')





