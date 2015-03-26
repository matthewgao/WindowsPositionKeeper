#coding=gbk
import win32gui, win32con, win32api  
import time, math, random, sys
import pickle


winList = ["Lynn (Ling) Zhang","金太阳","Chrome"]

def _RecordWindCallback( hwnd, extra ):  
    windows = extra  
    temp=[]
    if win32gui.IsWindowVisible( hwnd ) and win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd):
        temp.append(hex(hwnd))  
        #temp.append(win32gui.GetClassName(hwnd))  
        temp.append(win32gui.GetWindowText(hwnd))
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
                        #placement[1] = 4 
                        #placement = tuple(placement)
                        print placement[0]
                        #print placement[1]
                        #print placement[2]
                        #print placement[3]
                        #win32gui.SetWindowPlacement(hwnd,placement)
                        win32gui.MoveWindow(hwnd,placement[0],placement[1],placement[2]-placement[0],placement[3]-placement[1],True)
                        

def TestEnumWindows():  
    windows = {}
    win32gui.EnumWindows(_RecordWindCallback, windows)
    print "Enumerated a total of  windows with %d classes",(len(windows))
    print '------------------------------'
    #print classes
    #print windows
     
    for item in windows :  
        print  windows[item]
    print '-------------------------------' 
    return windows

def PrintAllWindow():
    print "------------Printing all windows...------------"  
    TestEnumWindows()
    print "------------All done!------------"      

def SaveAllWindows():
    win = TestEnumWindows()
    SaveTuple(win)

def RestoreWindows():
    entry = ParseFile()
    for item in entry :
        print  entry[item]
    win32gui.EnumWindows(_RestoreWindCallback, entry)      

def CreateList():
    return 0

def SaveTuple(entry):
    with open('cache', 'wb') as f:
        pickle.dump(entry, f)
def ParseFile():
    with open('cache', 'rb') as f:
        entry = pickle.load(f)
    return entry

def Usage():
    print "Error: Wrong parameters"
    print " Usage:"
    print "     -p print all the visible windows"
    print "     -s save all the visible windows postion"
    print "     -r restore visible windows postion which in the list"
    print "     -c cteate windows list"

if __name__ == "__main__":

    if sys.argv[1] == "-p":
        PrintAllWindow()
    elif sys.argv[1] == "-s":
        SaveAllWindows()
    elif sys.argv[1] == "-r":
        RestoreWindows()
    elif sys.argv[1] == "-c":
        CreateList()
    else:
        Usage()

    #PrintAllWindow()
    #win = TestEnumWindows()
    #SaveTuple(win)

    
    
    

    

