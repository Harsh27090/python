"""
functions:
-create
-read
-update
-delete
"""
from pathlib import Path

def __readFileAndFolder():
    path = Path('')
    items = path.rglob('*')
    for i,item in enumerate(items):
        print(f'{i+1}: {item}')

def createFile():
    __readFileAndFolder()
    try:
        filename = input('Enter file name: ')
        if '.' not in filename:
            filename = filename + '.txt'
        if Path(filename).exists():
            print(f'File {filename} already exists.')
            return
        with open(filename, 'w') as f:
            f.write('File successfully created.\n')
        print(f'{filename} created!')
    except Exception as e:
        print(f"Error occurred: {e}")


def readFile():
    __readFileAndFolder()
    try:
        filename = input('Enter filename:')
        if '.' not in filename:
            filename += '.txt'
        if not Path(filename).exists():
            print('File does not exist!')
            return
        with open(filename) as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"Error occurred: {e}")


def updateFile():
    __readFileAndFolder()
    try:
        filename = input('Enter filename:')
        if '.' not in filename:
            filename += '.txt'
        if not Path(filename).exists():
            print('File does not exist!')
            return
        print('1. Rename file.')
        print('2. Append')
        print('3. Overwrite')
        check = int(input('Enter choice:'))

        if check == 1:
            new_filename = input('Enter new filename:')
            if '.' not in new_filename:
                new_filename = new_filename + '.txt'
            Path(filename).rename(new_filename)

        if check == 2:
            with open(filename, 'a+') as f:
                print('type q or quit to exit')
                data = input()
                while data.lower() != "q" and data.lower() != "quit":
                    f.write(data+'\n')
                    data = input()
            return

        if check == 3:
            with open(filename,'w') as f:
                print('type q or quit to exit')
                data = input()
                while data.lower() != 'q' and data.lower() != 'quit':
                    f.write(data+'\n')
                    data = input()

    except Exception as e:
        print(f"Error occurred: {e}")


def deleteFile():
    __readFileAndFolder()
    try:
        filename = input('Enter filename:')
        if '.' not in filename:
            filename += '.txt'
        if not Path(filename).exists():
            print('File does not exist!')
            return

        ans = input('Do you really want to delete the file? (y/n): ')
        if ans.lower() == 'n':
            print('File not deleted!')
            return
        Path(filename).unlink()
    except Exception as e:
        print(f"Error occurred: {e}")


print('What do you want to do?')
print('1. Create a new file.')
print('2. Read a file.')
print('3. Update a file.')
print('4. Delete a file.')
choice = int(input('Enter your choice:'))


if choice ==1:
    createFile()

elif choice == 2:
    readFile()

elif choice == 3:
    updateFile()

elif choice == 4:
    deleteFile()

else:
    print('Invalid choice.')