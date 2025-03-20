def file_operations():
    original_file = 'file1.txt'
    modified_file = 'file2.txt'
    try:
        file1 = open(original_file,'r')
        contents = file1.read()
        print(f"File1 contents: {contents}")
        file1.close
        file2 = open(modified_file,'w')
        mod_contents = file2.write(f"{contents} \nAdded contents")
        print(f"File1 modified and written to file2")
        file2.close()
    except FileNotFoundError:
        print(f"Error -> {original_file} does not exist.")
    except IOError:
        print(f"Error performing operations in the file.")
file_operations()
