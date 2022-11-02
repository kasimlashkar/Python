# Install pyperclip command given below
# --> pip install pyperclip
# go to Pydroid3 terminal & Run The Command 

#import pyperclip

while True:
    opt = input("Options:\n 1.Encode\n 2.Decode\n 3.Exit\nEnter Your Choice :")
    if opt=="1":
            text = input("enter a string values :")
            ascii_values = []
            for character in text:
                ascii_values.append(ord(character))
            length=len(ascii_values)
            i=0
            for i in range(length):
                ascii_values[i]=ascii_values[i]*56
            i=0
            print()
            ascii=""
            for i in range(length):
                #print(chr(ascii_values[i]),end='')
                ascii="".join((ascii, str(chr(ascii_values[i]))))
            #pyperclip.copy(ascii)
            print(ascii)
            print("\n")
        
    elif opt=="2":
            #text = pyperclip.paste()
            text = input("enter a string values :")
            ascii_values = []
            for character in text:
                ascii_values.append(ord(character))
            length=len(ascii_values)
            i=0
            for i in range(length):
                ascii_values[i]=int(ascii_values[i]/56)
            i=0
            print()
            for i in range(length):
                print(chr(ascii_values[i]),end='')
            print("\n")
    elif opt=="3":
            exit()
    else:
            print("Invalid Option")
