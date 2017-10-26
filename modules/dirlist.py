import os 

def run(**args):
    files = os.listdir(".")
    print"[*]Dirlist started."
    return str(files)