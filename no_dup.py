#coding:gbk
"""
����Ŀ��:ʵ������һ�������б��������ͬ����ֵ����û���ظ�����б�
��������:������
"""

def no_dup(lis):
	lis1=list(set(lis))  #���ü�����Ԫ�ز��ظ�������set()
	return lis1
num=input("����������һ�������б�")
print(no_dup(num))
