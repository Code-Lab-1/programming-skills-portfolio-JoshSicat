guests = ['miguel', 'josh','luna']

name = guests [0].title()
print(f"{name}, please be my friend.")

name = guests [1].title()
print(f"{name}, please be my friend.")

name = guests [2].title()
print(f"{name}, please be my friend.")

name = guests [1].title()
print(f"/nsorry,{name} i cant be your firend.")

del(guests[1])
guests.insert(1, 'princess')

name = guests [1].title()
print(f"{name}, please be my firend.")