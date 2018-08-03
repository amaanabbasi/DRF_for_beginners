from django.db import models

class Post(models.Model):

    DJANGO_REST_FRAMEWORK = "DRF"
    TENSOR_FLOW = "TF"
    REACT_JS = "RJ"

    ARTICLE_TYPE_CHOICES = (
        (DJANGO_REST_FRAMEWORK, "Django Rest Framework"),
        (TENSOR_FLOW, "Tensor Flow"),
        (REACT_JS, "React JavaScript"),
    )

    title = models.CharField(max_length=120)
    content = models.TextField()
    article_type = models.CharField('type', blank=True, max_length=3, choices=ARTICLE_TYPE_CHOICES)
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = 'posts'

