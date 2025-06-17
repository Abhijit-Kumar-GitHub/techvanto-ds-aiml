"""                                              Interview Questions (Part1)


Problem Statement:
 You work in XYZ Corporation as a Data Analyst. Your corporation has told you to
 work with the structure of the data.
 Tasks To Be Performed:

 1. Create a list named ‘myList’ that has the following elements: 10, 20, 30,
 ‘apple’, True, 8.10:
 a. Now in the ‘myList’, append these values: 30, 40
 b. After that, reverse the elements of the ‘myList’ and store that in
 ‘reversedList’

 2. Create a dictionary with key values as 1, 2, 3 and the values as ‘data’,
 ‘information’ and ‘text’:
 a. After that, eliminate the ‘text’ value from the dictionary
 b. Add ‘features’ in the dictionary
 c. Fetch the ‘data’ element from the dictionary and display it in the output

 3. Create a tuple and add these elements 1, 2, 3, apple, mango in my_tuple.

 4. Create another tuple named numeric_tuple consisting of only integer
 values 10, 20, 30, 40, 50:
 a. Find the minimum value from the numeric_tuple
 b. Concatenate my_tuple with numeric_tuple and store the result in r1
 c. Duplicate the tuple named my_tuple 2 times and store that in ‘newdupli’

 5. Create 2 sets with the names set1 and set2, where set1 contains
 {1,2,3,4,5} and set2 contains {2,3,7,6,1}
 Perform the below operation:
 a. set1 union set2
 b. set1 intersection set2
 c. set1 difference set2
 
 """


#1
myList = [10, 20, 30, 'apple', True, 8.10]
myList.append(30)
myList.append(40)
revList = myList[::-1]

#2
myDict = {1: 'data', 2: 'information', 3: 'text'}
myDict.pop(3)

myDict[3] = 'features'

for key, value in myDict.items():
    if value == 'data':
        print(value)

#3
my_tuple = (1, 2, 3, 'apple', 'mango')

#4
numeric_tuple = (10, 20, 30, 40, 50)
min_value = min(numeric_tuple)
r1 = my_tuple + numeric_tuple
newdupli = my_tuple * 2

#5
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 7, 6, 1}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(f"Union: {union} \n Intersection: {intersection} \n Difference: {difference}")


