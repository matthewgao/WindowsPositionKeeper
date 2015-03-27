# WindowsPositionKeeper

## Introduce
This tool is used to remember all the visible windows in WINDOW OS, then you can restore the position according to your setting. 
* The index of this tool is windowsName, so if the windowsName has some overlap, you may need to find a unique key word for each windows

## Dependence
The tools is run on Python, so first of all you need to install a Python 2.7(Not 3.x), and a pywin32 lib for python 2.7, you can find it in these links:

1. [Download Python2.7](https://www.python.org/downloads/ "Title")
2. [Download pywin32 for 2.7](http://sourceforge.net/projects/pywin32/files/pywin32/ "Title")

## Usage

1. You need to open up all the windows you want to remember, and place them at the right place.
2. If you haven't set a PATH for python, then run this first `set PATH=%PATH%;C:\Python27`
3. Open a cmd, and run `python.exe main.py -p`, you will see all the windows name.
4. Find out the one or more which you cared about, and take a key word from the windows name.
5. run `python.exe main.py -c [win1] [win2] ...` to create a list, which store the key word for each windows
6. run `python.exe main.py -s` to save all the windows position.
7. Then you can run at any time when you need to restore the windows position with `python.exe main.py -r`

Note: you only have to create and save the windows once, if there is no change, then don't need to update it any more, because we have a local cache has saved them all.

## Note

* You can use "python main.py -c add or del" to add or delete key words

## Troubleshooting

Using WIN+up or down (right or left) to show up the windows which can't find.