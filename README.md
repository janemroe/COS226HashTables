# COS226HashTables
For this project, I made two hash tables, one for movie titles and one for quotes.

I started with a basic hash function that multiplied the first character's value by 71 and added the remaining values. I used linear probing to handle collisions.

For the second version, I improved the hash function by multiplying the running value by 71 as it went through each character. This worked a lot better and reduced collisions.

For versions 3 and 4, I reused the bad and good hash functions but switched to linked lists to handle collisions instead of linear probing.

For the last version, I kept the better hash function and linked lists but made the table smaller, from 20,000 to 15,000 spots. I wanted to see how much space I could save without making collisions too much worse.

Overall, improving the hash function made the biggest difference. Making the table smaller also showed me that saving space can mean having more collisions
