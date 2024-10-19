import subprocess
from urllib import response 
import requests
from time import sleep

def ctrl_motion(action):
    """控制motion启动和停止"""
    try:
        if action =='start':
            subprocess.run(["sudo","motion"])
        elif action =='stop':
            subprocess.run(["sudo","killall","motion"])
        else:
            None
        print(f"Motion {action} successfully.")
    except subprocess.CalledProcessError:
        print(f"Filed to {action} Motion.")
def get_motion_stream():
    """获取motion视频流的函数"""
    try:
        response = requests.get("http://localhost:8081/",stream=True)
        response.raise_for_status()
        print("Motion stream started successfully.")
        return response
    except subprocess.CalledProcessError as e:
        print(f"Error getting Motion stream: {e}")


ctrl_motion('start')
sleep(2)
stream = get_motion_stream()
try:
    if stream:
        for chunk in stream.iter_content(chunk_size=1024):
            print(1)
            sleep(1)
except KeyboardInterrupt:
    ctrl_motion('stop')
