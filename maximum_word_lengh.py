def word(n):
    m=n.split()
    l=max(len(i) for i in m)
    return l

n=input()
k=word(n)
print(k)