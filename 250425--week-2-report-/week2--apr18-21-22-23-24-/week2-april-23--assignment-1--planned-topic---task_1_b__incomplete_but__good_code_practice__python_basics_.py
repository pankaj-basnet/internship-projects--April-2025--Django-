

############################################
# - (1) Write a mini file organizer that moves files by extension.
############################################

### check file extension
### create folder for a file extension if not exits

print("=======   task_1_b    =========")
print("================================")

from pathlib import Path
import os
import shutil

import datetime

filepath2 = 'moveit22.txt'


filepath = 'foldercreation/moveit.txt'
destination = 'foldercreation/destination'
destination = 'foldercreation/destination/'

# for file in Path.iterdir("./")
# for file in Path.iterdir(destination):
#     if file.

source_file_path = Path('foldercreation/moveit33.txt')

destination2 = Path(destination)
print(destination2.name)

generator_of_path_objects = destination2.iterdir()
print(type(generator_of_path_objects))

print(destination2.iterdir())

source = './foldercreation'

source2 = Path(source)
print(source2.name)

generator_of_source_objects = source2.iterdir()



# extension = "txt"
# def get_path_to_destination(type, file_path = 'foldercreation/moveit33.txt'):
# def get_path_to_destination(type, file_path = 'foldercreation/moveit33.txt'):
def move_file_to_destination(type, file_path = 'foldercreation/moveit33.txt'):
    # for extension in extensions:
    type_path = Path(f'{destination}{type}')

    if type_path.exists():
        check = False
        for folder in generator_of_path_objects:
            print("--------")
            print(folder) # print every files and directories in the folder
            print("--------")

            if folder.is_dir():
                # print(folder.name == f"{type}", type(folder.name == "txt"))

                if folder.name == f"{type}":
                    check = True
                    print(check)
                    if os.path.exists(file_path):
                        shutil.move(file_path, f'{destination}/{folder.name}')
                        print(f'successfully moved {type} file to {type} folder ')
                    else:
                        print("moving failed")
                
                print("moving done/undone")

        ### During handling of the above exception, another exception occurred: (when moveit3_path was wrong path name) # error= 



try:
        
    for file_folder in generator_of_source_objects:
        print("===============")
        print(file_folder)
        print("===============")

        ext_type = "default_ext_type"
        # if file_folder.is_file():
        if True:


            # sou = 'foldercreation/moveit33.txt'
            # print(sou)
            # list_of_str = sou.split(".")
            # ext_type = list_of_str[-1]
            # print(ext_type)


            # sou = 'foldercreation/moveit33.txt'
            # print(sou)
            list_of_str = file_folder.name.split(".")
            ext_type = list_of_str[-1]
            print(ext_type)
        else:
            pass



        # moveit3_path = 'foldercreation/moveit33.txt'
        moveit3_path1 = 'foldercreation/moveit33.'

        file_path = 'foldercreation/'
        file_path = f'{file_path}moveit33.txt/'
        print(file_path)

        extension = ["txt", "py", "md"]

        for ext in extension:

            # move_file_to_destination(type= ext,)
            # move_file_to_destination(type= ext_type, file_path=f'foldercreation/{file_folder.name}')
            move_file_to_destination(type= ext, file_path=f'foldercreation/{file_folder.name}')

            # get_path_to_destination(type= ext,)

except Exception as e :
    print(f"error occurred while creating/moving txt: {e}")

# get_path_to_destination()

print("====================================")
print("====================================")

# print("====================================")

# print("====================================")

# print("====================================")

# ｗｈｙ moving failed output
# """
#                 =======   task_1_b    =========
# ================================
# destination
# <class 'generator'>
# <generator object Path.iterdir at 0x0000022D54A612F0>
# --------
# foldercreation\destination\folder222
# --------
# moving done/undone
# --------
# foldercreation\destination\moveit copy.txt        
# --------
# --------
# foldercreation\destination\moveit.txt
# --------
# --------
# foldercreation\destination\moveit22 copy.txt      
# --------
# --------
# foldercreation\destination\txt
# --------
# successfully moved txt file to txt folder
# moving done/undone
# ====================================
#                 """

# print("====================================")

# print("====================================")