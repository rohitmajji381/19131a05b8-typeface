a = int(input())

LCD_char = {'0', '1', '2', '5', '6', '8', '9'}
l = [0, 1, 2, 5, 6, 8, 9]

if a < 7:
    print(l[a])
else:
    c = 7
    n = 9
    while c <= a:
        n += 1
        s = str(n)
        f = True
        for i in s:
            if i not in LCD_char:
                f = False
                break
        if f:
            c += 1
            
    print(n)
