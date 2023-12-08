from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LoanApplication(models.Model):
    applicant = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
    )
    products = models.ManyToManyField(
        Product,
        through="LoanApplicationProduct",
        related_name="loan_application",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"LoanApplication(applicant={self.applicant},"
            f" product={self.products})"
        )


class Contract(models.Model):
    loan_application = models.OneToOneField(
        LoanApplication, on_delete=models.CASCADE, related_name="contract"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract(loan_application={self.loan_application})"


class LoanApplicationProduct(models.Model):
    loan_application = models.ForeignKey(
        LoanApplication, on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("loan_application", "product"),
                name="unique_loan_application_product",
            )
        ]
