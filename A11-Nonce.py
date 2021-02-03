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
#device.write_memory(0x2320b8020, '\x11\x11\x11\x11\x11\x11\x11\x11')
#device.write_memory(0x2320b8030, '\x11\x11\x11\x11\x11\x11\x11\x11')



#'/0x11/0x11/0x11/0x11'
 #[0x2320b8000] = 2;
 #[0x2320b8028] = nonce[0];
 #[0x2320b802c] = nonce[1];

#f77
#0x20E0B8028 -
#0x20E0B802C
#            1-2  3-4  5-6  7-8  9-10 a-b  c-d  e-f
#2320b8020:  ffff ffff f6fb 5fff f505 3252 a7ec e3cc  ......_...2R....
#2320b8030:  7fff efbf fffd fff7 afff deff ffb5 fede  ................

#2320b8020:  bdff ffff f7fb 5fff 2f70 532b 5584 19c4  ......_./pS+U...
#2320b8030:  7fff efbf fffd fff7 afff dee7 ffb5 feba  ................

#2320b8020:  bfff ffff f7fb 7fff c7ba 7e72 742a a8b2  ..........~rt*..
#2320b8030:  7fbf efbf fffd fff7 ebff fef7 ff35 fedf  .............5..

#ipwndfu -p ; test.py ; --patch ; Images
