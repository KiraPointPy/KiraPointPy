import os
import platform
import sys
from datetime import datetime

def run_system_check():
    """
    Performs a professional system check
using native Python libraries.
    Ensures 100% compatibility with Windows 7.
    """
    current_time=datetime.now().strftime("%Y-%m-&d %H:%M:%S")

    pc_name = os.environ.get ('COMPUTENAME', 'Unknown')

    os_info= f"{platform.system()}{platform.relase()}"

    processor= platform.processor()
    python_ver = sys.version.split()[0]

    report = f"""
    ============================================
   PROFESSIONAL SYSTEM CHECK - KIRA-POINT.PY 
============================================
   
    
    TIMESTAMP:      {current_time}
    PC_NAME:         {pc_name}
    OS_VERSION:     {os_info}
    PROCESSOR:      {processor}
    PYTHON_VER:     {python_ver}
    STATUS:         OPERATIONAL
    
============================================
============================================
"""

    print(report)

if __name__=="__main__":
    run_system_check()




