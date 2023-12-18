from django.db import migrations, models

class Migration(migrations.Migration):
    
    dependencies = [
        ('accounts', '0003_alter_studyususer_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyususer',
            name='profile_image',
            field=models.ImageField(default='profile_images/default_profile_image.png', upload_to='profile_images/'),
        ),
    ]
