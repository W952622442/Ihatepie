# Ihatepie
一个gdb的对于开了自动化的程序的自动定位插件，针对attach时开启随机化调试或者关掉随机化导致glibc地址错乱的情况，另外也支持对于libc的地址计算。

##如何使用
   添加插件进入 .gdbinit

##例子
 对于主程序
   使用 br 0x111  替代 b *0x111
 对于libc：
   使用 br l 0x111  断点 libc  的0x111地址

