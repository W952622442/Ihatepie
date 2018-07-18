#!/bin/bash
if ! hash gdb; then
	echo 'Could not find gdb in $PATH'
	exit
fi
# Load Pwndbg into GDB on every launch.
if ! grep Ihatepie ~/.gdbinit &>/dev/null; then
	    echo "source $PWD/gdbinit.py" >> ~/.gdbinit;
fi
exit
