import glob
import os
dir = os.getcwdb()
os.chdir(dir)
print("1] Delete all .txt files.")
print("2] Delete all .png files.")
print("3] Delete all .jpg files.")
print("4] Delete all .docx files.")
print("5] Delete all .exe files.")
print("6] Delete all .blend files.")
print("7] Delete all .doc files.")
print("8] Delete all .msg files.")
print("9] Delete all .pdf files.")
print("10] Delete all .rtf files.")
print("11] Delete all .jfif files.")
print("12] Delete all .wpd files.")
c = input("@~# ")
if c == "1":
    for file in glob.glob("*.txt"):
        print(file)
        os.remove(file)
elif c == "2":
    for file in glob.glob("*.png"):
        print(file)
        os.remove(file)
elif c == "3":
    for file in glob.glob("*.jpg"):
        print(file)
        os.remove(file)
elif c == "4":
    for file in glob.glob("*.docx"):
        print(file)
        os.remove(file)
elif c == "5":
    for file in glob.glob("*.exe"):
        print(file)
        os.remove(file)
elif c == "6":
    for file in glob.glob("*.blend"):
        print(file)
        os.remove(file)
elif c == "7":
    for file in glob.glob("*.doc"):
        print(file)
        os.remove(file)
elif c == "8":
    for file in glob.glob("*.msg"):
        print(file)
        os.remove(file)
elif c == "9":
    for file in glob.glob("*.pdf"):
        print(file)
        os.remove(file)
elif c == "10":
    for file in glob.glob("*.rtf"):
        print(file)
        os.remove(file)
elif c == "11":
    for file in glob.glob("*.jfif"):
        print(file)
        os.remove(file)
elif c == "12":
    for file in glob.glob("*.wpd"):
        print(file)
        os.remove(file)
# Thank you for checking my account!!
