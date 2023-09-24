import uuid
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Books_catlog(models.Model):
    BOOK_GENERE = {
        ('FICTION', 'fiction'),
        ('NON-FICTION', 'non-fictinonon'),
        ('LITERATURE', 'literature'),
        ('TRADITIONAL-LITERATURE', 'trafitional'),
        ('OTHER', 'other')
    }
    book_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    genere = models.CharField(max_length=255, choices=BOOK_GENERE, null=False)
    description = models.TextField()
    book_image = models.ImageField(upload_to='booksimg/', null=True, blank=True)
    avialable_free = models.BooleanField(default=True)
    avialable_paid = models.BooleanField(default=False)
    publication_date = models.DateField(auto_now_add=True)
    additional = models.TextField(null=True, blank=True)
    
    
    
    def save(self, *args, **kwargs):
        assigned_to = slugify(self.title)
        
        if Books_catlog.objects.filter(slug=assigned_to).exists():
            assigned_to = assigned_to+str(Books_catlog.objects.all().count())
            
        self.slug = assigned_to
        
        super(Books_catlog, self).save(*args, **kwargs)
