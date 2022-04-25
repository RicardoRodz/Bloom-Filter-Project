"""
This program implements a Bloom Filter.

Two CSV files are taken as input and a result.csv file if outputted.
The program takes the first file and adds its content to create the Bloom Filter. The second file is checked with the
Bloom Filter and its content is filtered. While the filtering occurs a new file is created and written with the data of
the second file and the product of the filtering.

***To run program through terminal use: python bloom_filter.py db_input.csv(path) db_check.csv(path)***

Date: April 22, 2022

Author: Ricardo Y. Rodriguez Gonzalez

Student Number: 802-18-2754

Course: CIIC 4025

Professor: Wilfredo E. Lugo-Beauchamp
"""

# ________________________________________________Cache Penetration___________________________________________________ #

# ----------------------------------------------Importing Modules----------------------------------------------------- #
import sys  # Used methods to pass the files as arguments through the terminal.
import csv  # Used methods for reading and writing files.
import mmh3  # Used method for hashing.
import math  # Used methods for different formulas.
from bitarray import bitarray  # Used bitarray for hash positioning and flags.

# -----------------------------------------------Bloom Filter Class--------------------------------------------------- #
"""
Class for Bloom filter, using the murmur3 hash function module.
"""


class BloomFilter(object):
    def __init__(self, num_items, prob_falsepositive):
        """
        num_items : int - Number of items expected to be stored in bloom filter.
        prob_falsepositive : float - False Positive probability in decimal.
        """
        # Probability (decimals) of possible false items
        self.prob_falsepositive = prob_falsepositive

        # Number of items to store on hash.
        self.num_items = num_items

        # Size of bit array required.
        self.size = self.get_size(num_items, prob_falsepositive)

        # Number of hash functions required.
        self.num_hash = self.get_num_hash(self.size, num_items)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # Sets all bits as 0
        self.bit_array.setall(0)

    def add(self, item):
        """
        item : any - In this case, Item is a string.

        Add an item to the filter.

        It saves the modulo result into a variable. The results variable is then used to
        determine position within the hash. Since adding items is part of building the Bloom Filter, the bit's flag
        is changed to 'True' boolean value meaning that when a check lands on that position it will detect the flag and
        return the values accordingly.
        """
        for seed in range(self.num_hash):
            result = mmh3.hash(item, seed) % self.size
            self.bit_array[result] = True

    def check(self, item):
        """
        item : any - In this case, Item is a string.

        Check for existence of an item in filter.

        This method works similar to the add method. After the Bloom Filter is created, the hash(es) it creates have
        boolean values 'True' or 'False' to determine if the item exists, probably exists or does not exist whatsoever.
        Similar to how the add() method works it checks for a position, and then it verifies if there is an item in that
        specific position by comparing if the flag is True or False.

        return string - If the flag is 'False' it returns the string 'Not in the DB'.
                        Else, it returns a string 'Probably in the DB'.
        """

        for seed in range(self.num_hash):
            result = mmh3.hash(item, seed) % self.size
            if not self.bit_array[result]:
                return 'Not in the DB'
        return 'Probably in the DB'

    def get_size(self, n, p):
        """
        Return the size of bit array(size) required.

        *Formula:
        Size = -(number of items * log(probability of false positive)) / (log(2)^2)
        """
        m = int(-(n * math.log(p)) / (math.log(2) ** 2))
        return m

    def get_num_hash(self, m, n):
        """
        Return the hash functions(num_hash) required:

        *Formula:
        Hash Functions = (Size/Number of Items) * log(2)
        """
        k = int((m / n) * math.log(2))
        return k


# ---------------------------------------------------Runnable--------------------------------------------------------- #
"""
 This section is where the magic happens. Three files are opened. Two are passed as arguments. 
 The first one is used to create the Bloom Filter, as mentioned before. An instance of the Bloom Filter is created. 
 Its parameters are the size of the first file that is passed and a given probability for False Positives. 
 The readline() method is used to read the whole file and saved into a variable for further use of the two files. 
 The first use is to get the length of the first file. Then, an iteration of the variable elements occurs to add each 
 element to the Bloom Filter. Another iteration occurs right after where the second file's data is checked with the 
 Bloom Filter and the product of the check() method is written on the third file tha was initially opened. The thirst 
 file is named result.csv and contains two columns. The first column has the data from the second file and the second 
 column has the filtered result. Each column has a header stating its content. 
"""
with open(sys.argv[1], 'r', newline='') as a, open(sys.argv[2], 'r', newline='') as b, open('./results.csv', 'w',
                                                                                            newline='') as c:
    data = csv.reader(a)
    next(data, None)  # Skips header. 'Email'
    data_save = a.readlines()  # Saves every line of file.
    data2 = csv.reader(b)
    next(data2, None)  # Skips header. 'Email'
    data2_save = b.readlines()  # Saves every line of file.

    n = len(data_save)  # Obtains value of items that are added to create Bloom Filter.
    p = 0.0000001  # False positive probability.

    header = ['Email', 'Result']  # Header for first row of Result CSV File.
    writer = csv.writer(c)  # Created CSV Writer
    writer.writerow(header)  # Writes Email and Result as the first row of the CSV File.

    bf = BloomFilter(n, p)  # Creates an instance of Bloom Filter and passes the number of inputs and probability.

    for item1 in data_save:
        var = item1.rstrip()  # Eliminates /r/n on file lines when iterating over each element of a file.
        bf.add(var)  # Adds items to create Bloom Filter.

    for item2 in data2_save:
        var2 = item2.rstrip()  # Eliminates /r/n on file lines when iterating over each element of a file.
        row = [var2, bf.check(var2)]  # Saves the emails and their filtered result into a list.
        writer.writerow(row)  # Writes each row of the file with the content of the variable 'row'.

a.close()  # Closes first input file, used to create Bloom Filter, after programs finishes.
b.close()  # Closes second input file, used to check items with Bloom Filter, after programs finishes.
c.close()  # Closes result file that is used to write rows of input from second file and their filtered results.
