# from django.contrib import admin
import xadmin
from art.models import Tag,Art
from xadmin import views
# Register your models here.





class BaseSetting(object):
    # 主题修改,给后台界面添加一个主题功能

    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置,修改界面里面的内容
    site_title = '美文后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [Tag, Art]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        Art: "glyphicon glyphicon-book",
        Tag: "fa fa-cloud"
    }  # 设置models的全局图标

    #设置app模块的标题
    apps_label_title={
        'art':'文章管理'
    }
    #设置app模块的图标
    apps_icons={
        'art':'glyphicon glyphicon-book'
    }



class TagAdmin(object):
    list_display=['name','add_time']
    search_fields=['name']

class ArtAdmin(object):
    list_display=['title','author','summary','publish_date']
    search_fields=['title','author']
    style_fields={
        'content':'ueditor'#设置content字段的样式为ueditor
    }

# 注册标题信息
xadmin.site.register(views.CommAdminView, GlobalSettings)

# 注册主题风格
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Art,ArtAdmin)