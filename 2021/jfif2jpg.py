import os
import glob

ext1 = ".jfif"
ext2 = ".jpg"
fname = "*"+ ext1

flist = glob.glob(fname) #fname拡張子の一覧を取得
print(flist)

for file in flist:
	os.rename(file, file.replace(ext1, "") + ext2) #ext2拡張子に変更
