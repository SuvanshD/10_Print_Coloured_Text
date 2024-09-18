import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+Back.BLUE+"Hello World"+Fore.WHITE+Style.DIM+Back.BLUE+"Hello World")
print(Fore.YELLOW+Style.BRIGHT+Back.BLUE+"Hello World"+Fore.WHITE+Style.DIM+Back.BLUE+"Hello World")
print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Hello World"+Fore.WHITE+Style.DIM+Back.BLUE+"Hello World")