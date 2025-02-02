import subprocess
import psutil
class CPU:
    def __init__(self,name:str):
        self.name=name

    def printCpuInfo(self):
        cpu_name = subprocess.check_output("wmic cpu get name", shell=True).decode().split("\n")[1].strip()
        cpu_cores = psutil.cpu_count(logical=False)  
        cpu_threads = psutil.cpu_count(logical=True)
        print( f"{self.name}: {cpu_name}  {cpu_cores} (Core) {cpu_threads} (Threads)")         
