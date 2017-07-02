# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime
from django.forms.models import model_to_dict
from Secure.password_secure import Password_Secure
import re, datetime

class UserPersonalInfo(models.Model):
    userID = models.CharField(max_length=11, primary_key=True)
    nickname = models.CharField(max_length=24)
    #avatar = models.ImageField
    profile = models.CharField(max_length=80,default='')
    #0其他，1男性，2女性，默认0
    gender = models.IntegerField(default=0)
    #0未知，1A型，2B型，3AB型，4O型，默认0
    bloodType = models.IntegerField(default=0)
    #默认1990-01-01
    birthday = models.DateTimeField(null=True, blank=True, default=datetime.datetime.strptime("1990-01-01", "%Y-%m-%d"))
    #邮箱地址允许留空
    address = models.CharField(null=True, blank=True, max_length=80, default='')
    email = models.EmailField(null=True, blank=True, default='')
    #每次更新生日自动判断星座和年龄
    constellation = models.CharField(max_length=6, blank=True, null=True, default='')
    age = models.IntegerField(blank=True, null=True, default=0)
    #手机号是否被验证
    isVerificate = models.BooleanField(default=False)

    def __unicode__(self):
        return self.userID

    def update(self, **kwargs):
        try:
            for key in kwargs:
                if hasattr(self, key):
                    if not kwargs[key] == '':
                        value = kwargs[key]
                        if key == 'nickname':
                            self.nickname = value
                        elif key == 'profile':
                            self.profile = value
                        elif key == 'gender':
                            self.gender = value
                        elif key == 'bloodType':
                            self.bloodType = value
                        elif key == 'birthday':
                            self.birthday = datetime.datetime.strptime(value, "%Y-%m-%d")
                        elif key == 'address':
                            self.address = value
                        elif key == 'email':
                            self.email = value
            return True
        except:
            return False

    def constellation_value(self, month, day):
        switch_constellation = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
        timeSeparator = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
        return switch_constellation[len(filter(lambda birth: birth <= (month, day), timeSeparator)) % 12]

    def todict(self):
        switch_gender = ('其他', '男性', '女性')
        switch_bloodType = ('未知', 'A型', 'B型', 'AB型', 'O型')
        dict = model_to_dict(self)
        dict['birthday'] = self.birthday.strftime('%Y-%m-%d')
        dict['gender'] = switch_gender[self.gender]
        dict['bloodType'] = switch_bloodType[self.bloodType]
        # timedelta = (datetime.datetime.now() - self.birthday).days
        # dict['age'] = timedelta/365
        dict['age'] = datetime.datetime.now().year - self.birthday.year
        dict['constellation'] = self.constellation_value(self.birthday.month, self.birthday.day)
        return dict


class Token(models.Model):
    userID = models.CharField(max_length=11, primary_key=True)
    token = models.CharField(max_length=32)
    deadLine = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.userID

    def todict(self):
        dict = {}
        dict['userID'] = self.userID
        #时区修正
        dict['deadLine'] = self.deadLine.strftime('%Y-%m-%d %H:%M:%S')
        dict['token'] = self.token
        return dict

    '''token的计算方式是由本地时间+密码MD5密文+32位加密盐进行MD5计算'''
    def update(self, password, salt):
        current_tz = timezone.get_current_timezone()
        self.deadLine = current_tz.normalize(timezone.now()) + timezone.timedelta(7)
        self.token = Password_Secure.string_md5(str(timezone.now()) + password + salt)


class User(models.Model):
    userID = models.CharField(max_length=11, primary_key=True)
    #使用md5加密，密码和加密盐都存储32长度的字节
    password = models.CharField(max_length=32)
    salt = models.CharField(max_length=32, blank=True)
    registerTime = models.DateTimeField(null=True, blank=True)
    Token = models.OneToOneField(Token)
    PersonalInfo = models.OneToOneField(UserPersonalInfo)

    def __unicode__(self):
        return self.userID

    '''保存操作只在创建账户和更改密码的情况下出现，在此类操作中需要更新加密盐、生存期以及token'''
    def save(self, *args, **kwargs):
        #如果密码没有密文存储，将密码进行md5加密存储
        if len(self.password) != 32:
            self.password = Password_Secure.string_md5(self.password)
        #更新加密盐和msg，调用Token更新接口，提供密码密文和当前的加密盐
        self.salt = Password_Secure.create_salt()
        self.Token.update(self.password, self.salt)
        self.Token.save()
        super(User, self).save(*args, **kwargs)

    '''检查userID命名规则，返回操作成功的真假'''
    @classmethod
    def userID_verification(cls, value):
        userID_template = '1[34578]\d{9}$'#正则判断手机号码
        if re.match(userID_template, value):
            return True
        else:
            return False

    '''检查password命名规则，返回操作成功的真假'''
    @classmethod
    def password_verification(cls, value):
        password_template = '[\w?!*]{6,18}$'#正则判断6-18位的数字和字母集，特殊符号只允许？！*
        if re.match(password_template, value):
            return True
        else:
            return False
