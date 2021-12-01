#coding:gbk
"""
程序目标：石头剪刀布蜥蜴史波克
程序作者：土木三班吴振洪
"""
import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    if name == "石头":
        name = 0
        return name
    if name == "史波克":
        name = 1
        return name
    if name == "纸":
        name = 2
        return name
    if name == "蜥蜴":
        name = 3
        return name
    if name == "剪刀":
        name = 4
        return name
    else:
        print("Error: No Correct Name")
def number_to_name(number):
    if number==0:
        number="石头"
        return number
    if number==1:
        number="史波克"
        return number
    if number==2:
        number="纸"
        return number
    if number==3:
        number="蜥蜴"
        return number
    if number==4:
        number="剪刀"
        return number

def rpsls(player_choice_number):
    player_choice_number=name_to_number(player_choice_number)
    computer_choice_number=random.randrange(5)
    computer_choice_number=number_to_name(computer_choice_number)
    print("计算机的选择是：" + str(computer_choice_number))
    if player_choice_number == 0 and computer_choice_number == "石头":
        print("平局")
    elif player_choice_number == 1 and computer_choice_number == "史波克":
        print("平局")
    elif player_choice_number == 2 and computer_choice_number == "纸":
        print("平局")
    elif player_choice_number == 3 and computer_choice_number == "蜥蜴":
        print("平局")
    elif player_choice_number == 4 and computer_choice_number == "剪刀":
        print("平局")
    elif player_choice_number == 4 and computer_choice_number == "纸":
        print("你赢了")
    elif player_choice_number == 2 and computer_choice_number == "石头":
        print("你赢了")
    elif player_choice_number == 0 and computer_choice_number == "剪刀":
        print("你赢了")
    elif player_choice_number == 0 and computer_choice_number == "蜥蜴":
        print("你赢了")
    elif player_choice_number == 3 and computer_choice_number == "史波克":
        print("你赢了")
    elif player_choice_number == 0 and computer_choice_number == "剪刀":
        print("你赢了")
    elif player_choice_number == 4 and computer_choice_number == "蜥蜴":
        print("你赢了")
    elif player_choice_number == 3 and computer_choice_number == "纸":
        print("你赢了")
    else:
        print:("计算机赢了")


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
