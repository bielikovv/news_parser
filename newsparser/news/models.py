from django.db import models

class PravdaSite(models.Model):
    time = models.CharField(max_length=20, verbose_name='Time')
    title = models.CharField(max_length=455, verbose_name='Title')
    link = models.CharField(max_length=455, verbose_name='Link')

class NVSite(models.Model):
    time = models.CharField(max_length=20, verbose_name='Time')
    title = models.CharField(max_length=455, verbose_name='Title')
    link = models.CharField(max_length=455, verbose_name='Link')