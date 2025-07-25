from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CategoryViewSet,
    SubCategoryViewSet,
    ProductViewSet,
    AttributeViewSet,
    CommentViewSet

)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('products', ProductViewSet)
router.register('attributes', AttributeViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))

]
