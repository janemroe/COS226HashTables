
# Linear probing with a basic hash function
# This function multiplies the first character by 71 and adds the
# remaining character values together. This is a simple approach,
# but it doesn't account for character order and can cause a lot
# of collisions. Linear probing is used to find the next empty
# space when a collision occurs.

import csv
import time

#Linear probing with bad function

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


# Read CSV
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


        # Insert title using linear probing
        startIndex = titleIndex

        while titleTable[titleIndex] != 0:
            titleCollisions += 1
            titleIndex = (titleIndex + 1) % len(titleTable)

            if titleIndex == startIndex:
                print("full")
                break

        if titleTable[titleIndex] == 0:
            titleTable[titleIndex] = row

        titleTime += time.time() - startTime


        # Calculate index based on hash function and insert quote
        startTime = time.time()

        quoteIndex = quoteFunction(quoteNumbers) % len(quoteTable)


        # linear probing
        startIndex = quoteIndex

        while quoteTable[quoteIndex] != 0:
            quoteCollisions += 1
            quoteIndex = (quoteIndex + 1) % len(quoteTable)

            if quoteIndex == startIndex:
                print("full")
                break

        if quoteTable[quoteIndex] == 0:
            quoteTable[quoteIndex] = row

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


#results

print("Linear probling bad function")

print("Title Table:")
print("Collisions:", titleCollisions)
print("Unused spaces:", titleWasted)
print("Construction time:", titleTime, "seconds")

print("Quote Table:")
print("Collisions:", quoteCollisions)
print("Unused spaces:", quoteWasted)
print("Construction time:", quoteTime, "seconds")
