import os
from os import system
import time
import colorama
from colorama import Fore

#Logo of the application
print('''  ▄█     █▄     ▄████████  ▄█    █▄     ▄████████ 
███     ███   ███    ███ ███    ███   ███    ███ 
███     ███   ███    ███ ███    ███   ███    █▀  
███     ███   ███    ███ ███    ███  ▄███▄▄▄     
███     ███ ▀███████████ ███    ███ ▀▀███▀▀▀     
███     ███   ███    ███ ███    ███   ███    █▄  
███ ▄█▄ ███   ███    ███ ███    ███   ███    ███ 
 ▀███▀███▀    ███    █▀   ▀██████▀    ██████████ 
                                                 
''')
#Run the application yes/no
start = input('Start Miner? y/n\n')
no = ('n')
yes = ('y')
if start == no:
    print('Ok, bye')
    time.sleep(0.5)
    system('exit')
#If start, a (fake) starting prozess will be sumulated
if start == yes:
    print('Starting . . .')
    time.sleep(1.4)
    print('Searching for Wallets . . .')
    time.sleep(2.85)
    print('Wallets found!\n\n\n')
    time.sleep(0.9)


    eth = ('      ETH:  0.0000')
    Wal = ('Wallet: ')
    privatekey = ('      Private Key:  [HIDDEN]')
    #Some fake ETH wallets (random generated letters & digits as long as a real ETH wallet is)
    str = (Fore.RED + 
           Wal + '0x1ABC7154748D1CE5144478CDEB574AE244B939B5' + privatekey + eth + '\n' +
          Wal + 'FSQA8IRR5DCB2OO259DY2M7G7I7SP23EN7AXCNC5AX' + privatekey + eth + '\n' +
          Wal + '2EZE9C3P4TNISF0D9IGX2G0ARSVA0F5YPM8XW8G9CG' + privatekey + eth + '\n' +
          Wal + 'IBK3RNZT22ONUMCCK0NK7R0V1QBKSOESTV2A6BU19R' + privatekey + eth + '\n' +
          Wal + 'ATEXYEF97RQQQR8Z4AN7QO9MPW4U510ACWSYBE0CQ8' + privatekey + eth + '\n' +
          Wal + 'J10KYQNPVBLH9QJTAYFML1SSX1I91B9BSO6MPQS0IS' + privatekey + eth + '\n' +
          Wal + 'IUMYQOBP6QHJ5AZPFS2JED9U9WQNA3PDQTVBXBZX6W' + privatekey + eth + '\n' +
          Wal + 'H3W52CH61EH9G1PFBVVP7YVPP2NFX7W0WJFPCLMOCY' + privatekey + eth + '\n' +
          Wal + '35AQ5EMU7KK5LMP8FC1FYULXQNZKVNWZAX0IPVP3VI' + privatekey + eth + '\n' +
          Wal + 'P3NC4DOJX2OZOTYNYDPXCHS6JR52DHW39Z2WASUPLB' + privatekey + eth + '\n' +
          Wal + 'NCA68O22NUGSILYP6R9PX6SMUEYZQQXORNKGH8RLFQ' + privatekey + eth + '\n' +
          Wal + 'RYF3PLDDWP19UFJ4NIVO3L2Z6WXJOHT9IW4ITKPEVT' + privatekey + eth + '\n' +
          Wal + 'OH1K8761UG4R9GUSYWFMO06LW9TD33YVYANUXV8301' + privatekey + eth + '\n' +
          Wal + 'TQOC2FBFETQVHU0VT3HVFEDDN4PLD9AP308Q3YNG9F' + privatekey + eth + '\n' +
          Wal + 'XB7VD85HPA0OIA5MR12XHJC6EGI8VIJR2BX6DDLK8L' + privatekey + eth + '\n' +
          Wal + 'YI0NFEK42H9IX1WYPKL3VSJV0GJ3NU9V5AJOGIFDW8' + privatekey + eth + '\n')
    #Repeat printing the fake wallets
    print(str*559999)
    #Fake found of a wallet with some ETH
    strr = print( Fore.GREEN + Wal + 'HO34WYASE82BKPLIHTMERK06FD6Z3F9EOGRQEQ4UAP' + privatekey +  '      ETH:  0.8034')
    print(strr)
    #Some dialog for the user who couldn't read the code
    print(Fore.WHITE + '\nto save Walletadress + Private key (clear) sent 5 dollar to the developer of this programm.')
    userinput = input('Is that ok? y/n\n')
    if userinput == no:
        print('Thats ok, the programm save the data on my pc.\n\nHave a nice day.\n')
    if userinput == yes:
        print('Send the money to xy')
        time.sleep(10)
        userinput_done = input('Done? y/n\n')
        if userinput_done == no:
            print('Ok, i saved the data on my pc.\n\nHave a nice day.\n')
            system('exit')
        if userinput_done == yes:
            print('You\'re a good boy, here your data:\n')
            time.sleep(2)
            x = ''
            wall = ('HO34WYASE82BKPLIHTMERK06FD6Z3F9EOGRQEQ4UAP\n')
            for characters in wall:
                x += characters
                print('Wallet: ',x)
                time.sleep(0.2)
                os.system('cls||clear')
            time.sleep(2.5)
            yx = ''
            key = (' ecb8e\n')
            for characters in key:
                print('Wallet: HO34WYASE82BKPLIHTMERK06FD6Z3F9EOGRQEQ4UAP\n')
                yx += characters
                print('Key: ',yx)
                time.sleep(2.9)
                os.system('cls||clear')
            #Fake error 
            print('Error! \n')
            






