a = int(input())

def base3(a):
    string = ''
    while a != 0:
        p = a%3
        a = a//3
        string += str(p)
    return string[::-1]

print(base3(a))
