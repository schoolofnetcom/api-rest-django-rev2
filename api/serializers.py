from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Category, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CategorySerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField() #read_only
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id', 'name', 'description', 'user', 'user_id')


class ProductSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField() #read_only
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                       write_only=True, source='categories', many=True)
    #categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'name', 'price', 'categories', 'categories_id')
        #fields = ('id', 'name', 'price', 'categories')

# campos de leitura - serializar
# campos de escrita - deserializar
