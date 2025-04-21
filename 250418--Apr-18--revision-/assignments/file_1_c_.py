print("----------------------------")


# with open('no_file_to_read_.txt', 'r') as wrong_file: # FileNotFoundError: [Errno 2] No such file or directory: 'no_file_to_read_.txt'
with open('no_file_to_read_.txt', 'r') as wrong_file:
    print("with statement will handle closing file in case of error if no file is there to read")
    pass

print("----------------------------")

with open('wrong_file_name.txt', 'w') as wrong_file:
    print("will not throw error if there is no file created before opening in 'write' mode ")
    pass

print("----------------------------")



print("----------------------------")


