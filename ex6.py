# -*- coding:utf-8 -*-
# 定义变量x，把10替换到字符串中%d位置
x = "There are %d types of people." % 10
# 定义变量binary
binary = "binary"
# 定义变量do_not
do_not = "don't"
# 定义变量y，把变量binary，do_not替换到字符串中指定的位置
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# %r与%s替换的值的类型是字符串时，%r会用单引号包含，而%s不会
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
# 定义变量w的值
w = "This is the left side of ..."
# 定义变量e的值
e = "a string with a right side."
# 使用连接符+连接两个字符串
print w + e
