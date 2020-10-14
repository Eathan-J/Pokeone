import LoadData

def Is_Equal_Str(str1, str2):
    str1 = str1.lower() # Unsorted Pokemon's name
    str2 = str2.lower() # Sorted name in dic
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return str2
    else:
        return '0'    # Not included in dic OR Spelling error

def Sort_Word(str1): 
    length = len(str1)
    if length == 3:
        dic = LoadData.dic3
    elif length == 4:
        dic = LoadData.dic4
    elif length == 5:
        dic = LoadData.dic5
    elif length == 6:
        dic = LoadData.dic6
    elif length == 7:
        dic = LoadData.dic7
    elif length == 8:
        dic = LoadData.dic8
    else:
        dic = LoadData.dic9P
    
    for str2 in dic:
        # result = is_equal_chars(str1, str2)
        result = Is_Equal_Str(str1, str2)
        if result != '0':
            break
    return result 
 
print('Input the Unsorted Pokemon\'s Name: ')
Unsorted_Word = input()
Sorted_Word = Sort_Word(Unsorted_Word)
if Sorted_Word == '0':
    print('Not included in the dic or exist spelling mistakes!')
else:
    print(Sorted_Word)

