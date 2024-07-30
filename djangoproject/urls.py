from django.contrib import admin
from django.urls import path, include
from djangoapp.views import home, computer_entry, computer_list, computer_edit, computer_delete, settings, computerhistory_list
from djangoapp.views import scan_devices  # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('computer_entry/', computer_entry, name='computer_entry'),
    path('computer_list/', computer_list, name='computer_list'),
    path('computer_list/<int:id>/', computer_edit, name='computer_edit'),
    path('computer_list/<int:id>/delete/', computer_delete, name='computer_delete'),
    path('accounts/', include('registration.backends.default.urls')), 
    path('settings/', settings, name='settings'),
    path('computerhistory_list/', computerhistory_list, name='computerhistory_list'),
    path('scan/', scan_devices, name='scan_devices'),  # Add this line
]
