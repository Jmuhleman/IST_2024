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

     We can list its metadata (using a long listing format) with the following command:

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



## TASK 2: PREPARE AND PARTITION A DISK

1. > Before you plug in the disk, list the existing block devices. Using the `findmnt` command find all the partitions that are already mounted.
   >
   > - In `findmnt`'s output you will see many pseudo file systems. You can suppress them with the `--real` option.

   The `findmnt` command allow us to list all mounted filesystems. Using the `--real` option, we only print the real filesystems. In our case, those are the result :

   ```bash
   $ findmnt --real
   TARGET                                   SOURCE                         FSTYPE      OPTIONS
   /                                        /dev/sda3                      ext4        rw,relatime,errors=remount-ro
   ├─/run/user/128/doc                      portal                         fuse.portal rw,nosuid,nodev,relatime,user_id=128,group_id=134
   ├─/run/user/1000/doc                     portal                         fuse.portal rw,nosuid,nodev,relatime,user_id=1000,group_id=1000
   ├─/snap/bare/5                           /dev/loop0                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/core20/1974                      /dev/loop1                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/core20/2182                      /dev/loop2                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/core22/858                       /dev/loop3                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/firefox/2987                     /dev/loop5                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/firefox/3836                     /dev/loop4                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/gnome-42-2204/120                /dev/loop6                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/gnome-42-2204/141                /dev/loop7                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/var/snap/firefox/common/host-hunspell /dev/sda3[/usr/share/hunspell] ext4        ro,noexec,noatime,errors=remount-ro
   ├─/snap/snapd/19457                      /dev/loop9                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/snapd-desktop-integration/83     /dev/loop11                    squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/gnome-3-38-2004/143              /dev/loop8                     squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/gtk-common-themes/1535           /dev/loop12                    squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/snap-store/959                   /dev/loop10                    squashfs    ro,nodev,relatime,errors=continue,threads=single
   ├─/snap/snapd/20671                      /dev/loop13                    squashfs    ro,nodev,relatime,errors=continue,threads=single
   └─/boot/efi                              /dev/sda2                      vfat        rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro
   ```

   

2. > Attach the disk to your computer.
   >
   > List again the block devices. Which new block devices and special files appeared? These represent the disk and its partitions you just attached.

   When we connected the disk to the VM, it did not appear in the output of the command `findmnt`. This is normal, as we didn't made any partition for now. However, we can see that the disk is correctly detected using the `lsblk` command. Two new lines will show with the disk informations :

   ```
   sdb      8:16   1 117.2G  0 disk
   └─sdb1   8:17   1 117.2G  0 part
   ```
   
   
   
   
   
3. > Create a partition table on the disk and create two partitions of equal size using the `parted` tool.
   >
   > You can consult [Gentoo Linux Documentation -- Preparing the Disks](https://www.gentoo.org/doc/en/handbook/handbook-amd64.xml?part=1&chap=4) as a reference on how to use `parted`.
   >
   > - Using superuser privileges invoke `parted` with a single parameter which is the special file representing the disk. Be careful not to confuse the special file for the disk (ending in a letter) and for the partitions (ending in a number).

   We used the command `sudo parted /dev/sdb`.

   

   > - Display the existing partitions with the `print` command. If the disk is completely blank you will get an error message about a missing disk label.

   As the USB disk was previously formatted in Windows, we can see that a primary partition already exists.

   ```bash
   (parted) print
   Model: SMI USB DISK (scsi)
   Disk /dev/sdb: 126GB
   Sector size (logical/physical): 512B/512B
   Partition Table: msdos
   Disk Flags:
   
   Number  Start   End    Size   Type     File system  Flags
    1      1049kB  126GB  126GB  primary
   ```

   

   > - Use the `mktable` command to create a partition table (overwriting any existing one). It should have Master Boot Record (MBR) layout (i.e. label type `msdos`).

   We used the command `mktable msdos` in the `parted` tool. Printing the information of the disk after creating the partition table, we can now see the newly created one, without any entries.

   
   
   > - Display the free space with the command `print free` (roughly the size of the disk minus some overhead). Write the value down.
   
   ```
   (parted) print free
   Model: SMI USB DISK (scsi)
   Disk /dev/sdb: 126GB
   Sector size (logical/physical): 512B/512B
   Partition Table: msdos
   Disk Flags:
   
   Number  Start  End    Size   Type  File system  Flags
           1024B  126GB  126GB        Free Space
   
   ```
   
   Note that the free space starts at the same bytes as our old partition.
   
   
   
   > - Use the `mkpart` command to create the partitions.
   >   - The first partition will be a primary partition, have a file system type of `fat32`, start at 0 and end at about half the free space.
   >   - The second partition will be a primary partition, have a file system type of `ext4`, start at half the free space, end at the free space.
   
   We created the partitions with the two following command : `mkpart primary fat32 0 63GB` for the first partition and `mkpart primary ext4 63GB -1`.  Note that the first command alerts us that *"The resulting partition is not properly aligned for best performance"*. This is due to the partition not starting at 0, as we can see it if we print the informations again :
   
   ```
   (parted) print
   Model: SMI USB DISK (scsi)
   Disk /dev/sdb: 126GB
   Sector size (logical/physical): 512B/512B
   Partition Table: msdos
   Disk Flags:
   
   Number  Start   End     Size    Type     File system  Flags
    1      512B    63.0GB  63.0GB  primary  fat32        lba
    2      63.0GB  126GB   62.8GB  primary  ext4         lba
   ```
   
   The `lba` flag is due to the msdos partition table and tell the systems to use linear (LBA) mode, as said in the documentation.
   
   
   
   > - Quit parted and verify that there are now two special files in `/dev` that correspond to the two partitions.
   
   We can check this with the `ls /dev` command and we can see that there are two special files named `sdb1` and `sdb2` corresponding to our newly created partitions.
   
   
   
4. > Format the two partitions using the `mkfs` command.
   >
   > - The first partition should have the file system type `vfat`.
   > - The second partition should have the file system type `ext4`.

   To format the two partitions, we used the following commands `sudo mkfs vfat /dev/sdb1` for the first partition and `sudo mkfs ext4 /dev/sdb2` for the second partition.

   We can double check that it worked by using the command `findmnt --real` again. We now can see the two entries corresponding to our new partitions

   

5. > Create two empty directories in the `/mnt` directory as mount points, called `part1` and `part2`. Mount the newly created file systems in these directories.

   We created the two directories simultaneously with the command :

   ```bash
   $ sudo mkdir /mnt/part1 /mnt/part2
   ```

   To make sure that the two folders were created correctly, we checked them with `ls`:

   ``` bash
   $ ls /mnt
   part1  part2
   ```

   We then mounted the partitions in these directories using the appropriate commands:

   ```bash
   $ sudo mount /dev/sdb1 /mnt/part1
   $ sudo mount /dev/sdb2 /mnt/part2
   ```

   Using the `lsblk ` command, we can check that the mount are correct. We can now see the following lines :

   ```bash
   sdb      8:16   1 117.2G  0 disk
   ├─sdb1   8:17   1  58.7G  0 part /mnt/part1
   └─sdb2   8:18   1  58.5G  0 part /mnt/part2
   ```

   We could also see them with the `findmnt --real` command, as the following lines are now visible:

   ```
   TARGET                                   SOURCE                         FSTYPE      OPTIONS
   ...
   ├─/mnt/part1                             /dev/sdb1                      vfat        rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro
   └─/mnt/part2                             /dev/sdb2                      ext4        rw,relatime
   ```

   

6. > How much free space is available on these filesystems? Use the `df` command to find out. What does the `-h` option do?

   The `df` command allows us to display the space available on all currently mounted file systems. The `-h` option will print sizes in powers of 1024 instead of the number of 1K blocks.

   ```bash
   $ df -h
   Filesystem      Size  Used Avail Use% Mounted on
   tmpfs           388M  2.0M  386M   1% /run
   /dev/sda3        20G   12G  6.4G  65% /
   tmpfs           1.9G     0  1.9G   0% /dev/shm
   tmpfs           5.0M  4.0K  5.0M   1% /run/lock
   /dev/sda2       512M  6.1M  506M   2% /boot/efi
   tmpfs           388M   76K  387M   1% /run/user/128
   tmpfs           388M   68K  387M   1% /run/user/1000
   /dev/sdb1        59G   32K   59G   1% /mnt/part1
   /dev/sdb2        58G   24K   55G   1% /mnt/part2
   ```

   Looking at the last two lines, which correspond to the directories we've just mounted, we can see that both still have 99% of the space available. We can see that the second partition has less space because some of it is used for the file system.

​	

## TASK 3: EXPLORE THE FILE SYSTEM SUPPORT IN THE KERNEL

1. > Find out which file systems the kernel supports right now. The kernel makes information about itself available to userspace programs in a pseudo file system that is mounted at `/proc`. The files in that file system describe kernel objects.
   >
   > - List the content of `/proc`. What is the version of the kernel in `/proc/version`?

   By listing the content with `ls /proc` we can see a lot of folders with numbers as name.

   ```bash
   $ ls /proc
   1     1325  1643  201   27   593  837            keys		
   103   1329  1675  202   278  596  84             key-users
   1035  1336  1678  203   279  6    85             kmsg
   1039  1338  1688  204   29   60   86             kpagecgroup
   1042  1342  1693  205   3    61   87             kpagecount
   1043  1346  1697  206   31   62   88             kpageflags
   1049  1362  17    207   318  63   880            loadavg
   105   14    1702  208   32   64   887            locks
   1052  1401  1706  209   34   65   89             mdstat
   1065  1412  1723  21    347  66   894            meminfo
   1067  1459  1725  210   35   67   909            misc
   1079  1472  174   211   355  68   911            modules
   109   1485  175   2110  358  69   93             mounts
   1094  1492  176   2111  36   695  931            mpt
   11    1495  1766  2112  369  697  932            mtrr
   1105  15    177   212   37   70   94             net
   1120  1501  178   213   38   706  95             pagetypeinfo
   1171  1513  179   214   39   708  960            partitions
   1177  1519  1790  215   4    71   969            pressure
   1188  1522  18    216   40   710  975            schedstat
   1199  1523  180   217   41   714  acpi           scsi
   12    1529  1805  2176  42   72   asound         self
   1228  153   181   218   43   727  bootconfig     slabinfo
   1233  1530  182   2184  44   73   buddyinfo      softirqs
   1237  1531  183   219   45   731  bus            stat
   1239  1532  184   2190  46   733  cgroups        swaps
   1244  1534  185   22    48   736  cmdline        sys
   1248  154   186   220   485  74   consoles       sysrq-trigger
   1253  155   187   221   486  740  cpuinfo        sysvipc
   1257  156   188   222   49   75   crypto         thread-self
   1264  1565  189   223   5    757  devices        timer_list
   1266  157   19    2236  50   759  diskstats      tty
   1273  1572  190   2237  51   76   dma            uptime
   1282  1579  191   2238  52   77   driver         version
   1289  158   192   2248  53   773  dynamic_debug  version_signature
   1295  159   193   2256  54   78   execdomains    vmallocinfo
   1296  16    194   2260  55   785  fb             vmstat
   13    160   195   2263  56   787  filesystems    zoneinfo
   1304  1608  196   2267  57   79   fs
   1308  161   197   2278  574  8    interrupts
   1311  162   198   23    575  80   iomem
   1317  1621  199   245   577  81   ioports
   1318  163   2     250   579  819  irq
   1320  1637  20    251   58   82   kallsyms
   1321  164   200   26    59   83   kcore
   ```

   We can check the version of the kernel as follows :

   ```bash
   $ cat /proc/version
   Linux version 6.5.0-21-generic (buildd@lcy02-amd64-091) (x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #21~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Feb  9 13:32:52 UTC 2
   ```

   

   - > The directories with numbers represent the running processes. The numbers are the process ids. Display the process id of your bash session with `echo $$`. List the information in the corresponding directory. What was the command line that started this process (look in `cmdline`)?

     ```bash
     $ echo $$
     2291
     $ ls /proc/2291
     arch_status         fd                 net            setgroups
     attr                fdinfo             ns             smaps
     autogroup           gid_map            numa_maps      smaps_rollup
     auxv                io                 oom_adj        stack
     cgroup              ksm_merging_pages  oom_score      stat
     clear_refs          ksm_stat           oom_score_adj  statm
     cmdline             limits             pagemap        status
     comm                loginuid           patch_state    syscall
     coredump_filter     map_files          personality    task
     cpu_resctrl_groups  maps               projid_map     timens_offsets
     cpuset              mem                root           timers
     cwd                 mountinfo          sched          timerslack_ns
     environ             mounts             schedstat      uid_map
     exe                 mountstats         sessionid      wchan
     ```

     We can see the command line that started this process in the `cmdline` file. Reading it, we see that the process was started by `bash` .

     

   - > The kernel lists the file systems it supports right now file `filesystems`. List them.

     ```bash
     $ cat /proc/filesystems
     nodev   sysfs
     nodev   tmpfs
     nodev   bdev
     nodev   proc
     nodev   cgroup
     nodev   cgroup2
     nodev   cpuset
     nodev   devtmpfs
     nodev   configfs
     nodev   debugfs
     nodev   tracefs
     nodev   securityfs
     nodev   sockfs
     nodev   bpf
     nodev   pipefs
     nodev   ramfs
     nodev   hugetlbfs
     nodev   devpts
             ext3
             ext2
             ext4
             squashfs
             vfat
     nodev   ecryptfs
             fuseblk
     nodev   fuse
     nodev   fusectl
     nodev   efivarfs
     nodev   mqueue
     nodev   pstore
     nodev   autofs
     nodev   binfmt_misc
     ```

     

   - > Can you find the `proc` filesystem itself in the list? How is it tagged? All file systems with that tag are pseudo file systems.

     By reading the results, we can find the line `proc` filesystem, tagged with `nodev`, as all other pseudo file sytems.

     

   - > List the real (non-pseudo) file systems.

     ```bash
     $ cat /proc/filesystems | grep -v 'nodev'
             ext3
             ext2
             ext4
             squashfs
             vfat
             fuseblk
     ```

     

2. > Find out which file systems the kernel is able to support by looking at the available kernel modules. The files containing kernel modules can be found at `lib/modules/<kernel version>/kernel/fs`. List them.

   ```bash
   $ ls /lib/modules/6.5.0-21-generic/kernel/fs/
   9p              ceph      fscache  minix       omfs       sysv
   adfs            coda      fuse     netfs       orangefs   ubifs
   affs            cramfs    gfs2     nfs         overlayfs  udf
   afs             dlm       hfs      nfs_common  pstore     ufs
   autofs          efs       hfsplus  nfsd        qnx4       vboxsf
   befs            erofs     hpfs     nilfs2      qnx6       xfs
   bfs             exfat     isofs    nls         quota      zonefs
   binfmt_misc.ko  f2fs      jffs2    ntfs        reiserfs
   btrfs           fat       jfs      ntfs3       romfs
   cachefiles      freevxfs  lockd    ocfs2       smb
   ```

   

3. > When a new disk is inserted the kernel knows which file system to activate by looking at a label that indicates the type of file system. That label is part of the partition metadata (called *signature*). Use the `blkid` command to list the metadata of all known partitions (mounted or not). Note that you might need to run the command with admin permissions to display all partitions metadata.
   >
   > - Verify that the partitions you created are labeled correctly.
   > - There is another piece of information in the partition metadata. What does it do?

   Using the `blkid` command, we listed the metadata of the known partitions. We found the lines corresponding to our partitions, with the `TYPE` label as expected:

   ```bash
   /dev/sdb2: UUID="9fca0610-608c-4ceb-9d32-6799fc6718c6" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="80480d50-02"
   /dev/sdb1: UUID="86C3-DB21" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="80480d50-01"
   ```

   We can see the `UUID` and `PARTUUID`. We also have the `BLOCK_SIZE` information which shows us the size of the block used in the partitions.

   

4. > An older way for the kernel to find out which file system to activate is the file `/etc/fstab`. This file lists all the file systems that should be mounted when the system boots. It indicates the special file that represents the partition, the directory where it should be mounted (the *mount point*), and the file system to activate.
   >
   > - List the content of `/etc/fstab`. What line is responsible for mounting the root (/) file system? This line has a particular way of referencing the partition, how?

   ```bash
   $ cat /etc/fstab
   # /etc/fstab: static file system information.
   #
   # Use 'blkid' to print the universally unique identifier for a
   # device; this may be used with UUID= as a more robust way to name devices
   # that works even if disks are added and removed. See fstab(5).
   #
   # <file system> <mount point>   <type>  <options>       <dump>  <pass>
   # / was on /dev/sda3 during installation
   UUID=76beeedf-f81c-4ecb-8fc3-090814c01177 /               ext4    errors=remount-ro 0       1
   # /boot/efi was on /dev/sda2 during installation
   UUID=3D7D-1890  /boot/efi       vfat    umask=0077      0       1
   /swapfile                                 none            swap    sw              0       0
   /dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0
   ```

   The first uncommented line is the one responsible for mounting the root filesystem, referring to the partition by its `UUID' instead of its name.



## TASK 4: MANAGE AN EXT4 PARTITION

1. > Unmount the ext4 partition on the external disk.

```bash
sudo umount /dev/sdb2
```

2. > Run a file system check using the fsck command.
```bash

fsck /dev/sdb2
```

4. > Display the file system structure with the dumpe2fs command. How many inodes are unused?
```bash
sudo dumpe2fs -h /dev/sdb2
```

The following line informs us about the # of Inodes available.
```bash Free inodes: 10981```


5. > Intentionally corrupt the file system by overwriting 4 MB of data, starting 10 kB in:
   
```bash
 
sudo dd if=/dev/zero of=/dev/sdb2 bs=1k seek=10 count=4k
```
6. > Try to mount the partition. You should get an error message. Repair the file system with the fsck 	command.

Try to mount the partition.
```bash
sudo mount /dev//sdb2 /mnt/part2
```

output:
```bash
mount: /mnt/part2: wrong fs type, bad option, bad superblock on /dev/sdb2, missing codepage or helper program, or other error.
```

We perform the fix on the FS with:
```bash
sudo fsck /dev/sdb2
```

7. > Mount the repaired partition.
```bash
sudo mount /dev/sdb2 /mnt/part2
```

## TASK 5: CREATE A FILE SYSTEM IN A FILE

2. > Find the next available loopback device:

```bash
losetup -f
```
output:
```bash
/dev/loop10
```
3. > Associate the loopback device with the file:

```bash
 sudo losetup /dev/loop10 /tmp/bigfile
```

4. > Verify that the association is OK:

```bash
/dev/loop9: []: (/var/lib/snapd/snaps/gtk-common-themes_1535.snap)
/dev/loop7: []: (/var/lib/snapd/snaps/snap-store_959.snap)
/dev/loop10: []: (/tmp/bigfile)
/dev/loop5: []: (/var/lib/snapd/snaps/core20_2182.snap)
/dev/loop12: []: (/var/lib/snapd/snaps/firefox_3836.snap)
```
We can see the loop10 associated with our 'bigfile'

5. > Create an ext4 file system on block device /dev/loop6. Create a mountpoint in /mnt/bigfile. Mount the file system on the mountpoint. How does findmnt show the new file system?
```bash
sudo parted /dev/loop10
mkfs msdos

mkpart
	primary
	ext4
	0
	100

sudo mkfs -t ext4 /dev/loop10
sudo mkdir /mnt/bigfile
sudo mount /dev/loop10 /mnt/bigfile
```
The bigfile is seen as:

```bash
findmnt --real
			└─/mnt/bigfile                       /dev/loop10 ext4       rw,relatime
```		
6. > Create a few files in the file system with unique strings. By searching the content of bigfile, can you find the strings? Use the sync command to force the kernel to write buffered data to disk.

```bash
sudo echo 'I am a black cat' >> a
sync -d /dev/bigfile
sudo strings /dev/loop10 | grep 'I am a black cat'
```	
output:
```bash
I am a black cat
```
7. > Undo everything:

```bash
sudo umount /dev/loop10
sudo losetup -d /dev/loop6
losetup -a
```
output:
```bash
/dev/loop1: []: (/var/lib/snapd/snaps/gnome-3-38-2004_143.snap)
/dev/loop8: []: (/var/lib/snapd/snaps/core22_858.snap)
/dev/loop6: []: (/var/lib/snapd/snaps/snapd_19457.snap)
/dev/loop13: []: (/var/lib/snapd/snaps/gnome-42-2204_141.snap)
/dev/loop4: []: (/var/lib/snapd/snaps/firefox_2987.snap)
/dev/loop11: []: (/var/lib/snapd/snaps/snapd-desktop-integration_83.snap)
/dev/loop2: []: (/var/lib/snapd/snaps/core20_1974.snap)
/dev/loop0: []: (/var/lib/snapd/snaps/bare_5.snap)
/dev/loop9: []: (/var/lib/snapd/snaps/gtk-common-themes_1535.snap)
/dev/loop7: []: (/var/lib/snapd/snaps/snap-store_959.snap)
/dev/loop5: []: (/var/lib/snapd/snaps/core20_2182.snap)
/dev/loop12: []: (/var/lib/snapd/snaps/firefox_3836.snap)
/dev/loop3: []: (/var/lib/snapd/snaps/gnome-42-2204_120.snap)
```
We can see there is no more loop10



