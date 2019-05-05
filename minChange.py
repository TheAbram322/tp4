def is_it_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False


maxLen = -1
inputStr = input()
if is_it_palindrome(inputStr):
    print(0)
else:
    for n in range(inputStr.__len__()):
        substr = [inputStr[i: i + n] for i in range(inputStr.__len__() - n + 1)]
        for item in substr:
            if is_it_palindrome(item) and maxLen < item.__len__():
                if item == inputStr[0: item.__len__()] or item == \
                        inputStr[inputStr.__len__() - item.__len__(): inputStr.__len__()]:
                    maxLen = item.__len__()

    print(inputStr.__len__() - maxLen)
