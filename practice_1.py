n = int(input("ile liczb chcesz wpisać? "))
numbers = []
len(numbers)
while len(numbers) <= n-1:
    i = float(input("wpisz liczbę: "))
    numbers.append(i)
print("wprowadzone liczby:", numbers)
print("suma:", (sum(numbers)))
print("średnia", sum(numbers)/len(numbers))
if sum(numbers) > (sum(numbers)/len(numbers)):
    print("Suma jest większa")
elif sum(numbers) < (sum(numbers)/len(numbers)):
    print("Średnia jest większa")
else:
    print("suma jest równa średniej")
#print(len(numbers))
#print(sum(range(0,n+1)))
