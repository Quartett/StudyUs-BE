from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_studyususer_options_alter_studyususer_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyususer',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default_profile_image.png', upload_to='profile_images/'),
        ),
    ]
