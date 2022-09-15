from components.directory import Directory
from components.file import File, QueryError
from system.machine import Machine


class Commands:
    def exit(self, machine: Machine, options: list):
        self.terminate = True
        print(f"bye, {machine.current_user.name}")

    def ls(self, machine: Machine, options: list):
        try:
            path = options[-1]
            path = machine.file_system.find_path(path)
        except QueryError:
            print("ls: No such file or directory")
            return
        except IndexError:
            path = machine.file_system.current_working_directory
        if type(path) is File:
            print(options[-1])
        elif type(path) is Directory:
            # if list_all:
            #    f = lambda x: x[0]
            # else:
            #    f = lambda x: x[0] and not x[0].startswith(".")
            # items = list(filter(f, path.content.items()))
            items = str.join(" ", filter(
                lambda x: x,
                list(map(lambda x: x[0], path.content.items())))
            )
            print(items)
    
    def cd(self, machine : Machine, options: list):
        if len(options) != 1:
            print("must provide only one path")
            return 
        path = options[-1]
        try:
            target = machine.file_system.find_path(path)
            if type(target) is Directory:
                machine.file_system.current_working_directory = target 
                return
            elif type(target) is File:
                print("cd: Destination is a file")
        except QueryError:
            print("cd: No such file or directory")
