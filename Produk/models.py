from django.db import models

# Create your models here.
class Category(models.Model):
    nama_kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kategori

class Status(models.Model):
    nama_status = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_status


class Product(models.Model):
    nama_produk = models.CharField(max_length=50)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


    def __str__(self):
        return self.nama_produk
    
