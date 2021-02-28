import dfu
import usbexec
import sys
import argparse
import usb.core

HOST2DEVICE = 0x21
DEVICE2HOST = 0xA1
DFU_DNLOAD = 1
DFU_ABORT = 4

parser = argparse.ArgumentParser(description='nonce setter', usage="./script.py -g 0xwhatever")
parser.add_argument('-g', '--generator', help='Generator to set', nargs=1)
args = parser.parse_args()
if not args.generator:
    exit('you didnt give a generator what the hell')

nonce = hex(int(args.generator[0], 16))[2:]
print(nonce)
noncearray = bytearray.fromhex(nonce)[::-1]

#Patch Nonce
device = dfu.acquire_device()
serial_number = device.serial_number
dfu.release_device(device)
device = usbexec.PwnedUSBDevice()
device.write_memory(0x2320b8000, '\x03\x02\x0a\x03')
device.write_memory(0x2320b8028, noncearray)
