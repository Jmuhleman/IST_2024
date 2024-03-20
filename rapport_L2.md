# IST Lab 02 : LOGICAL VOLUMES AND SNAPSHOTS

Authors : Butty Vicky & Mühlemann Julien

Group : L01GrA

Date : 07.03.2024

## TASK 1: CREATE PHYSICAL VOLUMES

1. > Reset your external disk. Using `parted` remove all partitions, or simply write a new partition table.

   For this, we use  `parted /dev/sdb` and use the `mktable msdos` to write a new partition table.

   

2. > Create four partitions with these characteristics: primary, 25 MB size, type `ext4`. 

   We used `parted`, with the command `mkpart` to create our partitions :

   -   `mkpart primary ext4 0 25MB`
   -   `mkpart primary ext4 25MB 50MB`
   -   `mkpart primary ext4 50MB 75MB`
   -  `mkpart primary ext4 75MB 101MB` . This last one goes to 101MB so we can have the same size as the other partitions.

We can then check our new partitions with `print` :

   ```bash
   (parted) print
   Model: VMware, VMware Virtual S (scsi)
   Disk /dev/sdb: 96.6GB
   Sector size (logical/physical): 512B/512B
   Partition Table: msdos
   Disk Flags:
   
   Number  Start   End     Size    Type     File system  Flags
    1      512B    25.0MB  25.0MB  primary  ext4         lba
    2      25.2MB  50.3MB  25.2MB  primary  ext4         lba
    3      50.3MB  75.5MB  25.2MB  primary  ext4         lba
    4      75.5MB  101MB   25.2MB  primary  ext4         lba
   ```

   

3. > List the available LVM commands. They belong to the Debian package *lvm2* which should already be installed. Use `dpkg` with the `-L` option to list the content of the package. The commands are all located in the `/sbin` directory. Use `grep` to filter and `sort` to sort alphabetically.

The command typed is as follows:

```bash
$ sudo dpkg -L lvm2 | grep /sbin/ | sort
/sbin/fsadm
/sbin/lvchange
/sbin/lvconvert
/sbin/lvcreate
/sbin/lvdisplay
/sbin/lvextend
/sbin/lvm
/sbin/lvmconfig
/sbin/lvmdiskscan
/sbin/lvmdump
/sbin/lvmpolld
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
     /dev/loop1         ---     0     0
     /dev/loop10        ---     0     0
     /dev/loop11        ---     0     0
     /dev/loop12        ---     0     0
     /dev/loop2         ---     0     0
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

   We can see that our new partitions are in this list and can therefore host a physical volume.

   

5. > On the four partitions of your external disk, create four Physical Volumes using `pvcreate`. Add the `-vv` option so that it tells you in detail what it is doing. For the first partition copy the output of the command into the report, but copy only the lines about the partition that receives the Physical Volume and ignore the other messages.

   We use the command `sudo pvcreate /dev/sdb1 -vv` and the  output lines about the partition are as follow :

   ```bash
     /dev/sdb1: size is 48828 sectors
     /dev/sdb1: using cached size 48828 sectors
     /dev/sdb1: No lvm label detected
     Wiping signatures on new PV /dev/sdb1.
     /dev/sdb1: using cached size 48828 sectors
     Device /dev/sdb1: queue/minimum_io_size is 512 bytes.
     Device /dev/sdb1: queue/optimal_io_size is 0 bytes.
     Device /dev/sdb1: alignment_offset is 0 bytes.
     Set up physical volume for "/dev/sdb1" with 48828 available sectors.
     Scanning for labels to wipe from /dev/sdb1
     Zeroing start of device /dev/sdb1.
     Writing physical volume data to disk "/dev/sdb1".
     /dev/sdb1: Writing label to sector 1 with stored offset 32.
     Physical volume "/dev/sdb1" successfully created.
   ```
   
   We then used the same command for the other partitions :
   
   - `sudo pvcreate /dev/sdb2 -vv` 
   - `sudo pvcreate /dev/sdb3 -vv` 
   - `sudo pvcreate /dev/sdb4 -vv`
   
   
   
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
     PV UUID               KrHps0-ZYx1-hdIL-VhuR-ts0d-xqVO-hh8wXH
   
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
     PV UUID               wfEL9K-3jYA-MB1c-coyG-Gfw5-Ujxb-8RlC2Z
   
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
     PV UUID               9ZRv4R-Xdd9-Bsep-hmBH-Ggsw-52X5-iM2Reo
   
     "/dev/sdb4" is a new physical volume of "24.00 MiB"
     --- NEW Physical volume ---
     PV Name               /dev/sdb4
     VG Name
     PV Size               24.00 MiB
     Allocatable           NO
     PE Size               0
     Total PE              0
     Free PE               0
     Allocated PE          0
     PV UUID               qlmG06-57Tl-ma4F-Yujl-yW2r-grj7-lLhexx
   ```
   
   
   

## TASK 2: CREATE TWO VOLUME GROUPS

1. > Create a first Volume Group `lab-vg1` that contains only the first Physical Volume. Display the Physical Volume again with `pvdisplay`. What has changed?

   The volume group was created with the command `sudo vgcreate lab-vg1 /dev/sdb1`.

   We can check that it worked with `pvdisplay`, as it now show us a VG Name and other new infos :

   ```bash
   $ sudo pvdisplay /dev/sdb1
     --- Physical volume ---
     PV Name               /dev/sdb1
     VG Name               lab-vg1
     PV Size               23.84 MiB / not usable 3.84 MiB
     Allocatable           yes
     PE Size               4.00 MiB
     Total PE              5
     Free PE               0
     Allocated PE          5
     PV UUID               KrHps0-ZYx1-hdIL-VhuR-ts0d-xqVO-hh8wXH
   ```

   

2. > Create a second Volume Group `lab-vg2` that contains Physical Volumes 2 and 3.

   The volume group was created with the command  `sudo vgcreate lab-vg2 /dev/sdb2 /dev/sdb3`

   

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
     /dev/sdb4          lvm2 ---  24.00m 24.00m
   ```
   
   The `vgs` command allows us to see information about our volume groups and let us know that our `lab-vg2` volume group consists of two physical volumes. The volume groups have write permission (w), are resizable (z), and have a normal (n) allocation policy, as shown in the `Attr` column.
   
   With the `pvs` command we show the details of the physical volumes and it allows us to see which of our physical volumes are grouped with which volume groups. The `Attr` column tells us that the first three physical volumes are assignable (a). These volumes also show only the usable size in the `PSize` column.
   
   

## TASK 3: CREATE LOGICAL VOLUMES

1. > On the Volume Group `lab-vg1` create a Logical Volume of size 20 MB with the command `lvcreate -L 20M lab-vg1`.

   We used the following command, as asked : `sudo lvcreate -L 20M lab-vg1` .

   

2. > Verify hat the new volume appears when you use `lvs` to list Logical Volumes. Also verify that it appears when you use `lsblk` to list the block devices. What is the name of the special file in `/dev` that represents the volume?

   Using the `lvs` command, we can see that our new logical volume exist with the correct size:

   ```bash
   $ sudo lvs
     LV    VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
     lvol0 lab-vg1 -wi-a----- 20.00m
   ```

   We can also see this logical volume by using the `lsblk` command :

   ```bash
   sdb                  8:16   0    90G  0 disk
   ├─sdb1               8:17   0  23.8M  0 part
   │ └─lab--vg1-lvol0 252:0    0    20M  0 lvm
   ├─sdb2               8:18   0    24M  0 part
   ├─sdb3               8:19   0    24M  0 part
   └─sdb4               8:20   0    24M  0 part
   sr0                 11:0    1 155.3M  0 rom
   sr1                 11:1    1   4.7G  0 rom
   ```

   The special file in dev is found at the path `/dev/lab-vg1/lvol0`. 

   **TODO : Is it correct ?**

   

3. > Create an ext4 file system on the volume. Mount the volume. Fill the file system with a 14 MB file using `dd` (Google it).

   We created the ext4 file system with `sudo mkfs.ext4 /dev/lab-vg1/lvol0`. We created the mount folder with `sudo mkdir /mnt/lvol0`. We then mouted the volume with the command `sudo mount /dev/lab-vg1/lvol0 /mnt/lvol0` and filed the file system with a zero filed file using `sudo dd if=/dev/zero of=/mnt/lvol0/bigfile bs=1M count=14`.

   We check then that our file was correctly created with :

   ```bash
   $ ls -lh /mnt/lvol0
   total 14M
   -rw-r--r-- 1 root root 14M Mär 20 16:39 bigfile
   ```

   

4. > On the Volume Group `lab-vg2` create another Logical Volume of size 20 MB, create an ext4 file system on it and mount it. Create a file named `foo` that contains the text `111`.

   We used the following commands :

   - `sudo lvcreate -L 20M lab-vg2` : Create the logical volume of 20MB
   - `sudo mkfs.ext4 /dev/lab-vg2/lvol0` : Create the file system
   - `sudo mkdir /mnt/lvol1` : Create the folder for the mount
   - `sudo mount /dev/lab-vg1/lvol0 /mnt/lvol0` : Mount the volume
   - `echo "111" | sudo tee /mnt/lvol1/foo` : Create the file `foo`
   
   We checked the file content with the command:
   
   ```bash
   $ cat /mnt/lvol1/foo
   111
   ```
   
   

## TASK 4: GROW A FILE SYSTEM WHILE IT IS IN USE

1. > Verify that the file system is indeed full (use `df -h`).

   Using the `df -h` we can see the following lines for our new file systems :

   ```bash
   Filesystem                  Size  Used Avail Use% Mounted on
   
   /dev/mapper/lab--vg1-lvol0   15M   15M     0 100% /mnt/lvol0
   /dev/mapper/lab--vg2-lvol0   15M   28K   14M   1% /mnt/lvol1
   ```

   We can see that the first file system is 100% full, and that the second has only a few K used.

   

2. > Verify that the Volume Group is full (use `vgs`).

   ```bash
   $ sudo vgs
     VG      #PV #LV #SN Attr   VSize  VFree
     lab-vg1   1   1   0 wz--n- 20.00m     0
     lab-vg2   2   1   0 wz--n- 40.00m 20.00m
   ```

   We can see that volume group `lab-vg1` has no free space left, and `lab-vg2` still has half of it's space left.

   

3. > Extend the Volume group using `vgextend` and verify with `vgs`.

   We extended the volume group with `sudo vgextend lab-vg1 /dev/sdb4` and checked it with :

   ```bash
   $ sudo vgs
     VG      #PV #LV #SN Attr   VSize  VFree
     lab-vg1   2   1   0 wz--n- 40.00m 20.00m
     lab-vg2   2   1   0 wz--n- 40.00m 20.00m
   ```

   The first volume group has now 20 MB of free space and consists of two physical volumes.

   

4. > Extend the Logical Volume by an additional 20 MB using `lvextend --size <new_size> <volume_group>/<logical_volume>`.

   For this, we used the command :

   ````bash
   $ sudo lvextend -L +20M /dev/lab-vg1/lvol0
     Size of logical volume lab-vg1/lvol0 changed from 20.00 MiB (5 extents) to 40.00 MiB (10 extents).
     Logical volume lab-vg1/lvol0 successfully resized.
   ````

   

5. > Grow the file system while it is mounted using `resize2fs` and verify its new capacity with `df -h`. Note: not all file systems support growing while being mounted. In that case you have to stop all applications using the file system, unmount, grow, remount, and restart the applications.

   ```bash
   $ sudo resize2fs /dev/lab-vg1/lvol0
   resize2fs 1.46.5 (30-Dec-2021)
   Filesystem at /dev/lab-vg1/lvol0 is mounted on /mnt/lvol0; on-line resizing required
   old_desc_blocks = 1, new_desc_blocks = 1
   The filesystem on /dev/lab-vg1/lvol0 is now 10240 (4k) blocks long.
   ```
   
   Using `df -h` command to check the new capacity of the file system :
   
   ```bash
   Filesystem                  Size  Used Avail Use% Mounted on
   
   /dev/mapper/lab--vg1-lvol0   35M   15M   20M  43% /mnt/lvol0
   /dev/mapper/lab--vg2-lvol0   15M   28K   14M   1% /mnt/lvol1
   ```
   
   

## TASK 5: CREATE A SNAPSHOT

1. > Create a snapshot volume using the `--snapshot` option of `lvcreate`. Use the `--name` option to give it the name `snap`. You also need to specify a size for the snapshot with the `--size` option. Remember that initially a snapshot does not consume any storage blocks as the data in the original volume and the snapshot volume is identical. It is only when the data in the two volumes starts deviating that storage blocks are needed. The size of the snapshot determines how many data blocks can be different.
   >
   > To make things interesting, specify a size less than the size of the original volume.
   >
   > Note that LVM snapshots are read/write by default.

   We made our snapshot of the second volume group with the command :

   ```bash
   $ sudo lvcreate --snapshot --name snap --size 10M /dev/lab-vg2/lvol0
     Rounding up size to full physical extent 12.00 MiB
     Logical volume "snap" created.
   ```
   
   The command rounded up the size to fit alignment requirements of the file system.
   
   
   
2. > Display an overview of all Logical Volumes using `lvs`. Which column shows the name of the original volume?

   ```bash
   $ sudo lvs
     LV    VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
     lvol0 lab-vg1 -wi-ao---- 40.00m
     lvol0 lab-vg2 owi-aos--- 20.00m
     snap  lab-vg2 swi-a-s--- 12.00m      lvol0  0.10
   ```

   The column `Origin` shows us the name of the original volume. The first bit in the `Attr`  column indicate the volume type, using `s` for a snapshot volume and `o` for an origin volume.

   

3. > Display the charactersticts of the snapshot volume using `lvdisplay`.
   
   ```bash
   $ sudo lvdisplay /dev/lab-vg2/snap
     --- Logical volume ---
     LV Path                /dev/lab-vg2/snap
     LV Name                snap
     VG Name                lab-vg2
     LV UUID                cWCIi6-sH2O-NAYg-r2lw-JLeR-upy3-k2R9tF
     LV Write Access        read/write
     LV Creation host, time IST, 2024-03-20 17:33:10 +0100
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
   
   
   
   > - What line shows the name of the original volume?
   
   We can see the name of the original volume in the `LV snapshot status` line. 
   
   
   
   > - What line shows the size of the original volume?
   
   The line `LV Size` .
   
   
   
   > - What line shows the space allocated for the snapshot volume?
   
   The line `COW-table size`.
   
   
   
   > - What does COW stand for?
   
   COW stand for Copy-On-Write, a resource-management technique where only the modified data are stored, by creating a copy of the original data.
   
   
   
4. > Mount the snapshot volume. Using the file `foo` you created earlier verify that the two volumes behave like independent copies.

   We mounted the snapshot with `sudo mount /dev/lab-vg2/snap /mnt/snap` after creating the folder with `sudo mkdir /mnt/snap`.  We then changed the contents of the `foo` file with the command `echo "222" | sudo tee /mnt/lvol1/foo`. Now the original file contains `222` and the snapshot should still contain `111`. We checked it like this:

   ```bash
   $ cat /mnt/lvol1/foo
   222
   $ cat /mnt/snap/foo
   111
   ```

   

5. > Make the data of the original volume change completely by using the `dd` command to write a new file of 14 MB size. Run `df -h` to see how it affects the fullness of the original volume and the snapshot. What do you see?

   We used the command `sudo dd if=/dev/zero of=/mnt/lvol1/new_bigfile bs=1M count=14` to create the new file. With `df -h` we can now see the new size of the volume, which is now full, and that the snapshot is missing :

   ``` bash
   $ df -h
   Filesystem                  Size  Used Avail Use% Mounted on
   
   /dev/mapper/lab--vg1-lvol0   35M   15M   20M  43% /mnt/lvol0
   /dev/mapper/lab--vg2-lvol0   15M   15M     0 100% /mnt/lvol1
   ```

   

   - > The way that you allocated it, is the snapshot volume able support a change of 14 MB of data?

     No, the snapshot is not able to support it.

     

   - > What happened? Why?

     Because we allocated 12 MB of space for the snapshot, it can only use that space. When the new 14MB file was created, the change could not be properly stored in the snapshot because it required 14MB of free space.

     We can also see that the snapshot is broken when we try to mount again the snapshot :
     
     ```
     $ sudo mount /dev/lab-vg2/snap /mnt/snap
     mount: /mnt/snap: can't read superblock on /dev/mapper/lab--vg2-snap.
     ```
     
     We can also see with  `lvdisplay` that the `LV snapshot status` is now `INACTIVE destination for lvol0`.
     
     

6. > Remove the broken snapshot volume.

   This can be done with the command `sudo lvremove /dev/lab-vg2/snap`.

   

7. > Redo the above, this time allocating sufficient space to the snapshot volume to support a complete change of data of the original volume.

   This time we allocated 20 MB for the snapshot. This time we removed the file created in step 5 with the command `rm /mnt/lvol1/new_bigfile` . With `df -h` we checked the size of the snapshot, which is obviously full, since it was a copy of the full volume :

   ```bash
   Filesystem                  Size  Used Avail Use% Mounted on
   
   /dev/mapper/lab--vg1-lvol0   35M   15M   20M  43% /mnt/lvol0
   /dev/mapper/lab--vg2-lvol0   15M   28K   14M   1% /mnt/lvol1
   /dev/mapper/lab--vg2-snap    15M   15M     0 100% /mnt/snap
   ```
   
   We then checked the files in the two volumes to make sure it was working properly :
   
   ```bash
   $ ls /mnt/lvol1
   foo  lost+found
   ls /mnt/snap/
   foo  lost+found  new_bigfile
   ```
   
   

### TASK 6: PROVISION A THIN VOLUME AND SNAPSHOT IT

1. > Remove all Logical Volumes from Volume Group `lab-vg2`.

   We removed them with `sudo lvremove /dev/lab-vg2/*`. Note that it may not be possible if the file systems are in use.

   

2. > Follow the explanations in the Ubuntu manual on [lvmthin](https://manpages.ubuntu.com/manpages/bionic/en/man7/lvmthin.7.html) to create
   >
   > - a thin data Logical Volume called `pool0` of 28 MB
   
   For this, we use the command `sudo lvcreate -n pool0 -L 28M lab-vg2`.
   
   > - a thin metadata Logical Volume called `pool0meta` of 4 MB
   
   This was made using the command `sudo lvcreate -n pool0meta -L 4M lab-vg2`. 
   
   
   
3. > Combine the two into a thin pool Logical Volume. List the Logical Volumes using `lvs`. Use the `-a` option to list also the hidden ones.

   We combined them using `sudo lvconvert --type thin-pool --poolmetadata lab-vg2/pool0meta lab-vg2/pool0`. We then used `lvs` to see the combined volume :

   ```bash
   $ sudo lvs -a
     LV              VG      Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
     lvol0           lab-vg1 -wi-a----- 40.00m
     [lvol0_pmspare] lab-vg2 ewi-------  4.00m
     pool0           lab-vg2 twi-a-tz-- 28.00m             0.00   10.84
     [pool0_tdata]   lab-vg2 Twi-ao---- 28.00m
     [pool0_tmeta]   lab-vg2 ewi-ao----  4.00m
   ```

   

4. > Create a thin Logical Volume from the thin pool named `thin1` and give it a size of 80 MB, although the thin pool only has 28 MB capacity. What warnings to you see?

   ```bash
   $ sudo lvcreate -n thin1 -V 80M --thinpool pool0 lab-vg2
     WARNING: Sum of all thin volume sizes (80.00 MiB) exceeds the size of thin pool lab-vg2/pool0 and the size of whole volume group (40.00 MiB).
     WARNING: You have not turned on protection against thin pools running out of space.
     WARNING: Set activation/thin_pool_autoextend_threshold below 100 to trigger automatic extension of thin pools before they get full.
     Logical volume "thin1" created.
   ```

   This warning informs us that the size of the new thin volume exceeds the size of our thin pool. A protection can be enabled if we don't want our thin pools to run out of space.

   

5. > Create an ext4 file system on `thin1`. Mount the file system. How much capacity does `df -h` see in the file system?

   We created the file system with `sudo mkfs -t ext4 /dev/lab-vg2/thin1` and mounted it with the command `sudo mount /dev/lab-vg2/thin1 /mnt/thin` in a previously created directory. With `df -h` we can see that our mount has a size of 71 MB and only 1% used.

   ```
   Filesystem                  Size  Used Avail Use% Mounted on
   
   /dev/mapper/lab--vg2-thin1   71M   24K   66M   1% /mnt/thin
   ```

   

6. > Do experiments: Fill the file system with a bit of data by using `dd` to write files and verify that it behaves normally. Then write more and more data until you cross the size of the thin pool and see what happens. You can see LVM's log messages by using the `dmesg` command, they appear as `device-mapper`. What do you observe?

   We filled the file system with `dd`. As soon as we reached the maximum size of the pool, the file created was smaller than the requested size and an error message was shown :

   ```bash
   $ sudo dd if=/dev/zero of=/mnt/thin/bigfile4 bs=1M count=20
   dd: error writing '/mnt/thin/bigfile4': No space left on device
   10+0 records in
   9+0 records out
   9781248 bytes (9.8 MB, 9.3 MiB) copied, 0.0232297 s, 421 MB/s
   ```
   
   We then looked at the LVM logs and saw the error messages:
   
   ```
   device-mapper: thin: 252:3: reached low water mark for data device: sending event.
   device-mapper: thin: 252:3: switching pool to out-of-data-space (queue IO) mode
   device-mapper: thin: 252:3: switching pool to out-of-data-space (error IO) mode
   ```
   
   We can see that a first warning was sent when we created our files and reached the low water mark. Then another was sent when we created the file that filled the remaining space in the pool. The last message was certainly sent when we tried to create a file again, even though we knew the pool was full.



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
