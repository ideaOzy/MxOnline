# -*- coding: utf-8 -*-

from .models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin:
    list_display = ("name", "desc", "add_time")
    search_fields = ("name", "desc")
    list_filter = ("name", "desc", "add_time")


class CourseOrgAdmin:
    list_display = ("name", "desc", "category", "click_nums", "fav_nums",
                    "image", "address", "city", "add_time")
    search_fields = ("name", "desc", "category", "click_nums", "fav_nums",
                     "image", "address", "city", "add_time")
    list_filter = ("name", "desc", "category", "click_nums", "fav_nums",
                   "image", "address", "city", "add_time")


class TeacherAdmin:
    list_display = ("org", "name", "work_years", "work_company",
                    "work_position", "points", "click_nums", "fav_nums", "add_time")
    search_fields = ("org", "name", "work_years", "work_company",
                     "work_position", "points", "click_nums", "fav_nums", "add_time")
    list_filter = ("org", "name", "work_years", "work_company",
                   "work_position", "points", "click_nums", "fav_nums", "add_time")


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
