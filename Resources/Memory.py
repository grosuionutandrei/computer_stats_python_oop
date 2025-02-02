import psutil

class Disk:
    gb =1073741824
    def __init__ (self,name,measureUnit):
         self.measureUnit=measureUnit
         self.name=name

    def computeDiskMemory(self,gb, getTypeMemory, mem_type):
       total_disk_space = 0
       count = 0  
       for drive in ["C:\\", "D:\\", "E:\\"]:
        try:
            if mem_type == "percent":
                total_disk_space += psutil.disk_usage(drive).percent
                count += 1 
            else:
                total_disk_space += round(getTypeMemory(drive, mem_type) / gb)
        except FileNotFoundError:
            continue 
       if mem_type == "percent" and count > 0:
            return str(round(total_disk_space / count)) 
        
       return str(total_disk_space)

# Function to get disk memory type
    def getTypeMemory(self,path, mem_type):
      disk_info = psutil.disk_usage(path)
      if mem_type == "total":
        return disk_info.total
      elif mem_type == "used":
        return disk_info.used
      elif mem_type == "free":
        return disk_info.free
      elif mem_type == "percent":
        return disk_info.percent
      else:
        raise ValueError("Invalid type. Choose from 'total', 'used', 'free', or 'percent'.")    

    #Get total disk memory
    def printDiskMemory(self,memoryType:str):
       print(f'{self.name}:  {self.computeDiskMemory(Disk.gb,self.getTypeMemory,memoryType)}  {self.measureUnit}')  
    
    def printDiskInfoFull(self):
        print(
            self.name + ":"
            + self.computeDiskMemory(Disk.gb, self.getTypeMemory, "total")
            + self.measureUnit
            + " / "
            + self.computeDiskMemory(Disk.gb, self.getTypeMemory, "used")
            + self.measureUnit
            + " / "
            + self.computeDiskMemory(Disk.gb,self.getTypeMemory,"percent")
            + "%")
 

