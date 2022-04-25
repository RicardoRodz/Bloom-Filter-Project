# Bloom-Filter-Project
Bloom Filter (Python Implementation)

This program was created for Project #2 of CIIC4025 course at University of Puerto Rico, Mayaguez Campus.

This program implements a Bloom Filter.

Two CSV files are taken as input and a result.csv file if outputted.
The program takes the first file and adds its content to create the Bloom Filter. The second file is checked with the
Bloom Filter and its content is filtered. While the filtering occurs a new file is created and written with the data of
the second file and the product of the filtering.

***To run program through terminal use: python bloom_filter.py db_input.csv(path) db_check.csv(path)***

How does it work?

Here are some references on how the algorithm is implemented and its fucntionality:

https://hur.st/bloomfilter/?n=1000000000&p=0.0000001&m=&k=

https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
