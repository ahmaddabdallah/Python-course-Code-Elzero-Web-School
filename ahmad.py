# x = 1
# l = []
# total = 0

# while x != 0 :
#     x = int(input("Enter your Number : "))
#     l.append(x)

# for i in l:
#     total += i
# print(f"The sum of {l} = {total}")

x = int(input("Enter your number : "))

for i in range(1 , 11) :
    result = x * i
    print(f"{x} × {i} = {result}")