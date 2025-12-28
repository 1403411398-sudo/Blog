from django.contrib import admin
from .models import BlogPost

# 注册BlogPost模型到管理员界面
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    # 列表中显示的字段
    list_display = ('title', 'owner', 'date_added')
    # 按日期筛选
    list_filter = ('date_added', 'owner')
    # 搜索功能
    search_fields = ('title', 'text')
    # 日期层级导航
    date_hierarchy = 'date_added'
