from django.db import models

from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=False,blank=False)
    short_desc = models.CharField(max_length=115, null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_post')
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self) -> str:
        return self.title
    
class Notes(models.Model):
    user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=False,blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    is_fijado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self) -> str:
        return self.user.nickname
