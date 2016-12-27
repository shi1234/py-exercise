# -*- coding:utf-8 -*-
# 赋予变量名为车的值为100
cars = 100
# 赋予变量名为车空间的值为4.0
space_in_a_car = 4.0
# 赋予变量名为司机的值为30
drivers = 30
# 赋予变量名为乘客总数的值为90
passengers = 90
# 赋予变量名为不能驾驶的车值为变量车减去变量司机数
cars_not_driven = cars - drivers
# 赋予变量名为驾驶员的值等于变量名为司机的值
cars_driven = drivers
# 赋予变量名为驾驶承载能力的值等于变量名为驾驶员与变量名为车空间的乘积
carpool_capacity = cars_driven * space_in_a_car
# 赋予变量名为每辆车平均乘客数等于变量为乘客总数除于变量为驾驶员的值
average_passengers_per_car = passengers / cars_driven

# 打印 “这里可获得100辆车”
print "There are", cars, "cars available."
# 打印 “这里只有30个司机”
print "There are only", drivers, "drivers available."
# 打印 “今天可能有70辆车是空的”
print "There will be", cars_not_driven, "empty cars today."
# 打印 “我们今天能承载120个人”
print "We can transport", carpool_capacity, "people today."
# 打印 “今天我们有90个乘客可以拼车”
print "We have", passengers, "to carpool today."
# 打印 “我们需要安排三个人到每辆车上”
print "We need to put about", average_passengers_per_car, "in each car."
