#coding:utf-8
__author__ = 'xp'

class Question:
    def __init__(self, time, ram, id, context, name, point):
        self.__time = int(time)
        self.__ram = int(ram)
        self.__id = int(id)
        self.__context = context
        self.__name = name
        self.__point = int(point)

    def __init__(self, dict):
        self.__id = dict['id']
        self.__name = dict['name']
        self.__ram = dict['ram']
        self.__point = dict['point']
        self.__context = dict['context']
        self.__time = dict['time']

    def getTime(self):
        return self.__time

    def getRam(self):
        return self.__ram

    def getID(self):
        return self.__id

    def getContext(self):
        return self.__context

    def getName(self):
        return self.__name

    def getPoint(self):
        return self.__point
