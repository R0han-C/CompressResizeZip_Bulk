from tqdm import tqdm
import os,glob,shutil,zipfile
path = os.walk(".")
from PIL import Image
import time
from tqdm import tqdm



def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def choice():
    print("MENU".center(40,"*"))
    print("1.Compression".center(40," "))
    print("2.Resizing".center(40," "))
    
    choice_user=(int(input("ENTER YOUR CHOICE:-\n".center(40," "))))
    if choice_user==1:
        compression()

    if choice_user==2:
        resizing() 
    if choice_user!=1 and choice_user!=2:
        print("\nENTER RIGHT CHOICE:-".center(40," "))
        choice()



def compression():
    
    qual=(int(input("Enter the Quality (1-100) you want to maintain.:-\n")))
    folders=[]
    for root, directories, files in path:
        for directory in directories:
            folders.append(directory)

    paths=[]
    for i in folders:
        paths.append((os.getcwd()+'\\'+i+"\\"))

    for i in ((paths)):
        os.chdir(i)
        files_in_sub=(os.listdir())
        for img in (tqdm(files_in_sub,desc="COMPRESSION PROGRESS :--->")):
            image_ = Image.open(img)
            file_name_compressed="COMPRESSED-"+img
            image_.save(file_name_compressed,quality=qual)
            image_.close()
    os.chdir('..')        
    if os.path.exists('OUTPUT'):
        shutil.rmtree('OUTPUT')

    if not os.path.exists('OUTPUT'):
        os.makedirs('OUTPUT')        
    zipf = zipfile.ZipFile('OUTPUT.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(os.getcwd(), zipf)
    zipf.close()
    shutil.move((os.getcwd()+'\OUTPUT.zip'),(os.getcwd()+'\OUTPUT'))           


    print("COMPRESSION DONE".center(40,"*"))        

def resizing():
    
    width=(int(input("\nEnter the Width for Resizing:-\n")))
    height=(int(input("\nEnter the Height for Resizing:-\n")))


    folders=[]
    for root, directories, files in path:
        for directory in directories:
            folders.append(directory)

    paths=[]
    for i in folders:
        paths.append((os.getcwd()+'\\'+i+"\\"))           

    
    for i in ((paths)):
        os.chdir(i)
        files_in_sub=(os.listdir())
        for img in (tqdm(files_in_sub,desc="RESIZING PROGRESS --->")):
            image_ = Image.open(img)
            file_name_resized='RESIZED-'+img
        
            image_resize= image_.resize((width,height),Image.ANTIALIAS)
            image_resize.save(file_name_resized)
            
            image_resize.close()
                
    os.chdir('..')
    if os.path.exists('OUTPUT'):
        shutil.rmtree('OUTPUT')

    if not os.path.exists('OUTPUT'):
        os.makedirs('OUTPUT')    
    zipf = zipfile.ZipFile('OUTPUT.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(os.getcwd(), zipf)
    zipf.close()
    shutil.move((os.getcwd()+'\OUTPUT.zip'),(os.getcwd()+'\OUTPUT'))                  
    print("RESIZING DONE".center(40,"*"))







choice()        


