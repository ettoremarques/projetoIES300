"""projetoies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from client.router import router as client_router
from insurance_companies.router import router as insurance_companies_router
from quote.router import router as quote_router
from services.router import router as services_router
from userprofile.router import router as userprofile_router


urlpatterns = [
    path("", include(client_router.urls)),
    path("", include(insurance_companies_router.urls)),
    path("", include(quote_router.urls)),
    path("", include(services_router.urls)),
    path("", include(userprofile_router.urls)),
]
