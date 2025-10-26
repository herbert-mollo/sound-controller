import sys
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_mute(mute: bool):
    # Obtiene el dispositivo de salida (altavoces)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(mute, None)
    print(f"mute state set to {mute}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "mute":
            set_mute(True)
        elif action == "unmute":
            set_mute(False)
        else:
            print("Uso: python sound_control.py [mute|unmute]")
    else:
        print("Falta argumento: mute o unmute")
