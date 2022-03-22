from django.apps import apps
# from django.conf import settings

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from reviews import models 

# Доступ к моделям через apps.get_model(app_label='review', model_name='User')


User = apps.get_model(app_label='reviews', model_name='User')


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=(
                    'username',
                    'email',
                ),
            ),
        ]

    def validate_username(self, value):
        """Проверяет правильность содержания поля username."""
        if 'me' == value.lower():
            raise serializers.ValidationError(
                f'Имя пользователя не может быть "{value.lower()}".'
            )
        return value

    def create(self, validated_data):
        validated_data.get('username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=(
                    'username',
                    'email',
                ),
            ),
        ]

    def validate_username(self, value):
        if 'me' == value.lower():
            raise serializers.ValidationError(
                f'Имя пользователя не может быть me.'
            )
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = models.Review


class CommentSerializer(serializers.ModelSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанра"""
    class Meta:
        fields = ('name', 'slug')
        model = models.Genre


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории"""
    class Meta:
        fields = ('name', 'slug')
        model = models.Category


class TitleReadOnlySerializer(serializers.ModelSerializer):
    """Сериализатор для тайтлов на чтение"""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = '__all__'
        model = models.Title


class TitleEditSerializer(serializers.ModelSerializer):
    """Сериализатор для тайтлов на запись"""
    category = serializers.SlugRelatedField(queryset=models.Category.objects.all(), slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=models.Genre.objects.all(), slug_field='slug', many=True)

    class Meta:
        fields = '__all__'
        model = models.Title
