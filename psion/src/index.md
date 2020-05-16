# Iain's Psion Series3a Page

![Psion with manual](img/main.jpg){: class="img-fluid" }

This page is still 
![Under construction](img/underconstruction.gif)

## TODO: Device Overview

### TODO: Hardware Overview

### TODO: Software overview

## File transfer between Windows 10 and Psion over serial link

Here is my procedure for doing file transfer from Windows 10.
The heart of the problem is that PsiWin (version 1, the version that is designed to work with the Psion 3a), is a 16-bit program. That doesn't work anymore on Windows 10. The secondary problem I faced is that my PC doesn't have a serial port, and configuring the USB-to-serial adapter I had wasn't always obvious. Here is my exact setup, that is probably suboptimal in many ways.

### Materials and Software

* Psion Series 3a
* Psion 3Link RS232 serial interface
* StarTech USB to RS232 DB9/DB25 Serial Adapter Cable (Part# `ICUSB232DB25`) - Prolific chipset `PL-2303 HXD`
* Windows 10
* VirtualBox  (TODO: link)
* Windows 2000 Professional SP4

### Configuring the USB-to-Serial adapter

1. When first connecting the adapter, Windows will pick the most recent driver it can. This driver caused `This device cannot start. (Code 10)` errors for me (visible in Device Manager.)
1. Looking up the chipset (from Prolific), I was able to find a different driver (installer version 1.20.0, driver version 3.8.25.0) which seemed to work a bit better - I still need to remove and reconnect the adapter to get it to work sometimes. (TODO: link)
1. In the device properties, modify the port settings. The following worked - no guarantee its the only option:
    * Bits per second: 9600
    * Data bits: 8
    * Parity: None
    * Stop bits: 1
    * Flow control: None
    * In the "Advanced" screen, disable "Use FIFO buffers"

### Setting up the virtual machine

1. Install Win2K in VirtualBox (nothing fancy necessary here.)
1. Bridge the serial port to the VM. In the VM's settings:
    1. Select "Serial Ports"
    1. My device was on COM4, so for sanity go to `Port 4` tab
    1. Check "Enable Serial Port"
    1. Port Mode: `Host Device`
    1. Path/Address: `COM4` or whatever port your adapter is on.
1. Share a folder with the VM. In the VM's settings:
    1. Select "Shared Folders", right-click, "Add Shared Folder"
    1. Select a folder of your choice on the host.
    1. Give it a simple name, e.g. `shared`.
    1. Check "Auto-mount", Mount point: `Z`, Check "Make Permanent".
1. In the VM, configure the serial port:
    1. Open Control Panel, System, Hardware tab, Device Manager
    1. Ports (COM & LPT) - you should see your serial port here.
    1. Ensure port settings match the hosts.

### Installing the PsiWin software

1. Download it. All versions I could find come as three floppy disks worth. here is one version containing one zip per disk. Extract each floppy into a folder in the shared folder. Then copy everything to the VM's desktop (things won't work well in the shared folder.)
    * TODO(download)
    * Note you could download in the VM, but exposing a Win2K VM to the internet is a bad idea.
1. Run the `SETUP.EXE` installer. When it wants Disk 2 and 3, just point to the corresponding folders.
1. Accept the option to start PsiWin, then...
1. Physically connect the Psion. On the System screen, in Special, select `Remote Link`, `On` with `Baud rate 9600`. Hit enter.
1. Back in the PsiWin in the VM, select `COM4`, `Baud rate: 9600`, OK.
    * For no particular reason, I have had this not work on the first try before. If it fails, check serial port settings and retry.
1. The first time you do this it may copy files to the Psion. After that, you should see the Psion's drives mounted in PsiWin.

