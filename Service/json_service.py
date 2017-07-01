# coding=utf-8

class Json_Service():
    @classmethod
    def combination(cls, **kwargs):
        data = {}
        for key in kwargs:
            data[key] = kwargs[key]
        return data
