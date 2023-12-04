#1
# field = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# turn = "x"
# win = "*"
# comp = "0"
#
# print(field[1], field[2], field[3])
# print(field[4], field[5], field[6])
# print(field[7], field[8], field[9])
# for i in range(5):
#     while True:
#         choice = int(input("Input: "))
#         if choice in field and choice != 0:
#             field[choice] = turn
#             turn = "0"
#             break
#     print(field[1], field[2], field[3])
#     print(field[4], field[5], field[6])
#     print(field[7], field[8], field[9])
#
#     if field[1] != 1:
#         if field[1] == field[2] and field[1] == field[3]:
#             win = field[1]
#         elif field[1] == field[4] and field[1] == field[7]:
#             win = field[1]
#         elif field[1] == field[5] and field[1] == field[9]:
#             win = field[1]
#
#     if field[2] != 2:
#         if field[2] == field[5] and field[2] == field[8]:
#             win = field[2]
#
#     if field[3] != 3:
#         if field[3] == field[6] and field[3] == field[9]:
#             win = field[3]
#
#     if field[4] != 4:
#         if field[4] == field[4] and field[4] == field[6]:
#             win = field[4]
#
#     if field[7] != 7:
#         if field[7] == field[8] and field[7] == field[9]:
#             win = field[7]
#         elif field[7] == field[5] and field[7] == field[3]:
#             win = field[7]
#             if win != "*":
#                 print(f"winner{win}")
#                 break
#             while True:
#                 if choice in field:
#                     if field[choice] == 1:
#                         field[2] = "0"
#                     elif field[choice] == 2:
#                         field[3] = "0"
#                     elif field[choice] == 3:
#                         field[6] = "0"
#                     elif field[choice] == 4:
#                         field[5] = "0"
#                     elif field[choice] == 5:
#                         field[9] = "0"
#                     elif choice == 6:
#                         field[9] = "0"
#                     elif field[choice] == 7:
#                         field[4] = "0"
#                     elif field[choice] == 8:
#                         field[5] = "0"
#                     elif field[choice] == 9:
#                         field[5] = "0"
#2
# from random import randint
# myLst = [randint(-50, 50) for i in range(15) if i % 2 == 0]
# print(myLst)
# myLst = [randint(-50, 50) for i in range(15) if i % 2 != 0]
# print(myLst)
# myLst = [randint(-50, 50) for i in range(15) if i < 0]
# print(myLst)
# myLst = [randint(-50, 50) for i in range(15) if i > 0]
# print(myLst)