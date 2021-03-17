#! python3
# working with files / paths
import os
import shelve
import shutil


def files_notes():
    '''
    windows 'C:\\dir\\dir\\filename.ext'
    r'C:\dir\dir\filename.ext'
    '\\'.join('C', 'dir', 'dir', 'filename.ext')
    above would not work on linux
    '''
    # below works on both linux and windows
    print(os.path.join('C', 'dir', 'dir', 'filename.ext'))
    print(os.sep) # separator in file paths
    print(os.getcwd())
    # os.chdir('C:\\')
    # print(os.getcwd())
    print(os.path.abspath('point.py'))
    print(os.path.abspath('..\\..')) # absolute path 2 directories up
    print(os.path.isabs('..\\..'))
    print(os.path.relpath('c:\\f1\\f2\\spam.png', 'c:\\f1'))
    print(os.path.dirname('c:\\f1\\f2\\spam.png'))
    print(os.path.basename('c:\\f1\\f2\\spam.png'))
    print(os.path.exists('c:\\f1\\f2\\spam.png'))
    print(os.path.isfile('c:\\f1\\f2\\spam.png'))
    print(os.path.isdir('c:\\f1\\f2\\spam.png'))
    # print(os.path.getsize('c:\\f1\\f2\\spam.png'))
    print(os.listdir(os.getcwd()))


def get_file_sizes(my_folder=os.getcwd()):
    print('Searching in: ' + my_folder)
    for sub_path in os.listdir(my_folder):
        if os.path.isfile(sub_path):
            print(sub_path, os.path.getsize(sub_path))


def shelve_file_creation():
    shelve_file = shelve.open('Data\\sampleshelve')
    shelve_file['dogs'] = ['Yorkshire', 'Poodle', 'Greyhound']
    shelve_file.close()
    shelve_test = shelve.open('Data\\sampleshelve')
    print(shelve_test['dogs'])
    shelve_test.close()


def create_simple_file():
    f = open('Data\\sample.txt', 'w')
    f.write('This is a test file.')
    f.close()
    print('Test file created.')


def copy_file_from_to(source, dest):
    shutil.copy(source, dest)


def copy_folder_from_to(source, dest):
    # recursive copy
    shutil.copytree(source, dest)


def move_folder_from_to(source, dest):
    # same as linux mv command
    # this does move but also rename
    shutil.move(source, dest)


def main():
    print()
    files_notes()
    my_folder = os.path.abspath('..\\')
    get_file_sizes(my_folder)
    get_file_sizes()
    # shelve_file_creation()
    # create_simple_file()
    # copy_file_from_to('Data\\sample.txt', 'Data\\sample_copy.txt')


if __name__ == '__main__':
    main()
