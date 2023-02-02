import os
os.system("ipconfig")#выполнение shell-скриптов
os.chdir("D:")#переход в директорию
os.mkdir("workers")#создание папки
os.rename("workers","WWW")#изменение названия папки
os.rmdir("WWW")#удаление папок
os.getcwd()#получение пути,в котором находится юзер