from pymem import Pymem
from pymem.ptypes import RemotePointer
from time import sleep

ammoValue = 999

pm = Pymem("ChaosGame424-Win64-Shipping.exe")

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
if __name__ == "__main__":
    while True:
        try:
            if (pm.read_int(getPointerAddress(pm.base_address + 0x035CC570, offsets=[0x10, 0x20, 0x50, 0x298, 0xE0, 0x248, 0x974]))) != ammoValue:
                pm.write_int(getPointerAddress(pm.base_address + 0x035CC570, offsets=[0x10, 0x20, 0x50, 0x298, 0xE0, 0x248, 0x974]), ammoValue)
            else:
                pass
        except:
            print("Couldt write memory!")
        sleep(0.1)
            