# 大堂点餐端子路由文件
from django.urls import path
from web.views import index
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index.index, name='web_index'),
]