from django.db import models


class Item(models.Model):
    item_no = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.item_no) + ' ' + str(self.item_name)


class ItemImage(models.Model):
    item_image_no = models.BigAutoField(primary_key=True)
    item_no = models.ForeignKey(Item,
                                related_name='related_item',
                                on_delete=models.CASCADE)
    image_url = models.CharField(max_length=64)

    def __str__(self):
        return str(self.item_image_no) + ' ' + str(self.item_no) + ' ' + str(self.image_url)
