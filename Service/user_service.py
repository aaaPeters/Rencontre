# coding=utf-8
from User.models import User, Token, UserPersonalInfo
from django.utils import timezone
from Secure.password_secure import Password_Secure
from datetime import datetime, timedelta

class User_Service():
    @classmethod
    def register(cls, userID, password):
        try:
            counter = User.objects.filter(userID=userID).count()
            if counter == 0:
                if User.userID_verification(userID) == False:
                    return 'Inconsistent with the ID rules'
                elif User.password_verification(password) == False:
                    return 'Inconsistent with the Password rules'
                else:
                    token = Token(userID=userID)
                    token.save()
                    personalInfo = UserPersonalInfo(userID=userID)
                    personalInfo.save()
                    new_User = User(userID=userID, password=password, registerTime=datetime.now(), salt='', Token=token, PersonalInfo=personalInfo)
                    #将新建用户存储到数据库，过程中利用加密密码和加密盐更新了token，再存储token到数据库
                    new_User.save()
                    return 'Success', '', token.todict()
            elif counter == 1:
                return 'Failure', 'ID ' + userID + ' is already in use', ''
            else:
                return 'Failure', 'Plural userID exist', ''
        except:
            return 'Failure', 'Register Failure', ''

    @classmethod
    def verification(cls, userID, password):
        try:
            targetUser = User.objects.get(userID=userID)
            if Password_Secure.string_md5(password) != targetUser.password:
                return 'Failure', 'The password is not correct', ''
            else:
                targetUser.msg.update(targetUser.password, targetUser.salt)
                targetUser.msg.save()
                return 'Success', '', targetUser.todict()
        except:
            return 'Failure', 'ID ' + userID + ' is not registered', ''


    @classmethod
    def resetPassword(cls, userID, latestPassword, token):
        try:
            targetUser = User.objects.get(userID=userID)
            if targetUser.msg.token == token:
                if targetUser.password_verification(latestPassword) == False:
                    return 'Failure', 'Inconsistent with the Password rules', ''
                elif targetUser.password == Password_Secure.string_md5(latestPassword):
                    return 'Failure', 'The password has not changed', ''
                else:
                    targetUser.password = latestPassword
                    targetUser.save()
                    return 'Success', '', targetUser.todict()
            else:
                return 'Failure', 'Illegal token', ''
        except:
            return 'Failure', 'ID ' + userID + ' is not registered', ''


    @classmethod
    def resetPersonalInfo(cls, **kwargs):
        try:
            targetUserInfo = UserPersonalInfo.objects.get(userID=kwargs['userID'])
            user_token = Token.objects.get(userID=kwargs['userID']).token
            if user_token == kwargs['token']:
                if targetUserInfo.update(**kwargs):
                    targetUserInfo.save()
                    return 'Success', '', targetUserInfo.todict()
                else:
                    return 'Failure', 'Illegal kwargs', ''
            else:
                return 'Failure', 'Illegal token'
        except UserPersonalInfo.DoesNotExist:
            return 'Failure', 'targetID does not exist', ''


    @classmethod
    def getPersonalInfo(cls, callerID, targetID, token):
        try:
            caller = Token.objects.get(userID=callerID)
            targetUserInfo = UserPersonalInfo.objects.get(userID=targetID)
            caller_token = Token.objects.get(userID=callerID).token
            print token, caller_token
            if caller_token == token:
                return 'Success', '', targetUserInfo.todict()
            else:
                return 'Failure', 'Illegal token', ''
        except UserPersonalInfo.DoesNotExist:
            return 'Failure', 'callerID or targetID does not exist', ''

    @classmethod
    def logout(cls, userID, token):
        try:
            user = User.objects.get(userID=userID)
            user_token = Token.objects.get(userID=userID).token
            if user_token == token:
                user.delete()
                return 'Success', '', ''
            else:
                return 'Failure', 'Illegal token', ''
        except:
            return 'Failure', 'ID ' + userID + ' is not registered', ''
