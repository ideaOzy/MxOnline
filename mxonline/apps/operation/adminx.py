# -*- coding: utf-8 -*-

from .models import UserAsk, UserCourse, UserMessage, UserFavorite, CourseComment
import xadmin


class UserAskAdmin:
    list_display = ("name", "mobile", "course_name", "add_time")
    search_fields = ("name", "mobile", "course_name")
    list_filter = ("name", "mobile", "course_name", "add_time")


class UserCourseAdmin:
    list_display = ("user", "course", "add_time")
    search_fields = ("user", "course")
    list_filter = ("user", "course", "add_time")


class UserMessageAdmin:
    list_display = ("user", "message", "add_time", "is_read")
    search_fields = ("user", "message", "is_read")
    list_filter = ("user", "message", "add_time", "is_read")


class UserFavoriteAdmin:
    list_display = ("user", "fav_id", "fav_type", "add_time")
    search_fields = ("user", "fav_id", "fav_type")
    list_filter = ("user", "fav_id", "fav_type", "add_time")


class CourseCommentAdmin:
    list_display = ("user", "course", "comments", "add_time")
    search_fields = ("user", "course", "comments")
    list_filter = ("user", "course", "comments", "add_time")


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)