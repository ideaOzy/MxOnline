# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """登录表单验证"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    """注册表单验证"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetForm(forms.Form):
    """找回密码表单验证"""
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
