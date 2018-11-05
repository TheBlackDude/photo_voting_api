from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Image(models.Model):
    CATEGORY_CHOICES = (
        ('people', 'People'),
        ('nature', 'Nature'),
        ('city_life', 'City Life'),
        ('love', 'Love'),
        ('sport', 'Sport'),
        ('family', 'Family')
    )
    owner = models.ForeignKey(User,
                              related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='Images/',
                              default='Images/No-img.jpg', blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=10,
                                choices=CATEGORY_CHOICES, default='nature')
    # In a real application you should use GeoDjango for GeoLocations
    location = models.CharField(max_length=255, blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
