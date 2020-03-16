from django.db import models


class Common(models.Model):
    name = models.CharField(max_length=150)
    bn_name = models.CharField(max_length=150)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Divisions(Common):
    pass


class Districts(Common):
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)
    lat = models.CharField(max_length=200, null=True)
    lon = models.CharField(max_length=200, null=True)


class Category(Common):
    pass


class Chondokotha(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    districts = models.ForeignKey(Districts, on_delete=models.CASCADE)

    def category_name(self):
        return self.category.name

    def disticts_name(self):
        return self.districts.name

    def division_name(self):
        return self.districts.division.name

    def __str__(self):
        return self.title

# Create your models here.
