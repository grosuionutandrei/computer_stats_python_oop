import subprocess
class GPU:
    def __init__(self,name:str):
        self.name=name
    def printGpuInfo(self):
        print (self.get_gpu_info())
    
    
    def get_gpu_info(self):
        try:
            gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode()
            gpu_list = [line.strip() for line in gpu_info.split("\n") if line.strip()][1:]
            return gpu_list
        except Exception as e:
          return ["Could not retrieve GPU info"]


