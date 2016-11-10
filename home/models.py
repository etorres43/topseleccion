from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
	Name = models.CharField(max_length=225,default="Auto")
	Profile_score = models.IntegerField(default=0)
	Post_number = models.IntegerField(default=0)
	User_id = models.ForeignKey(User, on_delete=models.CASCADE)
	profile_img = models.ImageField(blank=False, default="No_img")

	def __str__(self):
		return self.Name

class Tag_list(models.Model):
    Category = models.CharField(max_length=20)
    Tag_postnum = models.IntegerField()

    def __str__(self):
        return self.Category

class Main_post(models.Model):
	Title = models.CharField(max_length=225, default=None)
	Main_img = models.CharField(max_length=225, default=None)
	Post_content = models.TextField(default=None)
	Post_date = models.DateTimeField('date published')
	Post_score = models.IntegerField(default=0)
	Profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE,default='0')
	Tag = models.ManyToManyField(Tag_list,default=None)
	Post_short = models.TextField(default="this is ta text")
	
	def __str__(self):
		return self.Title
	def was_published_recently(self):
		now = timezone.now()

class Comments(models.Model):
	Name = models.CharField(max_length=80, default=None)
	Email = models.CharField(max_length=80, default=None)
	Website = models.CharField(max_length=80, default=None)
	Subscribe = models.IntegerField(default=0)
	body = models.TextField(default=None)
	Post_id = models.ForeignKey(Main_post, on_delete=models.CASCADE,default='0')
	Comment_date = models.DateTimeField('date published',default=None)
	
	def __str__(self):
		return self.Name
	def was_published_recently(self):
		now = timezone.now()
	
class Reply(models.Model):
	Name = models.CharField(max_length=80, default=None)
	Email = models.CharField(max_length=80, default=None)
	Website = models.CharField(max_length=80, default=None)
	Subscribe = models.IntegerField(default=0)
	body = models.TextField(default=None)
	Comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE,default='0')
	Reply_date = models.DateTimeField('date published',default=None)

	def __str__(self):
		return self.Name
	def was_published_recently(self):
		now = timezone.now()


