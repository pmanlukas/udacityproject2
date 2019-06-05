import os


def find_files(suffix, path, files=[]):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

   temp_path = suffix
   if path:
      temp_path = suffix + '/' + path

   for fi in os.listdir(temp_path):
      temp = temp_path + '/' + fi

      if os.path.isfile(temp) and temp.endswith(".c"):
         files.append(temp)
      elif os.path.isdir(temp):
         files = find_files(temp_path, fi, files)

   return files

# test cases
# add more
print(find_files('.', 'testdir'))
print(find_files('.', ''))
print(find_files('.', 'testdir/subdir3'))
