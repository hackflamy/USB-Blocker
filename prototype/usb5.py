from ctypes import windll
import visual
import disInput

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

if __name__ == '__main__':
    i = 0
    before = set(get_drives())
    print(before)
    while True:
        after = set(get_drives())
        print(after - before)
        if len(after - before) > 0:        
            visual.showScreen(i)
            disInput.Input(False)
            visual.root.mainloop()
        elif len(after - before) == 0:
            disInput.Input(True)
