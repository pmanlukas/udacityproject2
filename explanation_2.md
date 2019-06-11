## On my implementation

I have written a recursive function for this question which takes input the suffix, path and the list of required files which are found till now. Each time I find a file ending with .c will be appended to this file.

## On my runtime

Run time complexity: O(depth X Avg. number of directoryin each level)

Space complexity: It will be O(nm) due to the structure of the folders, where n is the number of folders and m the number of sub folders etc (a hierachical file system can be nested on several levels)

