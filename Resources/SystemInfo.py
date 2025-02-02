import platform

class SystemInfo:
  measure = " GiB"
  hostname = "Hostname: "
  system = "System: "
  kernel = "Kernel: "
  def __init__(self):
           self.hostname = platform.node()
           self.system = platform.system()  
           self.architecture = platform.machine()  
           self.kernel_version = platform.release()
           self.compiler = platform.python_compiler()
           
  def printSystemInfo(self):
          print("---System Info---")
          print("Hostname:", self.hostname)
          print("System:", self.system, self.architecture)
          print("Kernel:", self.kernel_version)
          print("Compiler:", self.compiler)
        
           
          




           
      


      
