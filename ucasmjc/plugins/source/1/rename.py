import os
 
class BatchRename():
 
    def rename(self):
        path = "C:/Users/24967/Desktop/ucasmjc/ucasmjc/plugins/source/1"
        filelist = os.listdir(path)
        for item in filelist:
            if (item.endswith(".mp3")):
                index=item.split("_")[0]
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path), ''+index+'.mp3')
                os.rename(src, dst)
if __name__=='__main__':
    demo = BatchRename()
    demo.rename()
