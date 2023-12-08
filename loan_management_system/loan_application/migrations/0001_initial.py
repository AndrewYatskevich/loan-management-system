# Generated by Django 4.2.7 on 2023-12-08 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='loan_application.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplicationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('loan_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_application.loanapplication')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan_application.product')),
            ],
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='products',
            field=models.ManyToManyField(related_name='loan_application', through='loan_application.LoanApplicationProduct', to='loan_application.product'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('loan_application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='loan_application.loanapplication')),
            ],
        ),
        migrations.AddConstraint(
            model_name='loanapplicationproduct',
            constraint=models.UniqueConstraint(fields=('loan_application', 'product'), name='unique_loan_application_product'),
        ),
    ]