## sigknock WPICTF 2020 Writeup

This was the challenge text:

```
sigknock - 200 (Linux)

Port knocking is boring. Enhance your security through obscurity using sigknock.

ssh ctf@sigknock.wpictf.xyz

pass: $1gkn0ck

made by: acurless

Note: this challenge is in no way related to the open source tool of the same name.

```

When you SSH in, you're dropped in an alpine docker container.

```
$ ssh ctf@sigknock.wpictf.xyz

~ $ cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.11.5
PRETTY_NAME="Alpine Linux v3.11"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://bugs.alpinelinux.org/"

~ $ ls -lah .
total 16K    
drwxr-sr-x    1 wpictf   nogroup     4.0K Apr 19 19:53 .
drwxr-xr-x    1 root     root        4.0K Apr 14 05:16 ..
-rw-------    1 wpictf   nogroup       31 Apr 19 19:53 .ash_history

~ $ id
uid=1010(wpictf) gid=65533(nogroup) groups=65533(nogroup)

~ $ ps aux
PID   USER     TIME  COMMAND
    1 wpictf    0:00 {init_d} /bin/sh /bin/init_d
    7 wpictf    0:00 /usr/bin/irqknock
    8 wpictf    0:00 /bin/sh
   12 wpictf    0:00 ps aux
```

There's an interesting process running `/usr/bin/irqknock`...

This must be a hint to do some interrupt requests (IRQ) against the process.

I quickly discovered that sending SIGINT increased the program "state":
```
~ $ kill -2 $pid
Got signal 2
State advanced to 1
```

I made this little hack to get the pid for irqknock which came in handy:
```
~ $ pid=$(ps aux | grep irq | grep -v grep | tr -s ' ' | cut -d ' ' -f 2)
~ $ echo $pid
7
```

Through some trial and error I discovered the correct "IRQ knock sequence":
```
~ $ kill -2 $pid
Got signal 2
State advanced to 1

~ $ kill -3 $pid
Got signal 3
State advanced to 2

~ $ kill -11 $pid
Got signal 11
State advanced to 3

~ $ kill -13 $pid
Got signal 13
State advanced to 4

~ $ kill -17 $pid
Got signal 17
State advanced to 5
WPI{1RQM@St3R}
```

There's the flag `WPI{1RQM@St3R}` :D
