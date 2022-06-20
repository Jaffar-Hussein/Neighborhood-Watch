from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    location = models.CharField(max_length=50, null=False)
    police = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    handyman = models.IntegerField(null=True)
    # occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(
        User, null=False, related_name='neighbourhoods', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        Neighbourhood, related_name="occupants", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.user.username


class Businesses(models.Model):
    name = models.CharField(max_length=60, blank=False)
    user = models.ForeignKey(
        User, related_name="business", on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        Neighbourhood, related_name="neighbour", on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    business_image = CloudinaryField("business_image")
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    @classmethod
    def save_business(cls, business):
        cls.save(business)

    @classmethod
    def delete_business(cls, business_id):
        cls.delete(id=business_id)

    @classmethod
    def find_businesses(cls, business_name):
        business = cls.objects.filter(name=business_name)
        return business

    @classmethod
    def update_business(cls, name, user, neighbourhood, description, email, business_image):
        cls.update(name=name, user=user,
                   neighbourhood=neighbourhood, email=email, business_image=business_image, description=description)


class Posts(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(
        Profile, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField()
    image = CloudinaryField("image")
    neighbourhood = models.ForeignKey(
        Neighbourhood, related_name="neighbour_post", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    
    