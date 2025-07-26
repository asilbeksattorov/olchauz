from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Product, Category, Comment

@receiver([post_save, post_delete], sender=Product)
def clear_product_cache(sender, **kwargs):
    cache.clear()
    print(" Product cache o‘chirildi")

@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, **kwargs):
    cache.clear()
    print(" Category cache o‘chirildi")

@receiver(post_save, sender=Comment)
def log_comment_created(sender, instance, created, **kwargs):
    if created:
        # print(f" Yangi comment: {instance.user.username} → {instance.product.title}")
         print(f"{instance.name} foydalanuvchi {instance.product.title} mahsulotga izoh qoldirdi.")
