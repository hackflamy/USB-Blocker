from subprocess import Popen
from threading import *

def runUsb():
    p = Popen("runUsb.bat", cwd=r"..\USB Project")
    stdout, stderr = p.communicate()

def killCom():
    p = Popen("killCom.bat", cwd=r"..\USB Project")
    stdout, stderr = p.communicate()

k = Timer(1.5, killCom)
r = Thread(target=runUsb)

k.start()
r.start()
