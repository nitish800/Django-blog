from django.db import models

# Create your models here.

#so i am going to create a blog
# some help from https://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/defining-your-models.html

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_url = models.SlugField(max_length=100, unique=True)
    post_body = models.TextField()
    post_date = models.DateField(db_index=True, auto_now_add=True)
    post_author = models.CharField(max_length=50)
    post_category = models.ForeignKey('Categories')
    
    def __str__(self):
        return self.post_title


class Categories(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True)
    cat_url= models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.cat_name

