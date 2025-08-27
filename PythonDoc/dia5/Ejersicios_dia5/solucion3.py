def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador +1 == len(args):
            return False
        if args[contador] == 0 and args[contador +1]  == 0:
           return  True
        else:
           contador += 1
    return False

print(ceros_vecinos(5,5,4,6,5,0,0))