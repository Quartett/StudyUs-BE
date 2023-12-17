from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ("study", "0002_studymember"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studygroup",
            old_name="thumnail",
            new_name="thumbnail",
        ),
    ]
