import win32gui, win32con, win32api  
import time, math, random  
    
def _MyCallback( hwnd, extra ):  
    windows = extra  
    temp=[]
    pos = (500, 500, 500, 500,500)
    placement = list((0, 1, (-1, -1), (-1, -1), (0, 0, 500, 500)))
    '''
    9 means restore.
    '''
    placement[1] = 9 
    placement = tuple(placement)
    if win32gui.IsWindowVisible( hwnd ):
        temp.append(hex(hwnd))  
        temp.append(win32gui.GetClassName(hwnd))  
        temp.append(win32gui.GetWindowText(hwnd))
        ##win32gui.SetWindowPlacement(hwnd,placement)
        windows[hwnd] = temp
    
def TestEnumWindows():  
    windows = {}  
    win32gui.EnumWindows(_MyCallback, windows)  
    print "Enumerated a total of  windows with %d classes" ,(len(windows))  
    print '------------------------------'  
    #print classes
    print windows
    print '-------------------------------'  
    for item in windows :  
        print  windows[item]  
  
print "Enumerating all windows..."  
h=win32gui.FindWindow(None,'\xba\xec\xce\xe5')  
print hex(h)  
TestEnumWindows()

print "All tests done!"  
