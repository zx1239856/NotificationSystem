# Generated by Django 2.1.7 on 2019-09-08 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=254, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(db_index=True, max_length=64)),
                ('token_set_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DBSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(db_index=True, max_length=255, unique=True)),
                ('system_title', models.CharField(max_length=255)),
                ('set_time', models.DateTimeField(auto_now_add=True)),
                ('other_settings', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=100)),
                ('db_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.DBSettings')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=1000)),
                ('ip', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('admin_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.AdminUser')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('content', models.TextField()),
                ('attachment_arr', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('notification_type', models.PositiveSmallIntegerField(default=0)),
                ('db_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.DBSettings')),
                ('visible_group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.Notification')),
            ],
        ),
        migrations.CreateModel(
            name='SessionToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(db_index=True, max_length=64)),
                ('set_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('db_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.DBSettings')),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dbapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('varname', models.CharField(db_index=True, max_length=255, unique=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='sessiontoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dbapp.User'),
        ),
        migrations.AddField(
            model_name='notificationstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.User'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dbapp.User'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'db_settings')},
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('groupname', 'db_settings')},
        ),
    ]
