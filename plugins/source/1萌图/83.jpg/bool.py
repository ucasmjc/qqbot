import os,shutil
def mycopyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print ("copy %s -> %s"%(srcfile, dstpath + fname))
 
 
src_dir = './'
dst_dir = './copy/'                                    # 目的路径记得加斜杠
filelist = os.listdir(src_dir);          
for srcfile in filelist:
    mycopyfile(srcfile, dst_dir)                       # 复制文件