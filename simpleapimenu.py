import shutil
import os


def createopenendpoint():
    url = input("\nopen endpoint url : host/")
    url = url.replace("/","-")
    filelocation = os.path.dirname(__file__)+"/api/src/files/endpoint"
    filetarget = os.path.dirname(__file__)+"/endpoint"
    print("copy from "+filelocation+ " to : "+filetarget)
    shutil.copy(filelocation,filetarget)
    os.rename(filetarget+"/endpoint",filetarget+"/"+url+".php")
    print(url)
    utama()


def createsecurepenendpoint():
    url = input("\nsecure endpoint url : host/")
    url = url.replace("/","-")
    filelocation = os.path.dirname(__file__)+"/api/src/files/secureEndpoint"
    filetarget = os.path.dirname(__file__)+"/endpoint"
    print("copy from "+filelocation+ " to : "+filetarget)
    shutil.copy(filelocation,filetarget)
    os.rename(filetarget+"/secureEndpoint",filetarget+"/"+url+".php")
    print(url)
    utama()

def listEndpoint():
    os.listdir()
    input("")
    utama()

def utama():    
    os.system('cls')
    print("-------------------------------------------\n")
    print("-      PHP SIMPLE API by danielbeeh       -\n")
    print("-------------------------------------------\n\n")
    print("  1. create open endpoint")
    print("  2. create secure endpoint")
    print("  3. list endpoint")
    opt = input("choose : ")


    if opt == "1":
        createopenendpoint()
    elif opt == "2":
        createsecurepenendpoint()
    elif opt == "3":
        listEndpoint()

utama()
