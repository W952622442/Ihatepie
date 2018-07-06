# Ihatepie
This plugin can find address automatic （include libc and main program address when you use gdb to attach something）



HOW TO USE IT
   just add it in .gdbinit


br 0x111  to replace b *0x111
br l 0x111 to b at libc 

it may have bug but I just fix it when I want 
