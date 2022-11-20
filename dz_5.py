import inspect
import colorama
from colorama import Back, Fore, Style, init

init(autoreset=True)

for met in dir(colorama):
    print(met)

print(inspect.ismodule(colorama))

print("_______________________________________________________")

print(Back.GREEN + "Hello1")
print(Fore.RED + "I'm Artem!")
print(Fore.RED + Back.BLUE + "I'm 14 years old...")
print(Fore.YELLOW + Back.RED + Style.BRIGHT + "The text with red background...")
print(Fore.CYAN + Back.YELLOW + Style.DIM + "The text with yellow background...")
print(Fore.LIGHTGREEN_EX + Back.GREEN + Style.BRIGHT + "The text with green background...")
print("\033[3m\033[32m\033[40m{}".format("Text with black background..."))
print("\033[9m\033[21m\033[46m{}".format("Text with blue background..."))
print("\033[4m\033[52m\033[45m{}".format("Text with pink background..."))
print("_______________________________________________________")
print(Back.RED + Fore.BLACK + "Every")
print(Back.YELLOW + Fore.BLACK + "Hunter")
print(Back.LIGHTYELLOW_EX + Fore.BLACK + "Wants")
print(Back.GREEN + Fore.BLACK + "To know")
print(Back.CYAN + Fore.BLACK + "Where")
print(Back.BLUE + Fore.BLACK + "Sits")
print(Back.MAGENTA + Fore.BLACK + "Pheasant")