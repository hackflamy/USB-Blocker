import pyHook, pythoncom

hm = pyHook.HookManager()
def disable(event):
    return False
def enable (event):
    return True

def OnKeyboardEvent(event):
    if event.Key.lower() in ['lwin', 'tab', 'rwin', 'lmenu', 'lctrl', 'rctrl']:
        return False
    else:
        return True

def disableInput():
    hm.KeyAll = OnKeyboardEvent
    hm.HookKeyboard()

def enableInput():
    hm.KeyAll = enable
    #hm.UnhookKeyboard()


def Input(s):
    if s == True:
        enableInput()
    else:
        disableInput()
    #pythoncom.PumpMessages()
