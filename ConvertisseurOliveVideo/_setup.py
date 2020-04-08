import os

#chemin_dossier = os.path.dirname(__file__)
#chemin_info = os.path.join(chemin_dossier,"data","info.json")

os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)\"")
os.system("brew install python3") #/usr/local/Cellar/python/3.7.7
os.system("brew install ffmpeg") #/usr/local/Cellar/ffmeg
os.system("pip3 install --upgrade pip")
os.system("pip3 install --user PySide2") #/Users/noe/Library/Python/3.7/lib/python/site-packages
os.system("pip3 install --user ffmpeg-python") #/Users/noe/Library/Python/3.7/lib/python/site-packages
os.system("pip3 install --user future") #/Users/noe/Library/Python/3.7/lib/python/site-packages

os.system("python3 _videoConverterStart.py")

#uninstall Homebrew
#ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
