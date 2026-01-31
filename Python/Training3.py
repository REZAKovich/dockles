def maxsep(n1,n2):

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1

def maxofthree(n1, n2, n3):

    data = [n1, n2, n3]

    return max(data)

def spyear():

    

    return