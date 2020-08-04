#Project STEGUN (Steganographic encoder and decoder).
#Author: Raajeshwaran Thiagarajan.

import sys
import binascii
import hashlib
import os
import sys

def hasher(data):
    h1=hashlib.md5(data).hexdigest()
    return(h1)
    
    
def encode():
    buff=[]
    #Input Message
    print('\nEnter the message to be embedded:')
    print('Note: Size limit for the message is 95 bytes')
    msg=input('\n>>>')
    msg_size=len(msg.encode('utf-8'))
    while True:
        if not msg_size > 95:
            break
        else:
            print('\n[error]:Message size exceeds the limit \nplease enter a new message:')
            msg=input('\n>>>')
            msg_size=len(msg.encode('utf-8'))

    #Input carrier image name
    print('\nEnter the name of the image file:')
    image_name=input('\n>>>')
    while True:
        if not 'jpg' in image_name:
            print('\n[error]:$TEGUN only supports files with .jpg extension \nPlease enter a valid jpg file:')
            image_name=input('\n>>>')
        else:
            break
            
    while True:
        try:
            file=open(image_name,'rb')
            image_data=file.read()
            file.close()
            break
        except:
            print('\nInvalid file name, please enter a valid image file:')
            image_name=input('\n>>>')

    #Hashing original image file data
    hash_data1=hasher(image_data)

    #Opening image file to find size
    with open(image_name,'rb') as image:
        image.seek(0,2)
        image_size1=image.tell()
        image_size2=image_size1
        image.seek(0,0)
        a1=image.read(image_size1)

    #Adding entire image_data in bytes to buff
        for i in range(len(a1)):
            x=hex(a1[i])[2:]
            buff.append(x)
        image.close()

    #Finding the EOF marker to append the message
    stat=0
    p=-1
    for i, byte in enumerate(buff):
        if stat==1:
            stat=0
            if byte=='da':
                p=i-1

        elif byte=='ff':
            stat=1

    #Appending the message to the image file
    msg_enc= [hex(ord(i))[2:] for i in msg]
    buff[p+10]=str(len(msg_enc))
    for i in range(len(msg_enc)):
        buff[p+11+i]=msg_enc[i]

    for i in range(len(buff)):
        if len(buff[i])==1:
            buff[i]='0'+buff[i]

        buff[i]=bytes.fromhex(buff[i])
    en_data= b''.join(buff)
    en_image_name=str("Encoded_"+image_name)

    #Hashing the modified image file
    hash_data2=hasher(en_data)
    with open(en_image_name, "wb") as image:
        image.write(en_data)

    image.close()

    print("\n\n\n\n                  --*-- Summary --*--                         ")
    print('\n[1] Name:',image_name,'|Size:',image_size1,'|md5 Hash:',hash_data1)
    print('\n[2] Name:',en_image_name,'|Size:',image_size2,'|md5 Hash:',hash_data2)

    print('\n\n Do you want to exit the program (y/n):')
    ch=input('\n>>>')

    if not ch=='n' or ch=='N':
        sys.exit()
    
    
    
            
            
def decode():
    buff=[]
    #Input carrier image name
    print('\nEnter the name of the image file, to extract the secret message:')
    image_name=input('\n>>>')
    while True:
        if 'Encoded' and 'jpg' in image_name:
            try:
                file=open(image_name,'rb')
                image_data=file.read()
                file.close()
                break
            except:
                print('\nInvalid file name, please enter a valid image file:')
                image_name=input('\n>>>')

        else:
            print('\nThe file mentioned is not an encoded jpg file, please enter a valid encoded image file:')
            image_name=input('\n>>>')
            

    #Hashing carrier image file data
    hash_data=hasher(image_data)
    

    #Opening image file to find size
    with open(image_name,'rb') as image:
        image.seek(0,2)
        image_size=image.tell()
        image.seek(0,0)
        a1=image.read(image_size)

     #Adding entire image_data in bytes to buff
        for i in range(len(a1)):
            x=hex(a1[i])[2:]
            buff.append(x)
        image.close()

    #Finding the EOF marker to locate the secret message
    stat=0
    p=-1
    for i, byte in enumerate(buff):
        if stat==1:
            stat=0
            if byte=='da':
                p=i-1

        elif byte=='ff':
            stat=1
    #Extracting the secret message which is embedded after EOF
    msg_len=buff[p+10]
    msg_data=buff[p+11:p+11+int(msg_len)]
    msg=b"".join([bytes.fromhex(c) for c in msg_data]).decode()
    print('\n\n\n\n  --*--Summary--*--')
    print('\n[1]The encoded message is: ',msg)
    print('\n[2]Message size: ',msg_len)
    print('\n[3]md5 Hash of carrier file: ',hash_data)
    print('\n[4]Carrier image size: {} bytes'.format(image_size))

    print('\n\n Do you want to exit the program (y/n):')
    ch=input('\n>>>')

    if not ch=='n' or ch=='N':
        sys.exit()
    
    
    
    
    
            
    
    




print("\n                                                   --* Welcome to #####STEGUN######   *--")
print("\n                                                   --* Version: 1.0 OpenSource License *--")
print('\n\n\n\n')

print("                             #############   ##############   ###############   ###########$Secret Message 007!$########")    
print("                             #############   ##############   ###############   ########################################")
print("                             ###                  ###         ###               ######################")
print("                             #############        ###         #######           #########   // ##")
print("                             #############        ###         #######           #########  // ##")
print("                                       ###        ###         ###               ################# ")     
print("                             #############        ###         ###############   ######### ")      
print("                             #############        ###         ###############   #######")




print("\n\n\n                                               The quieter you become, The more you are able to hear")
print("                                                                                                      - </DarkWriter>")
print("\n\n\n Note: Stegun only supports image files like JPG and PNG.....")
print("\n Note: The extraction can only be supported for carriers modified by Stegun.....")
      
while True:
    print('\n\n\n\n\n ---------------------------------------------------------------------------------------------------------------------------------------------')
    print("\n Option[1]:Embed message")
    print(" Option[2]:Extract message")
    print('\n Enter your option:')
    opt=input("\n >>>")


    if opt=='1':
        encode()

    elif opt=='2':
        decode()

    else:
        print('\n[error]:Invalid option')
        print('\n\n Exiting the application.....')
      
      
