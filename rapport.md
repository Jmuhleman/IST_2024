# Rendu IST 2024 Labo 1 

## Task 1

* 1
   - The boot partition is mounted on /dev/sda2
   - metadatas: brw-rw----  1 root disk      8,   2 feb 22 20:37 sda2
   - The root partition is mounted on /dev/sda3
   -  jul@jul-VirtualBox:~$ sudo hdparm -t /dev/sda2
        /dev/sda2:
        Timing buffered disk reads: 512 MB in  2.85 seconds = 179.78 MB/sec
* 2
   - We can see the hex values of the data stored on /dev/sda3
* 3
   - copy the text of target file
   - run: strings /dev/sda3 | grep "researched text"

TODO: TO FORMAT ACCORDING PROFESSOR REQUIREMENTS

## Task 2


lsblk -> visual

sudo mkfs -t fat32 /dev/sdb -> formattage

sudo mkdir -p /mnt/part1 /mnt/part -> create mount point 'usb'

sudo mount -t auto /dev/sdb /mnt/part -> mount sdb on part folder

sudo parted /dev/sdb -> managing the external drive


(parted) print
		Model: VBOX HARDDISK (scsi)
		Disk /dev/sdb: 90,0MB
		Sector size (logical/physical): 512B/512B
		Partition Table: msdos
		Disk Flags:

		Number  Start   End     Size    Type     File system  Flags
		 1      512B    45,0MB  45,0MB  primary               lba
		 2      45,0MB  90,0MB  45,0MB  primary  ext2
		 

Creating metadatas and formatting but not completly according professor assistant
we need to format once again with mkfs command as following:

sudo mkfs -t vfat /dev/sdb1
		mkfs.fat 4.2 (2021-01-31)

sudo mkfs -t ext4 /dev/sdb2

		Creating filesystem with 10985 4k blocks and 10992 inodes

		Allocating group tables: done
		Writing inode tables: done
		Creating journal (1024 blocks): done
		Writing superblocks and filesystem accounting information: done
		
		
		
		
		
sudo mount /dev/sdb1 /mnt/part1
sudo mount /dev/sdb2 /mnt/part2


lsblk

		sdb      8:16   0  85,8M  0 disk
		├─sdb1   8:17   0  42,9M  0 part /mnt/part1
		└─sdb2   8:18   0  42,9M  0 part /mnt/part2
		sr0     11:0    1  1024M  0 rom



df
		disk free output  in MB
		
		/dev/sdb1        43M     0   43M   0% /mnt/part1 -> 100% free
		/dev/sdb2        37M   24K   34M   1% /mnt/part2 -> 99% free

df -h
		output in 1k blocks
		/dev/sdb1          43828        0     43828   0% /mnt/part1
		/dev/sdb2          37060       24     33964   1% /mnt/part2
		
		
		
Task 3
	1. 
		a. 	 Linux version 6.5.0-21-generic
			(buildd@lcy02-amd64-091)
			(x86_64-linux-gnu-gcc-12 
			(Ubuntu 12.3.0-1ubuntu1~22.04) 
			12.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) 
			#21~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Feb  9 13:32:52 UTC 2
		
		b.  -bash
	
	
		e.  cat filesystems | grep -v 'nodev'
	
	
	3. 
		a.
			/dev/sdb2: UUID="c05ca81b-f41a-4fba-9cd3-3200a74ff1a4" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="d16fa281-02"
			/dev/sdb1: SEC_TYPE="msdos" UUID="6800-9D09" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="d16fa281-01"
			-> OK
		
		b.
			the 'BLOCK_SIZE' for the size of 
	
		
		
		
	4.
		a.
			UUID=0c31dc6b-2500-4c2f-ba34-22a5850d1265 /               ext4    errors=remount-ro 0       1
			
		
task 4
		4.
			Free inodes:              10981
		5.
			sudo fsck /dev/sdb2
		6.
			 sudo mount /dev//sdb2 /mnt/part2
task 5
		1.
			
		5.	seen as:
			└─/mnt/bigfile                       /dev/loop10 ext4       rw,relatime
			
		6.
			 sync -d /dev/bigfile
			 sudo strings /dev/loop10 | grep 'asddfsadfhlsdkjfh'
			
						


