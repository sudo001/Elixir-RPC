# certified sudo classic

import os, json, time, sys, ctypes, cursor, glob, random
from pystyle import *
from pypresence import *
from colorama import Fore

cursor.hide()

class etc:
    version = "1.0.1"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def resize(cols, rows):
    if os.name == "posix":
        sys.stdout.write("\x1b[8;{cols};{rows}t".format(rows=rows, cols=cols))

def title(text):
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW(f"{text}")
    else:
        print(f'\33]0;{text}\a', end='', flush=True)

def get_option(text):
    return f"{Fore.MAGENTA}[{Fore.RESET}{text}{Fore.MAGENTA}]{Fore.RESET}"

class art:
    ascii = """                         
                       ,                          
                      ,,*,,,                      
                     *********                    
                   ,*,,,*,,,*,,.                  
                 ,*,*,*,*,*,*,*,,                 
               ,*,,,*,,,*,,,*,,,*                 
             ,*******************,     .          
            *,,,*,,,*,,,*,,,*,,,*,    ,,,         
           ,*,*,*,*,*,*,*,*,*,*,*   *,*,*         
          ,,*,,,*,,,*,,,*,,,*,,,*,,,*,,,,         
           ******. *********************          
           ,*,,,.  ,*,,,*,,,*,,,*,,,*,,           
            .,*,    ,,*,*,*,*,*,*,*,*             
               ,.      ,*,,,*,,,*.                """
    
    options = f""" {get_option(1)} Launch config   {get_option(2)} Create config   {get_option(3)} Delete config
"""

class printing:
    def success(text):
        print(f" {Fore.LIGHTGREEN_EX}[✓]{Fore.RESET} {text}")
    
    def error(text):
        print(f" {Fore.LIGHTRED_EX}[×]{Fore.RESET} {text}")

def wizard():
    if not os.path.exists("Configs"):
        os.mkdir("Configs")
        printing.success("Configs/ folder created successfully")
    
    if not os.path.isfile("Configs/elixir.json"):
        pattern = """{
    "Application ID": "1054005029448728657",
    "Description": "github.com/sudo001/Elixir",
    "Details": "Elixir on top!",
    "Big Image": "main",
    "Big Image Text": "Elixir 1.0.1",
    "Small Image": "main",
    "Small Image Text": "Im smol!",
    "Show Time": true,
    "Buttons": [
        {
            "label": "Get Elixir", "url": "https://github.com/sudo001/Elixir-RPC"
        },
        {
            "label": "Google Ong", "url": "https://google.com"
        }
    ]
}"""
        file = open("Configs/elixir.json", "w").write(pattern)
        printing.success("Configs/elixir.json created successfully")
        printing.success("Press ENTER to launch Elixir")
        input()
    
        os.system("python3 Elixir.py")

wizard()
class rpc:
    def startrpc(name):
        if not name.endswith(".json"):
            name += ".json"
        rpcconfig = f"Configs/{name}"
        try:
            open(rpcconfig, "r")
        except:
            printing.error("Config does not exist")
            input()
            return
    
        client_id = str(json.loads(open(f"{rpcconfig}", "r").read())["Application ID"])
        try:
            RPC = Presence(client_id)
            RPC.connect()
        except Exception as error: 
            printing.error(error)
            return
        buttons = []
        buttons_list = json.loads(open(f"{rpcconfig}", "r").read())["Buttons"]
        for button in buttons_list:
            buttons.append(button)
        bottomtext = json.loads(open(f"{rpcconfig}", "r").read())["Description"]
        toptext = json.loads(open(f"{rpcconfig}", "r").read())["Details"]
        smallimage = json.loads(open(f"{rpcconfig}", "r").read())["Small Image"]
        image = json.loads(open(f"{rpcconfig}", "r").read())["Big Image"]
        smallimagetext = json.loads(open(f"{rpcconfig}", "r").read())["Small Image Text"]
        imagetext = json.loads(open(f"{rpcconfig}", "r").read())["Big Image Text"]
        showtime = json.loads(open(f"{rpcconfig}", "r").read())["Show Time"]
        if showtime == True:
            start_time = time.time()
        else:
            start_time = None
        if not buttons:
            buttons = None
        try:
            RPC.update(state=toptext, details=bottomtext, small_image=smallimage, small_text=smallimagetext, large_image=image, large_text=imagetext, start=start_time, buttons=buttons)
        except Exception as error:
            printing.error(error)
        printing.success("RPC connected")
        input()

def menu():
    clear()
    resize(36, 81)
    title(f"Elixir - {etc.version}")
    print(Fore.MAGENTA + Center.XCenter(art.ascii) + "\n\n")
    print("─"*os.get_terminal_size().columns + "\n")
    print(art.options)
    print(Fore.MAGENTA + "─"*os.get_terminal_size().columns + Fore.RESET + "\n")
    print()
    choice = input(" "+get_option(">")+" ")
    print()
    if choice == "1":
        cfgs = ""
        configs = glob.glob('Configs/*')
        for config in configs:
            config = config.replace("Configs/", "")
            config = config.replace(".json", "")
            cfgs += f"{config}, "
        xy = random.randint(1111, 9999)
        cfgs = cfgs + f"{xy}"
        cfgs = cfgs.replace(f", {xy}", "")
        if cfgs == str(xy):
            cfgs = "No configs" 
        # shit solution, but it works so idc
        
        print(" " + get_option("Configs")+f" {cfgs}")
        print()
        name = input(" "+get_option("Config name")+" ")
        rpc.startrpc(name)
    
    elif choice == "2":
        name = input(" "+get_option("Config Name")+" ")
        client_id = input(" "+get_option("Application ID")+" ")
        details = input(" "+get_option("Details")+" ")
        description = input(" "+get_option("Description")+" ")
        showtime = input(" "+get_option("Show Time [y/n]")+" ").lower()
        if showtime == "y":
            showtime = True
        else:
            showtime = False
        bigimage = input(" "+get_option("Big Image [leave blank for no image]")+" ")
        if len(bigimage) > 1:
            bigimagetext = input(" "+get_option("Big Image Text")+" ")
        else:
            bigimage = f"{random.randint(111111111, 999999999)}"
            bigimagetext = f"{random.randint(111111111, 999999999)}"

        smallimage = input(" "+get_option("Small Image [leave blank for no image]")+" ")
        if len(smallimage) > 1:
            smallimagetext = input(" "+get_option("Small Image Text")+" ")
        else:
            smallimage = f"{random.randint(111111111, 999999999)}"
            smallimagetext = f"{random.randint(111111111, 999999999)}"
        
        buttons = input(" "+get_option("Buttons (0-2)")+" ")
        buttons_final = []
        button_count = 0

        try:
            buttons = int(buttons)
        except:
            buttons = 0

        if int(buttons) > 2:
            printing.error("There cant be more than 2 buttons, repeat this process")
            input()
            return
        
        if buttons > 0:
            for i in range(int(buttons)):
                button_count += 1
                button_name = input(" "+get_option(f"Button {button_count} Name")+" ")
                button_url = input(" "+get_option(f"Button {button_count} URL")+" ")
                final_button = {"label": button_name, "url": button_url}
                buttons_final.append(final_button)

        final_config = {
    "Application ID": str(client_id),
    "Description": description,
    "Details": details,
    "Big Image": bigimage,
    "Big Image Text": bigimagetext,
    "Small Image": smallimage,
    "Small Image Text": smallimagetext,
    "Show Time": showtime,
    "Buttons": buttons_final

}

        config = open(f"Configs/{name}.json", "w")
        config.write(json.dumps(final_config, indent=4))
        printing.success("Config created")
        input()
    
    elif choice == "3":
        name = input(" "+get_option("Config Name")+" ")
        if not name.endswith(".json"):
            name += ".json"
        try:
            os.remove(f"Configs/{name}")
            printing.success("Config deleted")
        except:
            printing.error("Config does not exist")
        input()

while 1:
    menu()
