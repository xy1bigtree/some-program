#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020.4.12
"""

import random



#0 - ʯͷ
#1 - ʷ����
#2 - ֽ
#3 - ����
#4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
           name1=0
    elif name=="ʷ����":
           name1==1
    elif name=="ֽ":
           name1=2
    elif name=="����":
           name1=3
    elif name=="����":
           name1=4
    else:
        print("Error: No Correct Name") 
    return name1
   
   

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
             number1="ʯͷ"
    elif number==1:
		       number1="ʷ����"
    elif number==2:
		       number1="ֽ"
    elif number==3:
		       number1="����"
    elif number==4:
		       number1="����"
    return number1
     

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
 
    """
    print("���ѡ��Ϊ:",player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=str(number_to_name(comp_number))
    print("�������ѡ��Ϊ��%s"%comp_choice)
    if player_choice_number==0:
       if comp_number==4:
          print("��Ӯ�ˣ�")
       if comp_number==3:
          print("��Ӯ�ˣ�")
       elif player_choice_number==comp_number:
          print("��ͼ��������һ����")
       else:
          print("����Ӯ��")
    elif player_choice_number==1:
       if comp_number==4 or 0:
          print("��Ӯ�ˣ�")
       elif player_choice_number==comp_number:
          print("��ͼ��������һ����")
       else:
          print("����Ӯ��")
    elif player_choice_number==2:
       if comp_number==1 or 0:
          print("��Ӯ�ˣ�")
       elif player_choice_number==comp_number:
          print("��ͼ��������һ����")
       else:
          print("����Ӯ��")
    elif player_choice_number==3:
       if comp_number==1 or 2:
          print("��Ӯ�ˣ�")
       elif player_choice_number==comp_number:
          print("��ͼ��������һ����")
       else:
          print("����Ӯ��")
    elif player_choice_number==4:
       if comp_number==2 or 3:
          print("��Ӯ�ˣ�")
       elif player_choice_number==comp_number:
          print("��ͼ��������һ����")
       else:
          print("����Ӯ��")
	
	    
    


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
#print("�������ѡ��Ϊ��",comp_choice)
player_choice=input()
"""player_choice_number=name_to_number(player_choice)
comp_number=random.randrange(0,5)
comp_choice=number_to_name(comp_number)"""
rpsls(player_choice)










