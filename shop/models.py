from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Kategoriya nomi')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Kategoriya rasmi')

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Kategoriya')
    title = models.CharField(max_length=100, verbose_name='Subkategoriya nomi')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Subkategoriya rasmi')

    class Meta:
        verbose_name = 'Subkategoriya'
        verbose_name_plural = 'Subkategoriyalar'

    def __str__(self):
        return f'{self.category.title} - {self.title}'


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Subkategoriya')
    title = models.CharField(max_length=100, verbose_name='Mahsulot nomi')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Mahsulot rasmi')
    description = models.TextField(default='none', verbose_name='Tavsif')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Narxi')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Miqdori')

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        if self.subcategory:
            if  self.subcategory.category:
                return f'{self.subcategory.category.title} - {self.subcategory.title} - {self.title}'
            return f"{self.subcategory.title} - {self.title}"
        return self.title

class AttributeKey(models.Model):
    key_name = models.CharField(max_length=50, unique=True, verbose_name='Atribut kaliti')

    class Meta:
        verbose_name = 'Atribut kaliti'
        verbose_name_plural = 'Atribut kalitlari'

    def __str__(self):
        return self.key_name


class AttributeValue(models.Model):
    value_name = models.CharField(max_length=255, verbose_name='Atribut qiymati')

    class Meta:
        verbose_name = 'Atribut qiymati'
        verbose_name_plural = 'Atribut qiymatlari'

    def __str__(self):
        return self.value_name


class Attribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes', verbose_name='Mahsulot')
    attribute_key = models.ForeignKey(AttributeKey, on_delete=models.CASCADE, verbose_name='Kalit')
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, verbose_name='Qiymat')

    class Meta:
        verbose_name = 'Atribut'
        verbose_name_plural = 'Atributlar'
        unique_together = ('product', 'attribute_key', 'attribute_value')

    def __str__(self):
        return f'{self.product.title} - {self.attribute_key.key_name} - {self.attribute_value.value_name}'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='Mahsulot')
    name = models.CharField(max_length=100, verbose_name='Ismi')
    email = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Izoh')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'

    def __str__(self):
        return f'{self.product.title} - {self.name}'
