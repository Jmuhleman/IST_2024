# IST Lab 01 : File Systems 

Authors : Butty Vicky & Mühlemann Julien

Group : L01GrA

Date : 02.03.2024

## TASK 1: EXPLORE BLOCK DEVICES AND FILESYSTEMS

1. > Using the `lsblk` command, list the existing block devices.

   ```bash
   $ lsblk
   NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
   fd0      2:0    1     4K  0 disk
   loop0    7:0    0  63.4M  1 loop /snap/core20/1974
   loop1    7:1    0     4K  1 loop /snap/bare/5
   loop2    7:2    0  63.9M  1 loop /snap/core20/2182
   loop3    7:3    0 266.6M  1 loop /snap/firefox/3836
   loop4    7:4    0  73.9M  1 loop /snap/core22/858
   loop5    7:5    0 349.7M  1 loop /snap/gnome-3-38-2004/143
   loop6    7:6    0 237.2M  1 loop /snap/firefox/2987
   loop7    7:7    0 485.5M  1 loop /snap/gnome-42-2204/120
   loop8    7:8    0  91.7M  1 loop /snap/gtk-common-themes/1535
   loop9    7:9    0  12.3M  1 loop /snap/snap-store/959
   loop10   7:10   0  53.3M  1 loop /snap/snapd/19457
   loop11   7:11   0  40.4M  1 loop /snap/snapd/20671
   loop12   7:12   0   497M  1 loop /snap/gnome-42-2204/141
   loop13   7:13   0   452K  1 loop /snap/snapd-desktop-integration/83
   sda      8:0    0    20G  0 disk
   ├─sda1   8:1    0     1M  0 part
   ├─sda2   8:2    0   513M  0 part /boot/efi
   └─sda3   8:3    0  19.5G  0 part /var/snap/firefox/common/host-hunspell
                                    /
   sr0     11:0    1 155.3M  0 rom
   sr1     11:1    1   4.7G  0 rom
   ```

   

   - > On which block device is the boot partition mounted? In the `/dev` directory find the special file corresponding to this block device. With `ls -l` list its metadata.

     The boot partition is mounted on `/dev/sda2`.

     We can list it's metadata (using a long listing format) with the following command:

     ```bash
     $ ls -l /dev/sda2
     brw-rw---- 1 root disk 8, 2 Mär  1 20:21 /dev/sda2
     ```

     These are: file permissions, number of links, owner name, owner group, file size (bytes), last modification time and pathname.

     

   - > On which block device is the root (/) partition mounted? What is the name of its special file?

     The root partition is mounted on `/dev/sda3`.

     

   - > With `hdparm -t` do a timing test on the boot partition. What throughput do you get?

     ```bash
     $ sudo hdparm -t /dev/sda2
     
     /dev/sda2:
      Timing buffered disk reads: 512 MB in  0.25 seconds = 2008.50 MB/sec
     ```

     Note that the throughput  may vary from time to time, depending on the system and its use.

   

2. > Convince yourself that the special file representing the root (/) partition can be read just like any other file. As it contains binary data, just opening it with `less` will mess up the terminal, so use the `xxd` hexdump utility.

   - > To see how `xxd` works, create a small text file and open it with `xxd -a`.

     ```bash
     $ cd /usr/share/doc
     $ echo "This is a test!" > testfile.txt | xxd -a testfile.txt
     00000000: 5468 6973 2069 7320 6120 7465 7374 210a  This is a test!.
     ```

     As we can see, `xxd` allow us to create a hex dump of the given file.

     

   - > Now open the special file with the same command. You may pipe its output into `less`. What do you see? If your root partition uses LVM (verify with `lsblk`), you should see text strings containing volume group configuration information.

     Using the command `sudo xxd -a /dev/sda3 | less`, we can see the hex dump of `sda3`. The beginning of the file is shown below. Note that the `*` replaces nul-lines, as requested by the `-a` option.

     ```bash
     00000000: 0000 0000 0000 0000 0000 0000 0000 0000  ................
     *
     00000400: 0080 1300 00fc 4d00 33e6 0300 ab98 1d00  ......M.3.......
     00000410: 8671 1000 0000 0000 0200 0000 0200 0000  .q..............
     00000420: 0080 0000 0080 0000 0020 0000 b12a e265  ......... ...*.e
     00000430: b12a e265 0500 ffff 53ef 0100 0100 0000  .*.e....S.......
     00000440: d773 d765 0000 0000 0000 0000 0100 0000  .s.e............
     00000450: 0000 0000 0b00 0000 0001 0000 3c00 0000  ............<...
     00000460: c602 0000 6b04 0000 76be eedf f81c 4ecb  ....k...v.....N.
     00000470: 8fc3 0908 14c0 1177 0000 0000 0000 0000  .......w........
     00000480: 0000 0000 0000 0000 2f00 0000 0000 0000  ......../.......
     00000490: 0000 0000 0000 0000 0000 0000 0000 0000  ................
     *
     ```

     

3. >  As the special file represents all the blocks of a partition, the content of all files of the root partition should be there. Pick a text file at random (for example a file in `/usr/share/doc/`) and try to find its content in the special file.
   >
   >  - Tip: There is a filter utility that looks for data that looks like text strings and removes everything else: the `strings` command.

   As we have created our file `testfile.txt` in the folder `/usr/share/doc/`, we can search for its contents with the command `sudo strings /dev/sda3 | grep "This is a test!"`.

   This will retrieve the raw binary data from the `/dev/sda3` block device, then filter the results for lines containing the text `This is a test!`, which was present in the file created earlier.



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
			
						


