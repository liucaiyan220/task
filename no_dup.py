#coding:gbk
"""
程序目标:实现输入一个数据列表，输出包含同样数值，但没有重复项的列表
程序作者:刘彩艳
"""

def no_dup(lis):
	lis1=list(set(lis))  #利用集合中元素不重复的特性set()
	return lis1
num=input("请任意输入一个数据列表")
print(no_dup(num))
