from colorama import Fore, init, Style

valid = False
#init(autoreset=True)

i = input(">> ")

while valid == False:
    two = input("\n" + Fore.WHITE+ Style.RESET_ALL+ "Would you like to do one for each word? (y/n)\n>> ")
    if two != 'y' and two != 'n':
        print("\n" + Fore.RED + "y/n", end='\n')
    else:
        valid = True

with open('elements2.txt', 'r') as f:
    elements2 = f.read().splitlines()
with open('elements1.txt', 'r') as f:
    elements1 = f.read().splitlines()

def Name_Generator(name):
    replaced = False
    for item in elements2:
        index = name.lower().find(item.lower())
        if index != -1:
            print(Fore.WHITE + Style.RESET_ALL+ name[:index], end='')
            print(Fore.GREEN + item, end='')
            print(Fore.WHITE + Style.RESET_ALL+ name[index+2:], end='')
            replaced = True
            break

    if replaced == False:
        for item in elements1:
            index = name.lower().find(item.lower())
            if index != -1:
                print(Fore.WHITE + Style.RESET_ALL+ name[:index], end='')
                print(Fore.GREEN + item, end='')
                print(Fore.WHITE + Style.RESET_ALL+ name[index+1:], end='')
                replaced = True
                break
    if replaced == False:
        print(Fore.RED + "Sorry, that name is not Breaking Bad-able.", end='')
        print(Fore.WHITE + Style.RESET_ALL + '')
        
if two == 'y':
    print("\n")
    for item in i.split(' '):
        Name_Generator(item)
        print(' ', end='')
    print("")
else:
    print("\n")
    Name_Generator(i)
    print('')
print("\n")
