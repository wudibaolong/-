#coding:gbk
"""
����Ŀ�꣺ʯͷ����������ʷ����
�������ߣ���ľ���������
"""
import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    if name == "ʯͷ":
        name = 0
        return name
    if name == "ʷ����":
        name = 1
        return name
    if name == "ֽ":
        name = 2
        return name
    if name == "����":
        name = 3
        return name
    if name == "����":
        name = 4
        return name
    else:
        print("Error: No Correct Name")
def number_to_name(number):
    if number==0:
        number="ʯͷ"
        return number
    if number==1:
        number="ʷ����"
        return number
    if number==2:
        number="ֽ"
        return number
    if number==3:
        number="����"
        return number
    if number==4:
        number="����"
        return number

def rpsls(player_choice_number):
    player_choice_number=name_to_number(player_choice_number)
    computer_choice_number=random.randrange(5)
    computer_choice_number=number_to_name(computer_choice_number)
    print("�������ѡ���ǣ�" + str(computer_choice_number))
    if player_choice_number == 0 and computer_choice_number == "ʯͷ":
        print("ƽ��")
    elif player_choice_number == 1 and computer_choice_number == "ʷ����":
        print("ƽ��")
    elif player_choice_number == 2 and computer_choice_number == "ֽ":
        print("ƽ��")
    elif player_choice_number == 3 and computer_choice_number == "����":
        print("ƽ��")
    elif player_choice_number == 4 and computer_choice_number == "����":
        print("ƽ��")
    elif player_choice_number == 4 and computer_choice_number == "ֽ":
        print("��Ӯ��")
    elif player_choice_number == 2 and computer_choice_number == "ʯͷ":
        print("��Ӯ��")
    elif player_choice_number == 0 and computer_choice_number == "����":
        print("��Ӯ��")
    elif player_choice_number == 0 and computer_choice_number == "����":
        print("��Ӯ��")
    elif player_choice_number == 3 and computer_choice_number == "ʷ����":
        print("��Ӯ��")
    elif player_choice_number == 0 and computer_choice_number == "����":
        print("��Ӯ��")
    elif player_choice_number == 4 and computer_choice_number == "����":
        print("��Ӯ��")
    elif player_choice_number == 3 and computer_choice_number == "ֽ":
        print("��Ӯ��")
    else:
        print:("�����Ӯ��")


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
