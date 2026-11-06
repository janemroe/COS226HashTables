
import csv
import time

#Linked list with basic hash function
# I kept the original hash function but changed from linear probing
# to linked lists. Instead of looking for the next empty spot when
# there's a collision, the records are linked together at the same
# index. 


class LinkedList:
    def __init__(self, row):
        self.row = row #store movie record
        self.next = None #link to next record


def titleFunction(numbers): #create hash function for movie titles
    if len(numbers) == 0:
        return 0

    hashValue = numbers[0] * 71 #multiply first value by 71

    for number in numbers[1:]: #add remaining character values
        hashValue += number

    return hashValue


def quoteFunction(numbers): #create hash function for movie quotes
    if len(numbers) == 0:
        return 0

    hashValue = numbers[0] * 71

    for number in numbers[1:]:
        hashValue += number

    return hashValue


# Create hash tables
titleTable = [0] * 20000 #20000 spots
quoteTable = [0] * 20000

titleCollisions = 0 #set collisions
quoteCollisions = 0

titleTime = 0
quoteTime = 0



with open('MOCK_DATA.csv', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row['movie_title']
        quote = row['quote']

        # Convert characters to numbers
        titleNumbers = []
        quoteNumbers = []

        for character in title:
            titleNumbers.append(ord(character))

        for character in quote:
            quoteNumbers.append(ord(character))


        # Calculate index based on hash function and insert title
        startTime = time.time()

        titleIndex = titleFunction(titleNumbers) % len(titleTable)

        # Insert title using linked-list chaining
        if titleTable[titleIndex] == 0:
            titleTable[titleIndex] = LinkedList(row)
        else:
            current = titleTable[titleIndex]

            while current.next != None:
                titleCollisions += 1
                current = current.next

            titleCollisions += 1
            current.next = LinkedList(row)

        titleTime += time.time() - startTime

# Calculate index based on hash function and insert quote
        startTime = time.time()

        quoteIndex = quoteFunction(quoteNumbers) % len(quoteTable)

        # Insert quote using linked list
        if quoteTable[quoteIndex] == 0:
            quoteTable[quoteIndex] = LinkedList(row)
        else:
            current = quoteTable[quoteIndex]

            while current.next != None:
                quoteCollisions += 1 #count each record passed
                current = current.next

            quoteCollisions += 1 #count last record
            current.next = LinkedList(row)

        quoteTime += time.time() - startTime


# Count unused spaces
titleWasted = 0
quoteWasted = 0

for i in titleTable:
    if i == 0:
        titleWasted += 1

for i in quoteTable:
    if i == 0:
        quoteWasted += 1


# Results
print("linked list bad function")

print("Title Table:")
print("Collisions:", titleCollisions)
print("Unused spaces:", titleWasted)
print("Construction time:", titleTime, "seconds")

print("Quote Table:")
print("Collisions:", quoteCollisions)
print("Unused spaces:", quoteWasted)
print("Construction time:", quoteTime, "seconds")
