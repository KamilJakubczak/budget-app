from django.db import models
from django.conf import settings


# Create your models here
class Category(models.Model):
    """Model for category"""

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


class Tag(models.Model):
    """Model for tags"""
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    parent_tag = models.ForeignKey(
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

    def get_name(self, tag_object, name=None):

        if name is None:
            name = tag_object.name
            if self.has_parent(tag_object):
                return self.get_name(tag_object.parent_tag, name)
            else:
                return name
        elif not self.has_parent(tag_object):
            name = self.create_string(name, tag_object)
            return name
        else:
            name = self.create_string(name, tag_object)
            return self.get_name(tag_object.parent_tag, name)

    def has_parent(self, tag_object):
        if tag_object.parent_tag is None:
            return False
        else:
            return True

    def create_string(self, name, tag_object):
        return tag_object.name + ' - ' + name


class Payment(models.Model):
    """Model for payment method objects"""
    payment = models.CharField(
        max_length=100,
        null=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.payment

class TransactionType(models.Model):
    """Model for transaction types"""

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
    """Model for transaction objects"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    transaction_date = models.DateField(
        null=False,
        blank=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)

    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE)

    payment_target = models.ForeignKey(
        Payment,
        related_name = 'payment_target',
        on_delete=models.CASCADE)

    payment_source = models.ForeignKey(
        Payment,
        related_name = 'payment_source',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    description = models.CharField(
        max_length=500,
        blank=True)


