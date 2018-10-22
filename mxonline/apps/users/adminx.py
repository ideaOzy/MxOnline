# -*- coding: utf-8 -*-
from .models import EmailVerifyRecord, Banner
import xadmin
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    site_title = "幕学后台管理系统"
    site_footer = "幕学在线网"
    menu_style = "accordion"


# xx后台管理器
class EmailVerifyRecordAdmin:
    list_display = ("id", "code", "email", "send_type", "send_time")
    search_fields = ("id", "code", "email", "send_type",)
    list_filter = ("code", "email", "send_type", "send_time")


class BannerAdmin:
    list_display = ("title", "image", "url", "index", "add_time")
    search_fields = ("title", "image", "url", "index")
    list_filter = ("title", "image", "url", "index", "add_time")


# 将后台管理器与model进行关联
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
