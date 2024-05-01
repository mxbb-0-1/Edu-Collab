
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210531_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='disliked', to='myapp.Signup'),
        ),
    ]
