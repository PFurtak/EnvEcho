# from django.db import models
# from datetime import datetime
# from envecho.techs.models import Tech

# class Article(models.Model):
#     article_tech = models.ForeignKey(Tech, on_delete=models.DO_NOTHING)
#     article_id = models.AutoField(primary_key=True)
#     article_date = models.DateTimeField(default=datetime.now, blank=True)
#     article_name = models.CharField(max_length=250)
#     article_type = models.CharField(max_length=250)
#     article_vendor = models.CharField(max_length=250)
#     article_purchased = models.DateTimeField(default=datetime.now, blank=True)
#     article_expire = models.DateTimeField(default=datetime.now, blank=True)
#     article_serial = models.CharField(max_length=250)
#     article_body = models.TextField(blank=True)
#     is_published = models.BooleanField(default=True)
#     def __str__(self):
#         return self.article_name


    
