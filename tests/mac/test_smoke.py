import pyautogui
import time
import subprocess
import pytest

def test_open_focus_bear():
    print("🔹 Test started")
    
    # Launch Focus Bear using open command
    subprocess.Popen(["open", "/Applications/Focus Bear.app"])
    time.sleep
