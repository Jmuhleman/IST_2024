
---------------------------
## Commandes

- lsblk
- hdparm -t: timing test
- xxd: hexdump
- strings: find strings in binary files
- findmnt --real: find partitons that are mounted
- parted
    * print
    * mktable: new part table
    * mkpart: new partition
    * mkfs: format partition

- df: find free space
- blkid: list metadatas of availables partitions
- fsck -f : check check FS
- dumpe2fs: display the FS structure
-  sudo dd if=/dev/zero of=<block device> bs=1k seek=10 count=4k: 
    corrupte FS overwrite 4MB f data start= 10Kb


-  dd if=/dev/zero of=/tmp/bigfile bs=1M count=100: 
    create a 100MB file

- losetup -f: find the next loopback device: 
- sudo losetup /dev/loop6 /tmp/bigfile associate loopback with file
- sync: force to write from buffers



















