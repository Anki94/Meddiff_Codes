class abs_file_sys:
    def __init__(self, path):
        self.path1 = path

    def change_dir(self, path2):
        i=0
        pathlst=path2.split('/')
        path_len=len(pathlst)
        main_pathList=self.path1.split('/')
        if pathlst[0]=='':
            del main_pathList[:]
            main_pathList.append('/'+pathlst[1])
            i=i+2
        while(i<path_len):
            j=len(main_pathList)-1
            if pathlst[i]=='..':
                main_pathList.pop(j)
            else:
                main_pathList.append(pathlst[i])
            i=i+1
        self.path1="/".join(main_pathList)

        pass

path = abs_file_sys('/a/b/c/d')
path.change_dir('../z')
print(path.path1)
