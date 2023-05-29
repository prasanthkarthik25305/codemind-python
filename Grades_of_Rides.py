h,s,S=map(int,input().split())
if h>50 and s>60 and S>100:
    grade=10
elif h>50 and s>60:
    grade=9
elif s>60 and S>100:
    grade=8
elif h>50 and S>100:
    grade=7
elif h>50 or s>60 or S>100:
    grade=6
else:
    grade=5
print(grade)