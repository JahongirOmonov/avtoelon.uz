from rest_framework import serializers
from avto.models import Post, Region, District, Account
from option.serializers import PostOptionSerializer

class PostSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(source="json.district")
    title = serializers.StringRelatedField(source="json.title", read_only=True)
    extended_title = serializers.StringRelatedField(
        source="json.extended_title", read_only=True
    )
    photo_count = serializers.IntegerField(source="json.photos_count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "extended_title",
            "photo_count",
            "main_photo",
            "district",
        )


# class DistrictsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = District
#         fields = ('title',)

class RegionDistrictSerializer(serializers.ModelSerializer):
    districts = serializers.StringRelatedField(many=True, read_only=True)
    # districts = DistrictsSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = '__all__'


class PostSerializerRegionSerializer(serializers.ModelSerializer):
    subcategory=serializers.StringRelatedField(source='subcategory.title', read_only=True)
    district=serializers.StringRelatedField(source='district.title', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializerDistrictSerializer(serializers.ModelSerializer):
    subcategory=serializers.StringRelatedField(source='subcategory.title', read_only=True)
    district=serializers.StringRelatedField(source='district.title', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class DistrictPostCountSerializer(serializers.ModelSerializer):
    post_count=serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ('title', 'post_count')

    def get_post_count(self, object):
        return object.posts.count()
    

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"


class DetailSerializer(serializers.ModelSerializer):
    title=serializers.StringRelatedField(source='json.title', read_only=True)
    options=serializers.StringRelatedField(source='json.options')
    
    class Meta:
        model = Post
        fields = ('title', 'price', 'district', 'options')


