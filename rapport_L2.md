# IST Lab 02 : LOGICAL VOLUMES AND SNAPSHOTS

Authors : Butty Vicky & Mühlemann Julien

Group : L01GrA

Date : 07.03.2024

## TASK 1: CREATE PHYSICAL VOLUMES

1. > Reset your external disk. Using `parted` remove all partitions, or simply write a new partition table.

```bash
$ sudo parted /dev/sdb
$ mktable
msdos


2. > Create four partitions with these characteristics: primary, 25 MB size, type `ext4`.

```bash
$ mkpart primary 0 50 ext4
quit
$ sudo mkfs -t ext4 /dev/sdb1 ../dev/sdbn .../dev/sdb4 
```


3. > List the available LVM commands. They belong to the Debian package *lvm2* which should already be installed. Use `dpkg` with the `-L` option to list the content of the package. The commands are all located in the `/sbin` directory. Use `grep` to filter and `sort` to sort alphabetically.

The command typed is as follows:
```bash
$ sudo dpkg -L lvm2 | grep /sbin/
/sbin/fsadm
/sbin/lvm
/sbin/lvmdump
/sbin/lvmpolld
/sbin/lvchange
/sbin/lvconvert
/sbin/lvcreate
/sbin/lvdisplay
/sbin/lvextend
/sbin/lvmconfig
/sbin/lvmdiskscan
/sbin/lvmsadc
/sbin/lvmsar
/sbin/lvreduce
/sbin/lvremove
/sbin/lvrename
/sbin/lvresize
/sbin/lvs
/sbin/lvscan
/sbin/pvchange
/sbin/pvck
/sbin/pvcreate
/sbin/pvdisplay
/sbin/pvmove
/sbin/pvremove
/sbin/pvresize
/sbin/pvs
/sbin/pvscan
/sbin/vgcfgbackup
/sbin/vgcfgrestore
/sbin/vgchange
/sbin/vgck
/sbin/vgconvert
/sbin/vgcreate
/sbin/vgdisplay
/sbin/vgexport
/sbin/vgextend
/sbin/vgimport
/sbin/vgimportclone
/sbin/vgmerge
/sbin/vgmknodes
/sbin/vgreduce
/sbin/vgremove
/sbin/vgrename
/sbin/vgs
/sbin/vgscan
/sbin/vgsplit
```

4. > List all partitions that could potentially host a Physical Volume by using `pvs` with the `--all` option.
```bash
$ sudo pvs --all
  PV          VG Fmt Attr PSize PFree
  /dev/loop0         ---     0     0
  /dev/loop1         ---     0     0
  /dev/loop10        ---     0     0
  /dev/loop11        ---     0     0
  /dev/loop12        ---     0     0
  /dev/loop14        ---     0     0
  /dev/loop3         ---     0     0
  /dev/loop4         ---     0     0
  /dev/loop5         ---     0     0
  /dev/loop6         ---     0     0
  /dev/loop7         ---     0     0
  /dev/loop8         ---     0     0
  /dev/loop9         ---     0     0
  /dev/sda2          ---     0     0
  /dev/sda3          ---     0     0
  /dev/sdb1          ---     0     0
  /dev/sdb2          ---     0     0
  /dev/sdb3          ---     0     0
  /dev/sdb4          ---     0     0
  ```


5. > On the four partitions of your external disk, create four Physical Volumes using `pvcreate`. Add the `-vv` option so that it tells you in detail what it is doing. For the first partition copy the output of the command into the report, but copy only the lines about the partition that receives the Physical Volume and ignore the other messages.

   
```bash
$ sudo pvcreate /dev/sdb1 -vv

Device /dev/sdb1: queue/minimum_io_size is 512 bytes.
Device /dev/sdb1: queue/optimal_io_size is 0 bytes.
Device /dev/sdb1: alignment_offset is 0 bytes.
Set up physical volume for "/dev/sdb1" with 48828 available sectors.
Scanning for labels to wipe from /dev/sdb1
Zeroing start of device /dev/sdb1.
Writing physical volume data to disk "/dev/sdb1".
/dev/sdb1: Writing label to sector 1 with stored offset 32.
Physical volume "/dev/sdb1" successfully created.
Unlocking /run/lock/lvm/P_global
```
   

6. > Display detailed information about the first Physical Volume using `pvdisplay`.

```bash
$ sudo pvdisplay
"/dev/sdb1" is a new physical volume of "23.84 MiB"
--- NEW Physical volume ---
PV Name               /dev/sdb1
VG Name
PV Size               23.84 MiB
Allocatable           NO
PE Size               0
Total PE              0
Free PE               0
Allocated PE          0
PV UUID               oBLk2i-Ldz4-4nQB-gHcq-LeAr-wZHh-GuzHwZ

"/dev/sdb2" is a new physical volume of "24.00 MiB"
--- NEW Physical volume ---
PV Name               /dev/sdb2
VG Name
PV Size               24.00 MiB
Allocatable           NO
PE Size               0
Total PE              0
Free PE               0
Allocated PE          0
PV UUID               6x0yEs-yqCa-4gwf-Kpfu-hi0s-iHgL-guXz42

"/dev/sdb3" is a new physical volume of "24.00 MiB"
--- NEW Physical volume ---
PV Name               /dev/sdb3
VG Name
PV Size               24.00 MiB
Allocatable           NO
PE Size               0
Total PE              0
Free PE               0
Allocated PE          0
PV UUID               S4cGfQ-oZBH-6UdG-dxBC-MLWf-ZCOx-RJ2BVd

"/dev/sdb4" is a new physical volume of "23.00 MiB"
--- NEW Physical volume ---
PV Name               /dev/sdb4
VG Name
PV Size               23.00 MiB
Allocatable           NO
PE Size               0
Total PE              0
Free PE               0
Allocated PE          0
PV UUID               Lh92a0-XbGT-lEkm-ZhhN-mynE-g6Kt-XbtL07
```
   


## TASK 2: CREATE TWO VOLUME GROUPS

1. > Create a first Volume Group `lab-vg1` that contains only the first Physical Volume. Display the Physical Volume again with `pvdisplay`. What has changed?

```bash
$ sudo vgcreate lab-vg1 /dev/sdb1
Volume group "lab-vg1" successfully created
```

The name of the Volume group has been set to lab-vg1, it is now allocatable and we can see the physical extent size of 4 MB its total and free space.
```bash
  PV Name               /dev/sdb1
  VG Name               lab-vg1
  PV Size               23.84 MiB / not usable 3.84 MiB
  Allocatable           yes
  PE Size               4.00 MiB
  Total PE              5
  Free PE               5
```

2. > Create a second Volume Group `lab-vg2` that contains Physical Volumes 2 and 3.

```bash
$ sudo vgcreate lab-vg2 /dev/sdb2 /dev/sdb3
  Volume group "lab-vg2" successfully created
```
   

3. > List all Volume Groups with `vgs`. Then list all Physical Volumes with `pvs`. What do you see?

```bash
$ sudo vgs
  VG      #PV #LV #SN Attr   VSize  VFree
  lab-vg1   1   0   0 wz--n- 20.00m 20.00m
  lab-vg2   2   0   0 wz--n- 40.00m 40.00m
```

```bash
$ sudo pvs
  PV         VG      Fmt  Attr PSize  PFree
  /dev/sdb1  lab-vg1 lvm2 a--  20.00m 20.00m
  /dev/sdb2  lab-vg2 lvm2 a--  20.00m 20.00m
  /dev/sdb3  lab-vg2 lvm2 a--  20.00m 20.00m
  /dev/sdb4          lvm2 ---  23.00m 23.00m
```


## TASK 3: CREATE LOGICAL VOLUMES

1. > On the Volume Group `lab-vg1` create a Logical Volume of size 20 MB with the command `lvcreate -L 20M lab-vg1`.

```bash
$ sudo lvcreate -L 20M lab-vg1
  Logical volume "lvol0" created.
```


2. > Verify hat the new volume appears when you use `lvs` to list Logical Volumes. Also verify that it appears when you use `lsblk` to list the block devices. What is the name of the special file in `/dev` that represents the volume?

```bash
$ sudo lvs
  LV    VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lvol0 lab-vg1 -wi-a----- 20.00m
```

```bash
sdb                  8:16   0   100M  0 disk
├─sdb1               8:17   0  23.8M  0 part
│ └─lab--vg1-lvol0 252:0    0    20M  0 lvm
├─sdb2               8:18   0    24M  0 part
```

The name of the file in dev /dev/mapper/lab--vg1-lvol0 vol1/


3. > Create an ext4 file system on the volume. Mount the volume. Fill the file system with a 14 MB file using `dd` (Google it).

```bash
$ sudo mkfs -t ext4 /dev/mapper/lab--vg1-lvol0
```

```bash
$ sudo mount /dev/mapper/lab--vg1-lvol0 /mnt/vol1
``` 

```bash
$ sudo dd if=/dev/mapper/lab--vg1-lvol0 of=bigfile bs=1M count=14
```


4. > On the Volume Group `lab-vg2` create another Logical Volume of size 20 MB, create an ext4 file system on it and mount it. Create a file named `foo` that contains the text `111`.

   
```bash
$ sudo lvcreate -L 20M lab-vg2
```
   
```bash
$ sudo mkfs -t ext4 /dev/mapper/lab--vg2-lvol0
 ```

```bash
$ sudo mount /dev/mapper/lab--vg2-lvol0 /mnt/vol2
```

```bash
$ sudo echo "111" | sudo tee foo
```
   

## TASK 4: GROW A FILE SYSTEM WHILE IT IS IN USE

1. > Verify that the file system is indeed full (use `df -h`).

```bash
/dev/mapper/lab--vg1-lvol0   15M   15M     0 100% /mnt/vol1
```
We can see the 100% which appears to be the free space.
   

2. > Verify that the Volume Group is full (use `vgs`).

   
```bash
  lab-vg1   1   1   0 wz--n- 20.00m     0
```
We can see '0' which is the available space.

3. > Extend the Volume group using `vgextend` and verify with `vgs`.


```bash
$ sudo vgextend lab-vg1 /dev/sdb4
```

4. > Extend the Logical Volume by an additional 20 MB using `lvextend --size <new_size> <volume_group>/<logical_volume>`.

```bash
$ sudo lvextend -L +20M /dev/lab-vg1/lvol0
```
We get now both lab-vg1 and lab-vg2 having 40MB capacity. 
Capacity has been extended on the logical level. We now need to resize the file system with resize2fs   

5. > Grow the file system while it is mounted using `resize2fs` and verify its new capacity with `df -h`. Note: not all file systems support growing while being mounted. In that case you have to stop all applications using the file system, unmount, grow, remount, and restart the applications.

   
```bash
$ sudo resize2fs /dev/lab-vg1/lvol0
```
```bash
$ df -h
   LV    VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lvol0 lab-vg1 -wi-a----- 40.00m
  lvol0 lab-vg2 -wi-ao---- 40.00m
```  

   

## TASK 5: CREATE A SNAPSHOT

1. > Create a snapshot volume using the `--snapshot` option of `lvcreate`. Use the `--name` option to give it the name `snap`. You also need to specify a size for the snapshot with the `--size` option. Remember that initially a snapshot does not consume any storage blocks as the data in the original volume and the snapshot volume is identical. It is only when the data in the two volumes starts deviating that storage blocks are needed. The size of the snapshot determines how many data blocks can be different.
   >
   > To make things interesting, specify a size less than the size of the original volume.
   >
   > Note that LVM snapshots are read/write by default.

```bash
$ sudo lvcreate --snapshot --name snap --size 10M /dev/lab-vg2/lvol0
  Rounding up size to full physical extent 12.00 MiB
  Logical volume "snap" created.
```   

   

2. > Display an overview of all Logical Volumes using `lvs`. Which column shows the name of the original volume?

```bash
$ sudo lvs
  LV    VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lvol0 lab-vg1 -wi-a----- 20.00m
  lvol0 lab-vg2 owi-aos--- 20.00m
  snap  lab-vg2 swi-a-s--- 12.00m      lvol0  0.10
```

   

3. > Display the charactersticts of the snapshot volume using `lvdisplay`.
   >
   > - What line shows the name of the original volume?
   > - What line shows the size of the original volume?
   > - What line shows the space allocated for the snapshot volume?
   > - What does COW stand for?


- the LV snapshot status line. It specifies that the snapshot logical volume (snap) serves as a destination for the original volume named lvol0.

- the LV Size line. It specifies the size of the logical volume lvol0, which is 20.00 MiB.

- the LV Size line. It specifies the size of the snapshot logical volume snap, which is also 20.00 MiB.

- COW stands for Copy-On-Write. COW refers to a technique where data changes are tracked by creating a copy of the original data only when it is modified 

 ```bash
     --- Logical volume ---
  LV Path                /dev/lab-vg2/snap
  LV Name                snap
  VG Name                lab-vg2
  LV UUID                hLyX2b-D254-Qxhm-OXg1-UpUW-bpgg-Uj1Zvq
  LV Write Access        read/write
  LV Creation host, time ubuntu-VirtualBox, 2024-03-17 11:16:43 +0100
  LV snapshot status     active destination for lvol0
  LV Status              available
  # open                 0
  LV Size                20.00 MiB
  Current LE             5
  COW-table size         12.00 MiB
  COW-table LE           3
  Allocated to snapshot  0.10%
  Snapshot chunk size    4.00 KiB
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           252:4
```
   

4. > Mount the snapshot volume. Using the file `foo` you created earlier verify that the two volumes behave like independent copies.

We modified the content of foo file. e.g: 
```bash
$ sudo echo "2" | sudo tee foo
```

We now have "2" in foo on the snap volume whereas we still have "111" in the lab-vg2 volume.
Therefore the volumes behaves independently.

   

5. > Make the data of the original volume change completely by using the `dd` command to write a new file of 14 MB size. Run `df -h` to see how it affects the fullness of the original volume and the snapshot. What do you see?

```bash
$ sudo dd if=/dev/mapper/lab--vg2-lvol0 of=new_file bs=1M count=14
14+0 records in
14+0 records out
14680064 bytes (15 MB, 14 MiB) copied, 2.11044 s, 7.0 MB/s
```
```bash
$ df -h
Filesystem                  Size  Used Avail Use% Mounted on
tmpfs                       507M  1.6M  506M   1% /run
/dev/sda3                    24G   12G   11G  53% /
tmpfs                       2.5G     0  2.5G   0% /dev/shm
tmpfs                       5.0M  4.0K  5.0M   1% /run/lock
/dev/sda2                   512M  6.1M  506M   2% /boot/efi
tmpfs                       507M   96K  507M   1% /run/user/1000
/dev/mapper/lab--vg2-lvol0   15M   15M     0 100% /mnt/vol2
/dev/mapper/lab--vg2-snap    15M   28K   14M   1% /mnt/snap
```
The volume lab-vg2 is now fully occupied.


   - > The way that you allocated it, is the snapshot volume able support a change of 14 MB of data?

No, it is not.

   - > What happened? Why?

    
     Albeit the snapshot does not initially consume space on disk, if we make a 14MB change on the snapshot  volume
     those 14MB will need 14MB of new extends (copy on write)
```bash
mount: /mnt/snap: can't read superblock on /dev/mapper/lab--vg2-snap.
```
     
     

6. > Remove the broken snapshot volume.

```bash
$ sudo lvremove /dev/lab-vg2/snap
```

7. > Redo the above, this time allocating sufficient space to the snapshot volume to support a complete change of data of the original volume.

```bash
$ sudo lvcreate --snapshot --name snap --size 20M /dev/lab-vg2/lvol0
```

We allocate 20MB for the snapshot 
   

### TASK 6: PROVISION A THIN VOLUME AND SNAPSHOT IT

1. > Remove all Logical Volumes from Volume Group `lab-vg2`.

```bash
$ sudo lvremove /dev/lab-vg2/*
```

   

2. > Follow the explanations in the Ubuntu manual on [lvmthin](https://manpages.ubuntu.com/manpages/bionic/en/man7/lvmthin.7.html) to create
   >
   > - a thin data Logical Volume called `pool0` of 28 MB
   > - a thin metadata Logical Volume called `pool0meta` of 4 MB
```bash
$ sudo lvcreate -n pool0 -L 28M lab-vg2
  Logical volume "pool0" created.
```

```bash
$ sudo lvcreate -n pool0meta -L 4M lab-vg2
  Logical volume "pool0meta" created.
```

3. > Combine the two into a thin pool Logical Volume. List the Logical Volumes using `lvs`. Use the `-a` option to list also the hidden ones.

```bash
$ sudo lvconvert --type thin-pool --poolmetadata lab-vg2/pool0meta lab-vg2/pool0
```

```bash
$ sudo lvs -a
  LV              VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  [lvol0_pmspare] lab-vg2 ewi-------  4.00m

  pool0           lab-vg2 twi-a-tz-- 28.00m             0.00   10.84

  [pool0_tdata]   lab-vg2 Twi-ao---- 28.00m

  [pool0_tmeta]   lab-vg2 ewi-ao----  4.00m
```
   

4. > Create a thin Logical Volume from the thin pool named `thin1` and give it a size of 80 MB, although the thin pool only has 28 MB capacity. What warnings to you see?

```bash
$ sudo lvcreate -n thin1 -V 80M --thinpool pool0 lab-vg2
  WARNING: Sum of all thin volume sizes (80.00 MiB) exceeds the size of thin pool lab-vg2/pool0 and the size of whole volume group (60.00 MiB).
  WARNING: You have not turned on protection against thin pools running out of space.
  WARNING: Set activation/thin_pool_autoextend_threshold below 100 to trigger automatic extension of thin pools before they get full.
  Logical volume "thin1" created.
```

We see a warning because as stated, the sum of the volumes is greater than the pool availability.
System informs us that we can turn up a protection against pools running out of space.

5. > Create an ext4 file system on `thin1`. Mount the file system. How much capacity does `df -h` see in the file system?

```bash
$ sudo mkfs -t ext4 /dev/mapper/lab--vg2-thin1
mke2fs 1.46.5 (30-Dec-2021)
Discarding device blocks: done
Creating filesystem with 20480 4k blocks and 20480 inodes
.
.
```

```bash
$ df -h
Filesystem                  Size  Used Avail Use% Mounted on
/dev/mapper/lab--vg2-thin1   71M   24K   66M   1% /mnt/vol2   
```
df sees the capacity at 71MB.

   

6. > Do experiments: Fill the file system with a bit of data by using `dd` to write files and verify that it behaves normally. Then write more and more data until you cross the size of the thin pool and see what happens. You can see LVM's log messages by using the `dmesg` command, they appear as `device-mapper`. What do you observe?


We filled up the volume with dd until the messages as below appears. The pool is not able anymore to provide space on the thin volume.
```bash
[14704.710624] device-mapper: thin: 252:2: reached low water mark for data device: sending event.
```



### TASK 7: SCENARIO

> You are a data engineer in a company. You need to set up the backup system for your production system, which runs a large database. Backups are important in case of unexpected incidents or human error. As the volume of data is significant, the backup process's duration can be fairly long, typically between 30 minutes and 1 hour.
>
> Designing a solution for this backup system using snapshots, knowing that:
>
> - The backup should be performed without interrupting the database operations.
>
> - The backup files need to be physically distant and sent to another datacenter located a few kilometers away.
>
> Describe a potential solution and explain your thought process.

Here is our solution:

1. We can first make a snapshot of the volume to be backed up. We can perform it on production so that the database does not need to be interrupted. (constraint #1 is complied)

2. We can send the data of the snapshot on a physically distant server so that we respect redundancy of the backup.(constraint # 2 filled).

3. We should implement an automatic backup at regular times. E.G. with a script on amazon S3. etc..
