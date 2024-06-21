from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ReinoViewSet, FiloViewSet, ClasseViewSet, OrdemViewSet,
    FamiliaViewSet, GeneroViewSet, EspecieViewSet, DetalhesEspeciesViewSet,
    RegisterView, UserViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'reinos', ReinoViewSet)
router.register(r'filos', FiloViewSet)
router.register(r'classes', ClasseViewSet)
router.register(r'ordens', OrdemViewSet)
router.register(r'familias', FamiliaViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'especies', EspecieViewSet)
router.register(r'detalhes', DetalhesEspeciesViewSet, basename='detalhes_especies')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
