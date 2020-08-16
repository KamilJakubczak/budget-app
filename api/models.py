from django.db import models
from django.conf import settings


# Create your models here
class Tag(models.Model):

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    enabled = models.BooleanField(
        default=True,
        blank=False,
        null=False)

    def __str__(self):
        return self.user.username + ' - ' + self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    def __str__(self):
        name = (self.get_name(self))
        return str(name)

    def get_name(self, category_object, name=None):

        if name is None:
            name = category_object.name
            if self.has_parent(category_object):
                return self.get_name(category_object.parent_category, name)
            else:
                return name
        elif not self.has_parent(category_object):
            name = self.create_string(name, category_object)
            return name
        else:
            name = self.create_string(name, category_object)
            return self.get_name(category_object.parent_category, name)

    def has_parent(self, category_object):
        if category_object.parent_category is None:
            return False
        else:
            return True

    def create_string(self, name, category_object):
        return category_object.name + ' - ' + name


class Payment(models.Model):
    payment = models.CharField(
        max_length=100,
        null=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    initial_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2)

    def __str__(self):
        return self.payment


class PaymentInitial(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        related_name='payment_initial'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False)

    class Meta:
        unique_together = ('user', 'payment')


class TransactionType(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    transaction_type = models.CharField(
        max_length=100,
        null=False,
        blank=False)

    def __str__(self):
        return self.transaction_type


class Transaction(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    transaction_date = models.DateField(
        null=False,
        blank=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE)

    payment_target = models.ForeignKey(
        Payment,
        related_name='payment_target',
        on_delete=models.CASCADE)

    payment_source = models.ForeignKey(
        Payment,
        related_name='payment_source',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    description = models.CharField(
        max_length=500,
        blank=True)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False)
