def longest_len(a):
    max = len(a[0])
    temp = a[0]

    for i in a:
        if(len(i) > max):
            max = len(i)
            temp = i

    print(f"word with longest len = {temp} & lenght = {max}")

a = ["NIR" , "HIR" , "HEER"]
longest_len(a)


