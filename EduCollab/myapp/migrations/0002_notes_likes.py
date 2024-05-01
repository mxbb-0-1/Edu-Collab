
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='likes',
            field=models.ManyToManyField(to='myapp.Signup'),
        ),
    ]
