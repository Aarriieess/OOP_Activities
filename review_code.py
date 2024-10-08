import random 
 
list = random.sample(range(0,50),20)

halfList = len(list) // 2
firstHalf = list[:halfList]
secondHalf = list[halfList:]

sumsOfLists = []
for index in range(10):
    sumOfElements = firstHalf[index] + secondHalf[index]
    sumsOfLists.append(sumOfElements)

multipleOfFirstHalf = []
for index in range(len(firstHalf)):
    multipleOfFirstHalf.append(firstHalf[index] * 2) 
    
print(f"Full list: {list}")
print(f"First half: {firstHalf}")
print(f"First half: {secondHalf}")
print(f"Sums of first half and second half: {sumsOfLists}")
print(f"First half multiplied by 2: {multipleOfFirstHalf}")