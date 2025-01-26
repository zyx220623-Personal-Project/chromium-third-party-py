from sys import argv
from os import system,rename
import os
error_list = []
init_project_number: int = 0
if len(argv) == 2:
    output_path = argv[1]
def is_https(arg:list[str]):
    for i in arg:
        if "https://" in i and "googlesource" in i:
            return True
    return False
def get_unrenamed_path(path: str, link: str):
    path_to_list = path.split("/")
    i = 0
    folder = ""
    for j in path_to_list:
        i+=1
        if i != len(path_to_list):
            folder += j
            folder += "/"
    link_to_list = link.split("/")[-1]
    folder+=link_to_list
    if folder[len(folder)-4:] != ".git":folder += ".git"
    folder = folder.replace("F:/src/src/","F:/src/")
    return folder
def get_renamed_path(folder: str):
    if folder[len(folder)-4:] != ".git":folder += ".git"
    folder = folder.replace("F:/src/src/","F:/src/")
    return folder
def get_link(arg:list[str]):
    for i in arg:
        if "https://" in i:
            j = i.split("@")
            return j[0]
def get_project_path(arg:list[str]):
    return arg[1]
def init_project(out_path: str,
                 project_path: str,
                 project_link: str):
    global init_project_number
    global real_output_path
    bat_file = open("C:/bat.bat","w+")
    file: str = ""
    file += out_path[0]
    file += ":\n"
    file += "cd "
    file += out_path
    file += "\n"
    path_to_list = project_path.split("/")[1:]
    for i in path_to_list[:len(path_to_list)-1]:
            file += "mkdir "
            file += i
            file += "\n"
            file += "cd "
            file += i
            file += "\n"
    file += f"git clone --mirror {project_link}"
    bat_file.write(file)
    bat_file.close()
    if not os.path.exists(get_renamed_path(real_output_path+"/"+project_path)):
        system ("C:\\bat.bat")
        apath = get_unrenamed_path(real_output_path+"/"+project_path,project_link)
        try:
            rename(apath,get_renamed_path(real_output_path+"/"+project_path))
        except:
            error_list.append([apath,get_renamed_path(real_output_path+"/"+project_path),project_link])
    else:
        file: str = ""
        file += out_path[0]
        file += ":\n"
        file += "cd "
        file += get_renamed_path(real_output_path+"/"+project_path).replace("/","\\")
        file += "\n"
        file += "git fetch --tags -f"
        bat_file = open("C:/bat.bat","w+")
        bat_file.write(file)
        bat_file.close()
        system ("C:\\bat.bat")
    init_project_number += 1

file = open("1.txt","r")
read = file.read().split("\n")
file.close()
k = 0
link_list = []
path_list = []
for i in read:
    j = i.split("'")
    if is_https(j):
        link_list.append(get_link(j))
        path_list.append(get_project_path(j))
        k += 1
real_output_path = output_path.replace("\\","/")
for i in range(0, len(link_list)):
    path = path_list[i]
    link = link_list[i]
    init_project(output_path,path,link)
print(error_list)
input()



    


    