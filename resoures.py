import os
import platform
import psutil
import subprocess

measure = " GiB"
hostname = "Hostname: "
system = "System: "
kernel = "Kernel: "
compiler = "Compiler: "
memory = "Memory: "  
disk = "Disk: "
Gpu = "Grphic Card : "
gb = 1073741824  # 1 GB in bytes



hostname = platform.node()
system = platform.system()  
architecture = platform.machine()  
kernel_version = platform.release()
compiler = platform.python_compiler()

#cpu
cpu_name = subprocess.check_output("wmic cpu get name", shell=True).decode().split("\n")[1].strip()
cpu_cores = psutil.cpu_count(logical=False)  
cpu_threads = psutil.cpu_count(logical=True)  
#gpu
def get_gpu_info():
    try:
        gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode()
        gpu_list = [line.strip() for line in gpu_info.split("\n") if line.strip()][1:]
        return gpu_list
    except Exception as e:
        return ["Could not retrieve GPU info"]

gpu_list = get_gpu_info()


# Disk Memory
def computeDiskMemory(gb, getTypeMemory, mem_type):
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
def getTypeMemory(path, mem_type):
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


print("---System Info---")
print("Hostname:", hostname)
print("System:", system, architecture)
print("Kernel:", kernel_version)
print("Compiler:", compiler)
print(disk + computeDiskMemory(gb, getTypeMemory, "total") + measure)
print(  memory+ str(round(psutil.virtual_memory().total / gb))+ measure)
print("CPU:", cpu_name, f"{cpu_cores} (Core), {cpu_threads} (Threads)")
print("---Gpu Info---")
print(gpu_list)
print("---Memory Usage---")
print(
    memory
    + str(round(psutil.virtual_memory().total / gb))
    + measure
    + " / "
    + str(round(psutil.virtual_memory().available / gb))
    + measure
    + " / "
    + str(psutil.virtual_memory().percent)
    + "%"
)

print(
    disk
    + computeDiskMemory(gb, getTypeMemory, "total")
    + measure
    + " / "
    + computeDiskMemory(gb, getTypeMemory, "used")
    + measure
    + " / "
    + computeDiskMemory(gb,getTypeMemory,"percent")
    + "%"
)



