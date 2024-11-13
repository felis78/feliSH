import platform
import os
from utils.comands import Commands

interpret = Commands()
system = ""
login = os.getlogin()
actualDirPath = os.getcwd()
actualDir = os.path.basename(actualDirPath)

if platform.system() == "Windows":
    system = platform.uname().node
else:
    system = os.uname()[1]

while 1:
    user = input(login+'@'+system + " -> /" + actualDir + ": ")
    interpret.execute(user.split())

