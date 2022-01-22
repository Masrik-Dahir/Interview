import os


def minimumKeypadClickCount(text):
    # Write your code here
    list1 = [0,0,0]
    list2 = [0,0,0]
    list3 = [0,0,0]
    list4 = [0,0,0]
    list5 = [0,0,0]
    list6 = [0,0,0]
    list7 = [0,0,0]
    list8 = [0,0,0]
    list9 = [0,0,0]

    count = 0
    for i in text:
        # filling the first element in the dial lists
        if list1[0] == i or list1[0] == 0:
            list1[0] = i
            count += 1
        elif list2[0] == i or list2[0] == 0:
            list2[0] = i
            count += 1
        elif list3[0] == i or list3[0] == 0:
            list3[0] = i
            count += 1
        elif list4[0] == i or list4[0] == 0:
            list4[0] = i
            count += 1
        elif list5[0] == i or list5[0] == 0:
            list5[0] = i
            count += 1
        elif list6[0] == i or list6[0] == 0:
            list6[0] = i
            count += 1
        elif list7[0] == i or list7[0] == 0:
            list7[0] = i
            count += 1
        elif list8[0] == i or list8[0] == 0:
            list8[0] = i
            count += 1
        elif list9[0] == i or list9[0] == 0:
            list9[0] = i
            count += 1

        # filling the first element in the dial lists
        elif list1[1] == i or list1[1] == 0:
            list1[1] = i
            count += 2
        elif list2[1] == i or list2[1] == 0:
            list2[1] = i
            count += 2
        elif list3[1] == i or list3[1] == 0:
            list3[1] = i
            count += 2
        elif list4[1] == i or list4[1] == 0:
            list4[1] = i
            count += 2
        elif list5[1] == i or list5[1] == 0:
            list5[1] = i
            count += 2
        elif list6[1] == i or list6[1] == 0:
            list6[1] = i
            count += 2
        elif list7[1] == i or list7[1] == 0:
            list7[1] = i
            count += 2
        elif list8[1] == i or list8[1] == 0:
            list8[1] = i
            count += 2
        elif list9[1] == i or list9[1] == 0:
            list9[1] = i
            count += 2

        # filling the first element in the dial lists
        elif list1[2] == i or list1[2] == 0:
            list1[2] = i
            count += 3
        elif list2[2] == i or list2[2] == 0:
            list2[2] = i
            count += 3
        elif list3[2] == i or list3[2] == 0:
            list3[2] = i
            count += 3
        elif list4[2] == i or list4[2] == 0:
            list4[2] = i
            count += 3
        elif list5[2] == i or list5[2] == 0:
            list5[2] = i
            count += 3
        elif list6[2] == i or list6[2] == 0:
            list6[2] = i
            count += 3
        elif list7[2] == i or list7[2] == 0:
            list7[2] = i
            count += 3
        elif list8[2] == i or list8[2] == 0:
            list8[2] = i
            count += 3
        elif list9[2] == i or list9[2] == 0:
            list9[2] = i
            count += 3
    return count

print(minimumKeypadClickCount("abcdefghi"))