
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_notes_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked', to='myapp.Signup'),
        ),
    ]
