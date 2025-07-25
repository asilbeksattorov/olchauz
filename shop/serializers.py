from rest_framework import serializers
from .models import Category, SubCategory, Product, Attribute, Comment, AttributeKey, AttributeValue


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class AttributeKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeKey
        fields = '__all__'


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    attributes = AttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'subcategory',
            'title',
            'image',
            'description',
            'price',
            'quantity',
            'attributes'
        )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'
