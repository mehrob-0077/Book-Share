from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title","owner","desc","author","status","category","city","location","is_free"]


class TradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ["book","getter","status","start_data","finish_data"]


class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ['id', 'trade', 'author', 'user', 'rating', 'comment']
        read_only_fields = ['author', 'user']

    def validate(self, data):
        trade = data['trade']
        author = self.context['request'].user

        if trade.status != 'ACCEPTED' or author.id not in [trade.getter_id, trade.book.owner_id]:
            raise serializers.ValidationError('Only participants of an accepted trade can leave a review.')
        return data

    def create(self, validated_data):
        trade = validated_data['trade']
        author = self.context['request'].user
        user = trade.book.owner if author == trade.getter else trade.getter
        return Review.objects.create(author=author, user=user, **validated_data)


