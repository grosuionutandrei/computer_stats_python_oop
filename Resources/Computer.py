import SystemInfo as si
from Memory import Disk 
import VirtualMemory
import CPU
import Gpu


class Computer:
    def __init__(self,name:str,system:si,disk:Disk,virtual:VirtualMemory,cpu:CPU,gpu:Gpu):
        self.name=name
        self.system=system
        self.disk=disk
        self.virtual=virtual
        self.cpu=cpu
        self.gpu=gpu

    def getComputerInfo(self):
        print("---System Info---")
        print(f"Name : {self.name}")
        self.system.printSystemInfo()
        self.disk.printDiskMemory("total")
        self.virtual.printVirtualMemory("total")
        self.cpu.printCpuInfo();
        print("---Gpu Info---") 
        self.gpu.printGpuInfo()
        print("---Memory Usage---")
        self.disk.printDiskInfoFull()
        self.virtual.printvirtualInfoFull()




