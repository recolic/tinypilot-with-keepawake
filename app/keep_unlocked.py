# This module keeps target machine unlocked by one of two ways:
#   1. moving mouse by 1 pixel every 58 seconds.
#   2. press "Pause/Break" key every 58 seconds.

import time, threading
from hid import keyboard as fake_keyboard
from hid import keycodes as hid_keycodes

def wake_once_method_2(keyboard_path):
    hid_keycode = hid_keycodes.KEYCODE_PAUSE_BREAK
    hid_modifier_keycode = 0
    failed = "success"

    try:
        fake_keyboard.send_keystroke(keyboard_path, hid_modifier_keycode, hid_keycode)
    except Exception as e:
        failed = "failed " + str(e)
        pass
    
    #with open('/tmp/rlog2', 'w') as f:
    #    f.write('DEBUG: triggered! status=' + str(failed))
    
def keep_awake_daemon_func(keyboard_path):
    wake_once_method_2(keyboard_path)
    while True:
        time.sleep(58)
        wake_once_method_2(keyboard_path)

def start_keep_awake_thread(keyboard_path):
    thread = threading.Thread(target = keep_awake_daemon_func, args=(keyboard_path,))
    thread.start()
    #with open('/tmp/rlog', 'w') as f:
    #    f.write('DEBUG: keep unlocked thread started')
    # Never join

