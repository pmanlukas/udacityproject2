## On my implementation

I have implemented huffman encoding technique here with following steps:

- Calculate the occurences of each characters in a string. 

- Character with highest occurence is encoded with minimum code length ie 1 then next Character as 01 and then 001 and so on.

## On my runtime

Time complexity: O(n log(n)) Space complexity: O(distinct_characters)

- in time complexity we also need to factor in the sorted function with O(m log(m))
