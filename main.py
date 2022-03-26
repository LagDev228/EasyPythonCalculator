import sys
from colorama import Fore
while True:
    a=float(input(f"{Fore.CYAN}First Number: "))
    b=float(input(f"{Fore.YELLOW}Second Number: "))
    c=str(input(f"{Fore.MAGENTA}Action: "))
    if (c=="+"):
        print(f"{Fore.MAGENTA}Solution:",a+b)
        print()
    elif (c=="-"):
        print(f"{Fore.MAGENTA}Solution:",a-b)
        print()
    elif (c=="*"):
        print(f"{Fore.MAGENTA}Solution:",a*b)
        print()
    elif (c=="//" or ":" or "/"):
        print(f"{Fore.MAGENTA}Solution:",a//b)
        print()
        
        
