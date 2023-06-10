from datetime import datetime
n=input()
d=datetime.strptime(n,"%H:%M")
print(d.strftime("%I:%M %p"))
