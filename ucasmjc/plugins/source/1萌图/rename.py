import os
 
class BatchRename():
 
    def rename(self):
        path = "C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1萌图"
        filelist = os.listdir(path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if (item.endswith(".jpg")):
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path), ''+str(i)+'.jpg')
                os.rename(src, dst)
                i += 1
        print('total %d to rename & converted %d png'%(total_num, i))
 
if __name__=='__main__':
    demo = BatchRename()
    demo.rename()
