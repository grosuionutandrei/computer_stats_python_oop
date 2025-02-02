import SystemInfo as si
from Memory import Disk 
from VirtualMemory import VirtualMemory
from CPU import CPU
from Gpu import GPU
from Computer import Computer


measureUnit= "Gib"
system =  si.SystemInfo()
disk = Disk("Disk", measureUnit)
virtual = VirtualMemory("Memory" ,measureUnit)
cpu= CPU("Cpu")
gpu=GPU("Gpu")
computer = Computer("Personal computer",system,disk,virtual,cpu,gpu)
computer.getComputerInfo()
