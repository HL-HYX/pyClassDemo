#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 练习1
"""
狗的定义:
1.跑
2.叫
3.吃东西
4.卖萌
狗的属性:
1.体重
2.体长
3.年龄
"""

# class Dog:
#     def __init__(self):
#         self.weight = 100
#         self.tall = 12
#
#     def talk(self):
#         print("疯狂卖萌...")
#
#     def eat(self):
#         print("真好吃...汪汪")
#
#     def run(self):
#         print("跑跑跑....")
#
#     def bark(self):
#         print("汪汪汪....")
#
#
# fhc = Dog()
# fhc.bark()
# fhc.run()
# fhc.eat()
# fhc.talk()
# fhc.weight = 10
# fhc.tall = 19
# print(fhc.weight)
# print(id(fhc))

# 练习二
"""
烤地瓜

类的框架:
火
{
1.火的大小
2.什么时候添加柴火
}

地瓜
{
1.地瓜的成熟程度
2.佐料配单
}
"""
# import time
#
#
# class SweetPotato:  # 定义了一个烤地瓜类
#     def __init__(self, weigth, length):
#         self.weigth = weigth
#         self.length = length
#         self.level = 0
#         self.sea = []
#
#     def cookedLevelInfo(self):
#         print("地瓜已经有%d分熟了" % self.level)
#
#
# class Seasoning:  # 定义了一个佐料类
#     def __init__(self, spam):
#         self.spam = spam
#
#     def addSweet(self):
#         self.spam.sea.append("白砂糖")
#         print("加入了甜甜的白砂糖")
#
#     def addSour(self):
#         self.spam.sea.append("白醋")
#         print("加入了一点酸酸的白醋")
#
#     def addHot(self):
#         self.spam.sea.append("辣椒")
#         print("加入了辣辣的辣椒")
#
#     def seasoningMenu(self):  # 佐料菜单
#         print("白醋-------->sour")
#         print("辣椒-------->hot")
#         print("白砂糖-------->sweet")
#
#     def chooseSeasoning(self):
#         while True:
#             temp = input("你想加入什么佐料? ")
#             if temp == "辣椒":
#                 seasoning.addHot()
#             elif temp == "白砂糖":
#                 seasoning.addSweet()
#             elif temp == "白醋":
#                 seasoning.addSour()
#             else:
#                 print("配料完成!")
#                 break
#
#
# class Fire:
#     def __init__(self, fireSize):
#         self.fireSize = fireSize
#
#     def addFire(self):  # 加柴火
#         self.fireSize += 1
#         print("加了点柴火，火变大了!")
#
#     def fireInfo(self):  # 返回当前的火的大小
#         return self.fireSize
#
#     def addFire_1(self):
#         while True:
#             temp = input("你想加柴火吗? Yes/No:")
#             if temp == "Yes":
#                 self.addFire()
#             else:
#                 break
#
#
# redSweet = SweetPotato(500, 23)
# fire = Fire(3)
# seasoning = Seasoning(redSweet)
# i = 0
#
# print("-----------------------")
# print("地瓜的重量是%d克." % redSweet.weigth)
# print("地瓜的长度是%dcm." % redSweet.length)
# print("地瓜的熟练度是%d." % redSweet.level)
# print("-----------------------")
#
# print("生火...")
# print("当前的火量是%d" % fire.fireSize)
# fire.addFire_1()
# print("如今的火量是%d" % fire.fireSize)
# print("火的大小已经控制完成!")
#
# print("开始烤红薯了....")
# while True:
#     while True:
#         time.sleep(5 - fire.fireSize)
#         redSweet.level += 1
#         i += 1
#         if i == 6:
#             break
#     redSweet.cookedLevelInfo()
#     if 5 <= redSweet.level <= 8:
#         print("已经烤熟了，可以加调料了...")
#         break
#     elif redSweet < 5:
#         print("不行，还是生的...")
#     else:
#         print("已经烤焦了...")
#         break
#
# # 加佐料
# seasoning.seasoningMenu()
# seasoning.chooseSeasoning()
# # print(redSweet.sea)
# print("可以开吃了....")

# 练习三
"""
存放家具

模板：

房子

床等一些家具

"""

# class Home:
#     def __init__(self, area):      # 为家初始化
#         self.area = area
#         self.surplus = []
#
#     def __str__(self):             # 打印家的信息
#         msg = "家当前可以使用的面积为:" + str(self.area)
#         return msg
#
#     def addInfo(self, temp):       # 将家具用品填入家里面
#         if self.area > (temp.width * temp.heigth):
#             self.surplus.append(temp)
#             self.area -= (temp.heigth*temp.width)
#         else:
#             print("当前物品的面积大于家可用的面积")
#
#
# class Bed:      # 定义一个床
#     def __init__(self, width, heigth):       # 初始化床
#         self.width = width
#         self.heigth = heigth
#
#     def __str__(self):       # 打印床的信息
#         temp = "床的宽度为" + str(self.width) + "cm"
#         temp += "\n床的长度为" + str(self.heigth) + "cm"
#         return temp
#
#
# home = Home(200)
# bed = Bed(1.8, 2.0)
# bed_1 = Bed(1.8, 2.0)
#
# home.addInfo(bed)
# home.addInfo(bed_1)
#
#
# print(home)
# print(bed)




































































































































































































































































































