import zipfile
def get_todos(filepath='todos.txt'):
    """ open the file from the file path and fetch the list of
    todos."""
    with open(filepath) as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath='todos.txt'):
    """ write the list with appended new todo in the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def convert(feet_local, inches_local):
    metres= float(feet_local) * 0.3048 + float(inches_local) * 0.0254
    mts=format(metres, '.2f')
    print(f"{feet_local}feet and {inches_local}inches is {mts}metres")
    return mts

def get_average():
    with open('test/test/test.txt', 'r') as file_local:
         degrees = file_local.readlines()
         degrees = degrees[1:]
         values=[float(i) for i in degrees]
         print(values)
         average= sum(values)/len(values)
    return average

if __name__ == "__main__":
    f=get_average()
    print(f)

def compress(files_local, dest_local, name_local):
    with zipfile.ZipFile(dest_local+'/'+name_local+'.zip','w') as archive:
        for i in files_local:
            archive.write(i)

def get_maximum(degrees):
    # celsius_local = [14, 15.1, 12.3]
    maximum = max(degrees)
    return maximum

def greet(message):
    message=message.capitalize()
    print("hey hey")
    return message


def extract(filepath_local, dest_local, filename_local):
    with zipfile.ZipFile(filepath_local,'r') as archive:
        archive.extractall(dest_local+'/'+filename_local)




# print(__name__)

if __name__ == "__main__":
    print("Hi, I'm here!")

gvh= 87

