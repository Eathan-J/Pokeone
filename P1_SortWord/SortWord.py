import LoadData
#*****************Input Unsorted Word*****************#

def is_equal_chars(str1, str2):
    str1 = str1.lower() # Unsorted Pokemon's name
    str2 = str2.lower() # Sorted name in dic
    cnt = {}
    for c in str1:
        cnt[c] = cnt.get(c, 0) + 1
    for c in str2:
        if c not in cnt:
            return 'Error!'
        cnt[c] -= 1
        if cnt[c] < 0:
            return 'Error!'
    return str2

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
        result = is_equal_chars(str1, str2)
        if result != 'Error!':
            break
    return result 
 
print('Input the Unsorted Pokemon\'s Name: ')
Unsorted_Word = input()
Sorted_Word = Sort_Word(Unsorted_Word)
print(Sorted_Word)

