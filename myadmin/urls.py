# 后台管理子路由文件
from django.urls import path,include
from myadmin.views import index
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.index, name='myadmin_index'),
]
