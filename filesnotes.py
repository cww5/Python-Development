#! python3
# working with files / paths
import os


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
    os.chdir('C:\\')
    print(os.getcwd())


def main():
    print()
    files_notes()


if __name__ == '__main__':
    main()