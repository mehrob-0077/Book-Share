from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bookshare', '0002_trade_message_trade_offered_book_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='one_review_per_trade',
        ),
    ]
