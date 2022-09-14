from system.machine import my_machine
from components import *


a = my_machine.file_system.rootfs["a"] = Directory(my_machine.file_system.rootfs)
b = a["b"] = Directory(a)
f = b["file"] = File(b)

my_machine.file_system.cd("./a/b")
print(my_machine.file_system.find_path("./file").owner)


my_machine.start_shell()