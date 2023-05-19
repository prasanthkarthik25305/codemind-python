def unique(number):
    digitset= set()
    for digit in str(number):
        if digit in digitset:
            return "Not Unique Number"
        digitset.add(digit)
    return "Unique Number"
num=input()
res=unique(num)
print(res)
