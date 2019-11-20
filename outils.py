def diviseurs(n):
    "à modifier"
    pass

def est_premier(n):
    if n<2 :
        return False
    if n<4 :
        return True
    if not n%2 :
        return False
    for p in range(3, n, 2):
        if not n%p :
            return False
        if p*p>n :
            return True
