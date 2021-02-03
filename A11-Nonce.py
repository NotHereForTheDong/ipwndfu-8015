import dfu
import usbexec
import sys
import usb.core

device = dfu.acquire_device()
serial_number = device.serial_number
dfu.release_device(device)
device = usbexec.PwnedUSBDevice()
device.write_memory(0x2320b8000, '\x03\x02\x0a\x03')
device.write_memory(0x2320b8028, '\x11\x11\x11\x11')
device.write_memory(0x2320b802C, '\x11\x11\x11\x11')
