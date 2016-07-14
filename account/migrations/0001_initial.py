# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 05:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0001_initial'),
        ('level', '0001_initial'),
        ('configsettings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('register_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Suspended'), (1, 'Active')], default=1, null=True)),
                ('level', models.IntegerField(choices=[(1, 'General Holder'), (2, 'Holder'), (3, 'General Agency'), (4, 'Agency')], default=1)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True)),
                ('wechat', models.CharField(blank=True, max_length=255, null=True)),
                ('qq', models.CharField(blank=True, max_length=255, null=True)),
                ('promo_code', models.CharField(blank=True, max_length=255, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_banking_info', to='bank.Bank')),
                ('commission_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_commission_settings', to='configsettings.CommissionSettings')),
                ('default_member_lv', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_default_level', to='level.Level')),
                ('default_return_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_default_return_settings', to='configsettings.ReturnSettings')),
                ('parent_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account.Agent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_agent',
            },
        ),
        migrations.CreateModel(
            name='AgentApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True, unique=True)),
                ('ip', models.CharField(max_length=100)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Rejected'), (1, 'Accepted')], default=0, null=True)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('confirm_at', models.DateTimeField(auto_now=True, null=True)),
                ('active_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_application', to='account.Agent')),
            ],
            options={
                'db_table': 'account_agent_application',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('wechat', models.CharField(blank=True, max_length=255, null=True)),
                ('qq', models.CharField(blank=True, max_length=255, null=True)),
                ('register_at', models.DateTimeField(auto_now_add=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Suspended'), (1, 'Active'), (2, 'Fund Freezed')], default=1)),
                ('level_lock', models.IntegerField(choices=[(0, 'Locked'), (1, 'Unlocked')], default=1)),
                ('agent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_agent', to='account.Agent')),
                ('bank', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_banking_info', to='bank.Bank')),
                ('level', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_level', to='level.Level')),
                ('return_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_return_settings', to='configsettings.ReturnSettings')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_member',
            },
        ),
        migrations.CreateModel(
            name='MemberApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=100)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Rejected'), (1, 'Accepted'), (2, 'Unhandled')], default=1, null=True)),
                ('confirm_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'account_member_application',
            },
        ),
    ]
