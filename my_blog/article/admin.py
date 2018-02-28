from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','date_time','update_time')

    class Media:
        js = (
            '/static/js/tinymce/js/tinymce/jquery.tinymce.min.js',   # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/jquery.form.js',
            '/static/js/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/js/tinymce/js/tinymce/textarea.js',   # 手动添加文件，用户初始化参数
        )

#    class Media:
#        js = (
#            '/static/js/kindeditor/kindeditor-all.js',
#            '/static/js/kindeditor/lang/zh-CN.js',
#            '/static/js/kindeditor/themes/config.js',
#        )
admin.site.register(Article,ArticleAdmin)

