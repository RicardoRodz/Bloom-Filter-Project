# Bloom-Filter-Project
Bloom Filter (Python Implementation)

This program was created for Project #2 of CIIC4025 course at University of Puerto Rico, Mayaguez Campus.

For this project, a Bloom Filter had to be implemented. The implementation consists on creating a class with the variables and methos to calculate the proper values of hash functions to create. The program takes a two files, passed as arguments, through the terminal. The first file is opened and its data is used as input to create the Bloom Filter with a given probability of 0.0000001 for False Posisitves. The program will then take the data of the second file and check it with the first file to determine if each element is 'Probably in DB' or 'Not in the DB'. A results.csv file is created with the content of the second file, and the resulting string produced by the filtering.

***To run program through terminal use: python bloom_filter.py db_input.csv(path) db_check.csv(path)***

How does it work?

Here are some references on how the algorithm is implemented and its fucntionality:

https://hur.st/bloomfilter/?n=1000000000&p=0.0000001&m=&k=

https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
