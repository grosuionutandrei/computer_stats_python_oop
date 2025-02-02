import psutil
class VirtualMemory:
    gb = 1073741824
    def __init__(self,name,measureUnit):
          self.measureUnit=measureUnit
          self.name=name

# retrieve info bassed on  memory type          
    def getvirtualMemory(self,type:str):
         if type=="total":
              return str(round(psutil.virtual_memory().total / VirtualMemory.gb))
         if type =="available":
              return str(round(psutil.virtual_memory().available / VirtualMemory.gb))
         if type=="percent":
              return str(psutil.virtual_memory().percent)
         raise ValueError("Invalid type. Choose from 'total', 'used', 'free', or 'percent'.")
    
    def printVirtualMemory(self,type:str):
         if type== "percent":
              print(f"{self.name} : {self.getvirtualMemory(type)} %")
              return  
         else :  
              print(f"{self.name} : {self.getvirtualMemory(type)} {self.measureUnit}")   
#print all info about virtual memory              
    def printvirtualInfoFull(self):
       print(
    self.name +": "
    + self.getvirtualMemory("total")
    + self.measureUnit
    + " / "
    + self.getvirtualMemory("available")
    + self.measureUnit
    + " / "
    + self.getvirtualMemory("percent")
    + "%")
        
            
       

           
