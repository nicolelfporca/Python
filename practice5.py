i = 1
j = 0

def counter():
    global j
    j += 1

def count():
    counter()
    print(i + j)

count() # 1+1
count() # 1+2
count() # 1+3
count() # 1+4
count() # 1+5