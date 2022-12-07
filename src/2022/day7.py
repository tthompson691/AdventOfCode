from utils.utils import pull_input_directly


class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = dict()
        self.files = dict()
        self.parent = None
        self.total_size = 0
        self.part1_eligible = False
        
    
    def find_total_size(self):
        self.total_size = sum(self.files.values())
        
        for subdir in self.subdirs:
            self.total_size += self.subdirs[subdir].find_total_size()
        
        self.part1_eligible = self.total_size <= 100000
            
        return self.total_size
    
    
def part1(dir: Directory, totalsum=0):
    if dir.part1_eligible:
        totalsum += dir.total_size
        
    for subdir in list(dir.subdirs.values()):
        totalsum += part1(subdir)
    
    return totalsum

def part2(dir: Directory):
    disk_space = 70000000
    need_space = 30000000
    available = disk_space - dir.total_size
    delete_size = need_space - available
    
    def part2_helper(curdir, current_winner):
        if curdir.total_size >= delete_size and curdir.total_size < current_winner:
            current_winner = curdir.total_size
                
        for subdir in list(curdir.subdirs.values()):
            current_winner = part2_helper(subdir, current_winner)
            
        return current_winner

    return part2_helper(dir, available)
    

if __name__ == "__main__":
    cmds = pull_input_directly(2022, 7)[1:-1]
    
    # plant the tree
    activedir = Directory("/")
    for cmd in cmds:
        if "$ cd" in cmd and ".." not in cmd:
            switchdir = cmd.split(" ")[-1]          
            activedir = activedir.subdirs[switchdir]
        elif cmd == "$ cd ..":
            activedir = activedir.parent
        elif "dir " in cmd:
            dirname = cmd.split(" ")[-1]
            newdir = Directory(name=dirname)
            activedir.subdirs[dirname] = newdir
            newdir.parent = activedir
        elif cmd == "$ ls":
            continue
        else:
            filename = cmd.split(" ")[-1]
            size = int(cmd.split(" ")[0])
            activedir.files[filename] = size
    
    # get back to the root
    activedir = activedir.parent
    
    # get all directory sizes
    activedir.find_total_size()
    
    print(part1(activedir))
    print(part2(activedir))
            