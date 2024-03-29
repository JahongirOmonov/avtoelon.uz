from django.db import models
from utils.models import BaseModel
from option.models import PostOption


class Region(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
  


class District(BaseModel):
    title = models.CharField(max_length=256)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )

    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    has_price = models.BooleanField(default=True)
    options = models.ManyToManyField(
        "option.Option",
    )

    def __str__(self):
        return self.title

VP, NC, PT=("VIP", "ZO'R", "A'LO")

class Post(BaseModel):
    choices=[
        (VP,VP),
        (NC,NC),
        (PT,PT),
    ]
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="posts"
    )

    status=models.CharField(max_length=12, choices=choices, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    views = models.IntegerField(default=0, editable=False)
    main_photo = models.ImageField(blank=True, null=True, editable=False)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="posts"
    )
    json = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.info

    def make_json_fields(self):
        data = {
            "title": "",
            "extended_title": "",
            "year": "",
            "model": "",
            "district": "",
            "photos_count": 0,
            "options": [],
        }
        data.update(**PostOption.generate_json_options(self.id))
        data["district"] = self.district.title
        data["photos_count"] = self.photos.count()
        data["title"] = f"{data['model']}"
        data["extended_title"] = f"{data['model']} {data['year']} {self.price}  y.e."
        return data

 
class Photo(BaseModel):
    image = models.ImageField(upload_to="photos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    is_main = models.BooleanField(default=False)

    @classmethod
    def get_main_photo(cls, post_id):
        photo = Photo.objects.filter(post_id=post_id, is_main=True).first()
        print(photo)
        if photo:
            return photo.image
        return None
    
class Account(BaseModel):
    years=[
        ("ninty_eight","1998"),
        ("ninty_nine","1999"),
        ("two_thousand","2000"),
        ("th_one","2001")
    ]
    number=models.CharField(max_length=128)
    title=models.CharField(max_length=128, default="id")
    birt_year=models.CharField(max_length=12, choices=years)
    region=models.ForeignKey(Region, on_delete=models.CASCADE)
    city=models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
