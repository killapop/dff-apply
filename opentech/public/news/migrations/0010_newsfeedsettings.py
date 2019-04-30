# Generated by Django 2.0.13 on 2019-04-30 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0009_add_awesome_table_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeedSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(help_text='The title of the main news feed.', max_length=255)),
                ('news_description', models.CharField(help_text='The description of the main news feed.', max_length=255)),
                ('news_per_type_title', models.CharField(help_text='The title of the news feed by type. Use {news_type} to insert the type name.', max_length=255)),
                ('news_per_type_description', models.CharField(help_text='The description of the news feed by type. Use {news_type} to insert the type name.', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
