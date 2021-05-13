from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Two(models.Model):
    title = models.CharField(max_length=5)
    writer = models.CharField(max_length=5)
    pub_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Three(models.Model):
    title = models.CharField(max_length=10)
    score = models.FloatField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Four(models.Model):
    title = models.CharField(max_length=10)
    height = models.FloatField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Five(models.Model):
    title = models.CharField(max_length=10)
    weight = models.FloatField()
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


