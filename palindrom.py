def palindrom(palindrom):
    b = -1
    for i in palindrom:
        if i == palindrom[b]:
            b -= 1
        else:
            return False
    return f'{palindrom} is palindrom'

print(palindrom("racecar"))

