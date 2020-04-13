#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name==str("ʯͷ"):
            return "0"
    elif name==str("ʷ����"):
	        return "1"
    elif name==str("ֽ"):
		    return "2"
    elif name==str("����"):
	        return "3"
    elif name==str("����"):
	        return "4"
    else:	 
		     print("Error:No Correct Name")
	# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    # ����û���ѡ����ʯͷ/����/��/����/ʷ�����е�����һ�����������Error: No Correct Name����

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
            return str("ʯͷ")
    elif number==1:
		    return str("ʷ����")
    elif number==2:
		    return str("ֽ")
    elif number==3:
		    return str("����")
    elif number==4:
		    return str("����")
    else:	
		    print("Error:No Correct Name")
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    # ����û���ѡ����ʯͷ/����/��/����/ʷ�����е�����һ�����������Error: No Correct Name����

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("--------")  # ���"-------- "���зָ�
    
    print("���ѡ��Ϊ��",player_choice) # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    player_choice_number=name_to_number(player_choice)
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(5) 
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    
    comp_choice=number_to_name(comp_number) # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    
    print("�������ѡ��Ϊ:",comp_choice) # ����Ļ����ʾ�����ѡ����������
    
    result=(comp_number - int(player_choice_number))%5 
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    if result==1 or result==2 :
		   print("�����Ӯ��")
    elif result==3 or result==4 :
		   print("��Ӯ��")
    elif result==0 :
		   print("���ͼ��������һ����")    
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")

choice_name=input()
rpsls(choice_name)


