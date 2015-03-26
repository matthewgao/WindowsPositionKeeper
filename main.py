#coding=gbk
import win32gui, win32con, win32api  
import time, math, random, sys
import pickle

winList = []

def _RecordWindCallback( hwnd, extra ):  
    windows = extra  
    temp=[]
    if win32gui.IsWindowVisible( hwnd ) and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd):
        temp.append(hex(hwnd))  
        #temp.append(win32gui.GetClassName(hwnd))  
        temp.append(win32gui.GetWindowText(hwnd))
        '''
        For GetWindowPlacement is returned only the position when it goes maxminze or minimize,
        so not fit for our requirement
        '''
        #temp.append(win32gui.GetWindowPlacement(hwnd))
        ##win32gui.SetWindowPlacement(hwnd,placement)
        temp.append(win32gui.GetWindowRect(hwnd))
        windows[hwnd] = temp

def _RestoreWindCallback( hwnd, extra ):  
    entry = extra
   
    if win32gui.IsWindowVisible( hwnd ) and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd):
        for listItem in winList:
            #print "listItem:"+str(listItem)
            if win32gui.GetWindowText(hwnd).find(listItem) != -1:
                for item in entry :
                    if entry[item][1].find(listItem) != -1:
                        placement = list(entry[item][2])
                        if placement[0]<0:
                            placement[0] = 0
                        if placement[1]<0:
                            placement[1] = 0
                        if placement[2]<0:
                            placement[2] = 0
                        if placement[3]<0:
                            placement[3] = 0
                        #placement[1] = 4 
                        #placement = tuple(placement)
                        #print placement[0]
                        #print placement[1]
                        #print placement[2]
                        #print placement[3]
                        #win32gui.SetWindowPlacement(hwnd,placement)
                        print placement
                        '''
                        MoveWindows parameter is X,Y,weight,height
                        '''
                        win32gui.MoveWindow(hwnd,placement[0],placement[1],placement[2]-placement[0],placement[3]-placement[1],True)
                        print "Restore : " + str(win32gui.GetWindowText(hwnd))
                        del entry[item]
                        break

def TestEnumWindows():  
    windows = {}
    win32gui.EnumWindows(_RecordWindCallback, windows)
    print "Enumerated a total of windows with %d classes",(len(windows))
     
    for item in windows :  
        print  windows[item][1]
        print  windows[item][2]
 
    return windows

def PrintAllWindow():
    print "------------Printing all windows------------"  
    TestEnumWindows()
    print "------------All done!------------"      

def SaveAllWindows():
    win = TestEnumWindows()
    SaveTuple(win,'cache')

def RestoreWindows():
    entry = ParseFile('cache')
    if len(entry) == 0:
        print "Cache is NULL, please set it first with main.py -s"
        return 0
    #for item in entry :
    #    print  entry[item]
    win32gui.EnumWindows(_RestoreWindCallback, entry)      

def CreateList(arg):
    if arg[1] != "-c":
        Usage()
        return
    tmplist = []
    offset = 0
    
    if arg[2] == "-add":
        tmplist = ParseFile('windows.list')
        offset = 1

    if arg[2] == "-del":
        tmplist = ParseFile('windows.list')
        offset = 1
        length = len(arg)-2-offset
        dellist = list(arg[2+offset:2+offset+length])
        for ditem in dellist:
            for item in tmplist:
                if item.find(ditem) != -1:
                    tmplist.remove(item)
                    break
        tmplist = RemoveDup(tmplist)
        PrintList(tmplist)
        SaveTuple(tmplist, 'windows.list')
        return

    length = len(arg)-2-offset
    #print arg
    #print length                

    #tmplist = list(arg[2+offset:2+offset+length])
    tmplist.extend(arg[2+offset:2+offset+length])
    tmplist = RemoveDup(tmplist)
    PrintList(tmplist)
    SaveTuple(tmplist, 'windows.list')
    
    return 0

def PrintList(input_list):
    for item in input_list:
        print item


def ShowList():
    winList = ParseFile('windows.list')
    PrintList(winList)

def RemoveDup(seq, idfun=None): # Alex Martelli ******* order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

def SaveTuple(entry, filename):
    with open(filename, 'wb') as f:
        pickle.dump(entry, f)
def ParseFile(filename):
    with open(filename, 'rb') as f:
        entry = pickle.load(f)
    return entry

def Usage():
    print "Error: Wrong Parameters"
    print " Usage:"
    print "     -p print all the visible windows"
    print "     -s save all the visible windows postion"
    print "     -r restore visible windows postion which in the list"
    print "     -c [-add|-del] cteate windows list"
    print "     -l list the windows list"

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "-p":
        PrintAllWindow()
    elif len(sys.argv) > 1 and sys.argv[1] == "-s":
        SaveAllWindows()
    elif len(sys.argv) > 1 and sys.argv[1] == "-r":
        winList = ParseFile('windows.list')
        if len(winList) == 0:
            print "Key Word List is NULL, please set it first with main.py -c [Key Words]"
        else:
            RestoreWindows()
    elif len(sys.argv) > 2 and sys.argv[1] == "-c":
        CreateList(sys.argv)
    elif len(sys.argv) > 1 and sys.argv[1] == "-l":
        ShowList()
    else:
        Usage()

    
    
    

    

