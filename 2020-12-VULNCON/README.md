## Memory Forensics 1: Game Over

Profile information:
```
$ volatility -f dump.raw imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/user/ctf/vulcon/dump.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002bf20a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002bf3d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-12-12 14:05:05 UTC+0000
     Image local date and time : 2020-12-12 19:35:05 +0530
```

* I used this volatility chrome plugin (chromehistory): https://github.com/superponible/volatility-plugins

```
$ volatility --plugins=volatility-plugins/ --profile=Win7SP0x64 -f dump.raw chromehistory
Volatility Foundation Volatility Framework 2.6.1
Index  URL                                                                              Title                                                                            Visits Typed Last Visit Time            Hidden Favicon ID
------ -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ------ ----- -------------------------- ------ ----------
     7 https://www.google.com/search?source=hp...QCgAQGqAQdnd3Mtd2l6sAEA&sclient=psy-ab facebook - Google खोजी                                                        2     0 2020-12-12 13:46:13.497778        N/A       
     1 http://google.com/                                                               Google                                                                                2     2 2020-12-12 13:46:06.035590        N/A       
     4 https://www.google.com/search?source=hp...nO2MycjtAhW3zzgGHcBJDXIQ4dUDCAc&uact=5 online betting game - Google खोजी                                             3     0 2020-12-12 13:42:15.187823        N/A       
     8 https://www.facebook.com/                                                        Facebook - Log In or Sign Up                                                          2     0 2020-12-12 13:46:16.862696        N/A       
     2 http://www.google.com/                                                           Google                                                                                2     0 2020-12-12 13:46:06.035590        N/A       
     6 https://www.gamblingsites.org/                                                   Online Gambling Sites - Best Real Money Gambling Sites 2020                           1     0 2020-12-12 13:43:07.638967        N/A       
     3 https://www.google.com/                                                          Google                                                                                2     0 2020-12-12 13:46:06.035590        N/A       
     4 https://www.google.com/search?source=hp...nO2MycjtAhW3zzgGHcBJDXIQ4dUDCAc&uact=5 online betting game - Google खोजी                                             3     0 2020-12-12 13:42:15.187823        N/A       
     7 https://www.goov%;|e±åÐëþ...iyÈYdñ(³                                                                                       1     0 1601-01-01 00:00:00               N/A       
     1 http://google.com/                                                               Google                                                                                1     1 2020-12-12 13:41:40.947451        N/A
```

Flag: `vulncon{gamblingsites-12-12-2020}`

## Memory Forensics 2: USB Device

* I used this volatility plugin (usbstor): https://github.com/kevthehermit/volatility_plugins

```
$ volatility --plugins=volatility_plugins/ --profile=Win7SP0x64 -f dump.raw usbstor
Volatility Foundation Volatility Framework 2.6.1
Reading the USBSTOR Please Wait
Found USB Drive: CCYYMMDDHHmmSSX1TIOR&0
	Serial Number:	CCYYMMDDHHmmSSX1TIOR&0
	Vendor:	SMI
	Product:	USB_DISK
	Revision:	1100
	ClassGUID:	USB_DISK

	ContainerID:	{68b70eb8-f3fd-5099-907d-4e542601b2c7}
	Mounted Volume:	\??\Volume{f7d58027-3b76-11eb-a2d8-d0abd5a4ad75}
	Drive Letter:	\DosDevices\E:
	Friendly Name:	SMI USB DISK USB Device
	USB Name:	Unknown
	Device Last Connected:	2020-12-11 06:19:46 UTC+0000

	Class:	DiskDrive
	Service:	disk
	DeviceDesc:	@disk.inf,%disk_devdesc%;Disk drive
	Capabilities:	16
	Mfg:	@disk.inf,%genmanufacturer%;(Standard disk drives)
	ConfigFlags:	0
	Driver:	{4d36e967-e325-11ce-bfc1-08002be10318}\0001
	Compatible IDs:
		USBSTOR\Disk
		USBSTOR\RAW
		
		
	HardwareID:
		USBSTOR\DiskSMI_____USB_DISK________1100
		USBSTOR\DiskSMI_____USB_DISK________
		USBSTOR\DiskSMI_____
		USBSTOR\SMI_____USB_DISK________1
		SMI_____USB_DISK________1
		USBSTOR\GenDisk
		GenDisk

Windows Portable Devices
	--
	FriendlyName:	E:\
	Serial Number:	CCYYMMDDHHMMSSX1TIOR&0
	Last Write Time:	2020-12-11 06:19:59 UTC+0000
```

Flag: `vulncon{68b70eb8-f3fd-5099-907d-4e542601b2c7}`

## Memory Forensics 3: Phishy Email

Dumped all strings appearing to be an email from the memory dump:
```
strings dump.raw  | egrep '([[:alnum:]_.-]{1,64}+@[[:alnum:]_.-]{2,255}+?\.[[:alpha:].]{2,4})' > email_strings.txt
```

Then searched for the `:)` string manually and found the email:
```
...
"email": "sarojchaudhary581@gmail.com",
"name": "Technical Boy"
"rthMsgId": null,
"snippet": "Congratulations! You have 1000$ from an online betting game. Open the attachment and take your money :)",
"starred":false,
"subject":"You have won 1000$",
...
```

Flag: `vulncon{sarojchaudhary581@gmail.com}`

## Memory Forensics 4: UnKnown Backdoor

I took a look at the netscan (netstat-like) information:
```
$ volatility --plugins=volatility-plugins/ --profile=Win7SP0x64 -f dump.raw netscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x4ca493b0         UDPv4    0.0.0.0:5353                   *:*                                   2588     chrome.exe     2020-12-12 13:45:43 UTC+0000
0x4ca493b0         UDPv6    :::5353                        *:*                                   2588     chrome.exe     2020-12-12 13:45:43 UTC+0000
0x4ca49d60         UDPv4    0.0.0.0:5353                   *:*                                   2588     chrome.exe     2020-12-12 13:45:43 UTC+0000
0x4cb1d740         UDPv6    fe80::fd64:305c:49bc:c47c:1900 *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4cc47010         UDPv6    fe80::fd64:305c:49bc:c47c:546  *:*                                   736      svchost.exe    2020-12-12 13:59:39 UTC+0000
0x4cdf79c0         UDPv6    ::1:57133                      *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4caad010         TCPv4    -:49258                        172.16.130.254:443   CLOSED           2908     chrome.exe     
0x4cc8c200         TCPv4    172.16.130.133:49255           52.22.236.125:443    CLOSED           2908     chrome.exe     
0x4cd6e360         TCPv4    172.16.130.133:49270           74.125.24.109:993    CLOSED           4020     mailsync.exe   
0x4cf23900         UDPv4    172.16.130.133:137             *:*                                   4        System         2020-12-12 13:45:19 UTC+0000
0x4cf42a10         UDPv4    0.0.0.0:0                      *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4cf42a10         UDPv6    :::0                           *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4cf42ec0         UDPv4    0.0.0.0:5355                   *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4cf42ec0         UDPv6    :::5355                        *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4cf6ecf0         UDPv4    0.0.0.0:5355                   *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4cf78cb0         UDPv4    127.0.0.1:1900                 *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4cf78ec0         UDPv6    ::1:1900                       *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4d068c20         UDPv4    172.16.130.133:1900            *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4d27fc20         UDPv4    127.0.0.1:57134                *:*                                   2800     svchost.exe    2020-12-12 13:47:16 UTC+0000
0x4d5b5730         UDPv4    0.0.0.0:50178                  *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4ce41ef0         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        480      lsass.exe      
0x4ced6740         TCPv4    172.16.130.133:139             0.0.0.0:0            LISTENING        4        System         
0x4cfcc6c0         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        480      lsass.exe      
0x4cfcc6c0         TCPv6    :::49156                       :::0                 LISTENING        480      lsass.exe      
0x4d0573e0         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        464      services.exe   
0x4d15f120         TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System         
0x4d15f120         TCPv6    :::445                         :::0                 LISTENING        4        System         
0x4d160b00         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        464      services.exe   
0x4d160b00         TCPv6    :::49155                       :::0                 LISTENING        464      services.exe   
0x4d2168a0         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        660      svchost.exe    
0x4d2183d0         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        660      svchost.exe    
0x4d2183d0         TCPv6    :::135                         :::0                 LISTENING        660      svchost.exe    
0x4d2207e0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        364      wininit.exe    
0x4d224c90         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        364      wininit.exe    
0x4d224c90         TCPv6    :::49152                       :::0                 LISTENING        364      wininit.exe    
0x4d25a420         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        736      svchost.exe    
0x4d25a420         TCPv6    :::49153                       :::0                 LISTENING        736      svchost.exe    
0x4d25e4f0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        736      svchost.exe    
0x4d3ae300         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        840      svchost.exe    
0x4d3afc90         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        840      svchost.exe    
0x4d3afc90         TCPv6    :::49154                       :::0                 LISTENING        840      svchost.exe    
0x4ce2fcf0         TCPv4    172.16.130.133:49276           52.22.236.125:443    CLOSED           4020     mailsync.exe   
0x4d11f900         TCPv4    172.16.130.133:49170           172.217.194.108:993  CLOSED           4020     mailsync.exe   
0x4d282010         TCPv4    -:49285                        142.250.67.164:443   CLOSED           2908     chrome.exe     
0x4d2a26a0         TCPv4    172.16.130.133:49288           35.213.130.45:5552   CLOSED           2932     dwm.exe        
0x4d3c5340         TCPv4    172.16.130.133:49279           172.16.130.254:443   CLOSED           2596     mailspring.exe 
0x4d3f09f0         TCPv4    172.16.130.133:49199           216.58.203.1:443     CLOSED           4020     mailsync.exe   
0x4d5f0640         TCPv4    172.16.130.133:49188           216.58.203.1:443     CLOSED           4020     mailsync.exe   
0x4df6d850         UDPv4    0.0.0.0:61677                  *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4df6d850         UDPv6    :::61677                       *:*                                   484      svchost.exe    2020-12-12 14:05:05 UTC+0000
0x4df97600         TCPv4    -:0                            56.11.7.17:0         CLOSED           2908     chrome.exe
```

The first that jumps out to me is `dwm.exe` reaching out over port 5552:
```
172.16.130.133:49288           35.213.130.45:5552   CLOSED           2932     dwm.exe
```

A quick Google search told me that njRAT uses 5552 for C2. An alternate name for njRAT is Bladabindi which is the flag.

Flag: `vulncon{Bladabindi-5552}`