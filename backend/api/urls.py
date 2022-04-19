from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),
    path('account/', include('account.urls')),
    path('ledger/', include('ledger.urls'))
]