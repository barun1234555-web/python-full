a = [10, 20, 30, 40, 50]
print("Original list:", a)

a.append(60)
print("After adding:", a)

a.insert(2, 25)  
print("After inserting: ", a)

a.remove(40)
print("After removeing:", a)

popped = a.pop(3)
print("After popping (removed", popped, "):", a)


a.sort()
print("After sorting:", a)