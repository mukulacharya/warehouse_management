from django.db import models

from .base_models import BaseModel


class Inventory(BaseModel):
    AVAILABLE = 1
    OUT_OF_STOCK = 2
    UNAVAILABLE = 3

    B2C = 1
    HORECA = 2
    KIRANA = 3

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (OUT_OF_STOCK, 'Out Of Stock'),
        (UNAVAILABLE, 'Not Available')
    )

    stock_type_choices = (
        (B2C, 'B2C'),
        (HORECA, 'Horeca'),
        (KIRANA, 'Kirana')
    )

    sku = models.IntegerField(db_index=True)
    entity = models.IntegerField(db_index=True)
    quantity = models.DecimalField(decimal_places=2, default=0, max_digits=13)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=UNAVAILABLE)
    stock_type = models.SmallIntegerField(choices=stock_type_choices, default=B2C)

    class Meta:
        verbose_name_plural = 'Inventory'


class InventoryReservation(BaseModel):
    RESERVED = 1
    UNRESERVED = 2

    status_choices = (
        (RESERVED, 'Reserved'),
        (UNRESERVED, 'Unreserved')
    )

    reference = models.IntegerField(null=True, blank=True, db_index=True)
    sku = models.IntegerField(db_index=True)
    entity = models.IntegerField(db_index=True)
    quantity = models.DecimalField(decimal_places=2, default=0, max_digits=13)
    expiry_date = models.DateTimeField(null=True, blank=True, db_index=True)
    status = models.SmallIntegerField(choices=status_choices)

    class Meta:
        verbose_name_plural = 'Inventory Reservations'


class EntityRelations(BaseModel):
    entity = models.IntegerField(max_length=11)
    parent_entity = models.IntegerField(max_length=11)


class ProductRelations(BaseModel):
    sku = models.IntegerField(max_length=11)
    child_sku = models.IntegerField(max_length=11)
