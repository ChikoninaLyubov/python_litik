## 2 Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('X Y Z')
for x in range(2):
     for y in range(2):
        for z in range(2):
             if  (x or y or z == x and y and z):
                print(x, y, z)