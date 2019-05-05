def is_it_palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False


def min_change(input_str):
    max_len = -1
    if is_it_palindrome(input_str):
        return 0
    else:
        for n in range(input_str.__len__()):
            substr = [input_str[i: i + n] for i in range(input_str.__len__() - n + 1)]
            for item in substr:
                if is_it_palindrome(item) and max_len < item.__len__():
                    if item == input_str[0: item.__len__()] or item == \
                            input_str[input_str.__len__() - item.__len__(): input_str.__len__()]:
                        max_len = item.__len__()

    return input_str.__len__() - max_len


