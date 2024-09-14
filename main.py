import psutil
from pypresence import Presence
import time

def is_game_running(game_process_name):
    
    for process in psutil.process_iter():
        try:
            if game_process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

CLIENT_ID = '1284264076578394282'
rpc = Presence(CLIENT_ID)
rpc.connect()
start_time=time.time()
while True:
    if is_game_running('sh3.exe'):  
        rpc.update(state="Walking through a nightmare", details="Exploring Silent Hill", large_image="iconalt", large_text="I hate mirrors..", start=start_time)
    else:
        rpc.clear()  
    time.sleep(15)
