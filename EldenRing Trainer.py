import pyMeow as py
from pyMeow import *
import time
import keyboard

 
try:
        process = py.open_process("start_protected_game.exe")
except:
        try:
                process = py.open_process("Elden-Ring.exe")
        except:
                print("Elden-Ring is not detected Running on System.")
                input("")

def read_offsets(proc, address, offsets):
        try:
                basepoint = py.r_int64(proc, address)
                current_pointer = basepoint
                for i in offsets[:-1]:
                        current_pointer = r_int64(proc, current_pointer + i)
                return current_pointer + offsets[-1]
        except:
                return

base_address = None


#eldenring.exe+3CDCDD8 world chr main
#eldenring.exe+3CD4D88 game data man
if process_exists("start_protected_game.exe") or process_exists("Elden-Ring.exe"):
        modules = py.enum_modules(process)
        for module in modules:
                if module['name'] == 'start_protected_game.exe' or module['name'] == 'Elden-Ring.exe':
                        #print(f"Found Module : {module}")
                        base_address = module['base']

        Roffset = 0x3CD4D88
        Roffsets = [0x08, 0x6C]    # --> PTR OFFSETS --> VALUE R
        
        charname_offset = 0x3CD4D88
        charname_offsets = [0x08, 0x9C]
        
        charType_offset = 0x3CDCDD8
        charType_offsets = [0x10EF8, 0x0*10, 0x68]


        healthoffset = 0x3CDCDD8
        health_offsets1 = [0x10EF8, 0x0*10, 0x190, 0x0, 0x138]
        
        maxHealth_Offset = 0x3CDCDD8
        maxHealth_offsets = [0x10EF8, 0x0*10, 0x190, 0x0, 0x144]
        maxHealth_offsets2 = [0x10EF8, 0x0*10, 0x190, 0x0, 0x140]

        energyoffset = 0x3CDCDD8
        energy_offsets1 = [0x10EF8, 0x0*10, 0x190, 0x0, 0x148]           # --> PTR OFFSETS --> VALUE E
        
        maxEnergy_offset = 0x3CDCDD8
        maxEnergy_offsets = [0x10EF8, 0x0*10, 0x190, 0x0, 0x150]
        maxEnergy_offsets2 = [0x10EF8, 0x0*10, 0x190, 0x0, 0x14C]
        
        stats_offset = 0x3CD4D88
        
        vigor_offsets = [0x08, 0x3C]
        mind_offsets = [0x08, 0x40]
        endurance_offsets = [0x08, 0x44]
        strength_offsets = [0x08, 0x48]
        dexterity_offsets = [0x08, 0x4C]
        intelligence_offsets = [0x08, 0x50]
        faith_offsets = [0x08, 0x54]
        arcane_offsets = [0x08, 0x58]
        
        
        #start_protected_game.exe+434222 
        All_Health_Control_State_ADDR = base_address + 0x434222 #ENGINE HEALTH BARS CONTROL   0000  ADDRESS WITH OPERATION CODES
        
        
        Runes_pointer_address = base_address + Roffset       # RUNE PTR
        char_name_PTR_address = base_address + charname_offset
        chatType_PTR_address = base_address + charType_offset

        Energy_PTR_address = base_address + energyoffset   # ENERGY 1 PTR
        max_Energy_PTR_address = base_address + maxEnergy_offset
        
        health_PTR_address = base_address + healthoffset   # HEALTH 1 PTR
        max_health_PTR_address = base_address + maxHealth_Offset
        
        vigor_PTR_address = base_address + stats_offset
        mind_PTR_address = base_address + stats_offset
        endurance_PTR_address = base_address + stats_offset
        strength_PTR_address = base_address + stats_offset
        dexterity_PTR_address = base_address + stats_offset
        intelligence_PTR_address = base_address + stats_offset
        faith_PTR_address = base_address + stats_offset
        arcane_PTR_address = base_address + stats_offset

        try:
                
                health = read_offsets(process, health_PTR_address, health_offsets1)
                max_health = read_offsets(process, max_health_PTR_address, maxHealth_offsets)
                max_health2 = read_offsets(process, max_health_PTR_address, maxHealth_offsets2)
                
                energy = read_offsets(process, Energy_PTR_address, energy_offsets1)
                max_energy = read_offsets(process, max_Energy_PTR_address, maxEnergy_offsets)
                max_energy2 = read_offsets(process, max_Energy_PTR_address, maxEnergy_offsets2)

                runes = read_offsets(process, Runes_pointer_address, Roffsets)
                Character_Name = read_offsets(process, char_name_PTR_address, charname_offsets)
                Character_Type = read_offsets(process, chatType_PTR_address, charType_offsets)
                
                Vigor = read_offsets(process, vigor_PTR_address, vigor_offsets)
                Mind = read_offsets(process, mind_PTR_address, mind_offsets)
                Endurance = read_offsets(process, endurance_PTR_address, endurance_offsets)
                Strength = read_offsets(process, strength_PTR_address, strength_offsets)
                Dexterity = read_offsets(process, dexterity_PTR_address, dexterity_offsets)
                Intelligence = read_offsets(process, intelligence_PTR_address, intelligence_offsets)
                Faith = read_offsets(process, faith_PTR_address, faith_offsets)
                Arcane = read_offsets(process, arcane_PTR_address, arcane_offsets)
                
        except:
                print("Load a game before openning.")
                input("")

        #print(f"Memory address is {str(hex(rune_arc))} with Value: {str(r_int(process, rune_arc))}")
        #print(f"\nYou have {r_int(process, runes)} Runes.\n\n")


        
        def Starter():
                state = False
                        
                
                
                
                if (py.r_bytes(process, All_Health_Control_State_ADDR, 6)) == b'\x89\x818\x01\x00\x00':
                        state = False
                elif (py.r_bytes(process, All_Health_Control_State_ADDR, 6)) == b'\x90\x90\x90\x90\x90\x90':
                        state = True
                
                
                while True:
                        print(f"\nLogged In As: {py.r_bytes(process, Character_Name, 32).decode('UTF-8', errors = 'ignore')} | Runes: {r_int(process, runes)}")
                        z = input(f"1: RUNES HACK\n2: HEALTH HACK\n3: ENERGY HACK\n4: UNLIMITED HEALTH & ENERGY\n5: CHANGE CHARACTER'S STATS\n6: CHANGE CHARACTER TYPE\n7:FREEZE GAME ENGINE HEALTH (EVERYTHING'S HEALTH FREEZE) [{state}]\n")
                        if z:
                                try:
                                        z = int(z)
                                except:
                                        print("ya 5wl\n")
                                        
                                if z == 1:    #runes
                                        runess = input("How much Runes you need ya kosmk ?\n")
                                        try:
                                                runess = int(runess)
                                                print("Writing...")
                                                time.sleep(2)
                                                w_int(process, runes, runess)
                                                print("Success ya kosmk ya hacker yabnl 27ba\n")
                                        except:
                                                print("Kosmk enter a number !\n")
                                
                                
                                elif z == 2:    #health
                                        print(f"\nYour Current Health is {py.r_int(process, health)}")
                                        method = input("1: Current Health\n2: MAX Health\n3: METHOD-3 '! HARDCORE !'\n")
                                        
                                        if method == '1':
                                                print("Giving You Max Health...")
                                                time.sleep(1)
                                                w_int(process, health, 10000)
                                                time.sleep(1)
                                                health_max = r_int(process, health)
                                                print("----------Script Running. Press F1 to Stop----------")
                                                while True:
                                                        health_new = r_int(process, health)
                                                        time.sleep(0.3)
                                                        if health_new != health_max:
                                                                w_int(process, health, health_max)
                                                        if keyboard.is_pressed('F1'):
                                                                print("Health Script exited !\n")
                                                                break
                                                        
                                        elif method == '2':
                                                print(f"Your MAX Health is {py.r_int(process, max_health)}")
                                                time.sleep(0.3)
                                                i = input("Input THE MAX HEALTH YOU NEED (DON'T GIVE HIGH NUMBERS SO THE GAME DON'T CRASH):\n")
                                                try:
                                                        i = int(i)
                                                        print("Writing...")
                                                        time.sleep(2)
                                                        py.w_int(process, max_health, i)
                                                        time.sleep(0.5)
                                                        
                                                        if py.r_int(process, max_health) == i:
                                                                print("Success ya kosmk\n")
                                                        else:
                                                                py.w_int(process, max_health2, i)
                                                                time.sleep(1)
                                                                if py.r_int(process, max_health) == i:
                                                                        print("Success ya kosmk\n")
                                                                else:
                                                                        print("Didn't work on your Save. Don't try this again to prevent corrupting your save file\n")
                                                
                                                except:
                                                        print("Kosmk it didn't work\n")
                                                        
                                        elif method == '3':
                                                print("You Will Regret !")
                                                time.sleep(5)
                                                w_int(process, health, 10000)
                                                time.sleep(1)
                                                health_max = r_int(process, health)
                                                print("Started !. Press F1 to Stop.")
                                                while True:
                                                        w_int(process, health, 1)
                                                        time.sleep(4)
                                                        w_int(process, health, health_max)
                                                        time.sleep(2)
                                                        if keyboard.is_pressed('F1'):
                                                                print("Health Script exited !\n")
                                                                break
                                                        
                                
                                
                                elif z == 3:    #energy
                                        print("\n\nThis will let you have unlimited Energy !")
                                        method = input("1: Current Energy\n2: MAX Energy\n")
                                        
                                        if method == '1':
                                                print("Giving You Max Energy...")
                                                time.sleep(1)
                                                w_int(process, energy, 1000)
                                                time.sleep(1)
                                                energy_max = r_int(process, energy)
                                                print("----------Script Running. Press F1 to Stop----------")
                                                while True:
                                                        energy_new = r_int(process, energy)
                                                        time.sleep(0.3)
                                                        if energy_new != energy_max:
                                                                time.sleep(0.2)
                                                                w_int(process, energy, energy_max)
                                                        if keyboard.is_pressed('F1'):
                                                                print("Energy Script exited !\n")
                                                                break
                                                        
                                        elif method == '2':
                                                print(f"Your MAX Energy is {py.r_int(process, max_energy)}")
                                                time.sleep(0.3)
                                                i = input("Input THE MAX ENERGY YOU NEED (DON'T GIVE HIGH NUMBERS SO THE GAME DON'T CRASH):\n")
                                                try:
                                                        i = int(i)
                                                        print("Writing...")
                                                        time.sleep(2)
                                                        py.w_int(process, max_energy, i)
                                                        time.sleep(0.5)
                                                        if py.r_int(process, max_energy) == i:
                                                                print("Success ya kosmk\n")
                                                        else:
                                                                py.w_int(process, max_energy2, i)
                                                                time.sleep(1)
                                                                if py.r_int(process, max_energy2) == i:
                                                                        print("Success ya kosmk\n")
                                                                else:
                                                                        print("Didn't work on your Save. Don't try this again to prevent corrupting your save file\n")
                                                except:
                                                        print("Kosmk it didn't work\n")
                                                        
                                elif z == 4:
                                        print("Giving You Max Health & Energy...")
                                        time.sleep(1)
                                        w_int(process, health, 10000)
                                        time.sleep(1)
                                        w_int(process, energy, 10000)
                                        time.sleep(1)
                                        
                                        health1_max = r_int(process, health)
                                        energy1_max = r_int(process, energy)
                                        print("----------Script Running. Press F1 to Stop----------")
                                        while True:
                                                        health1_new = r_int(process, health)
                                                        energy1_new = r_int(process, energy)
                                                        time.sleep(0.3)
                                                        if health1_new != health1_max:
                                                                w_int(process, health, health1_max)
                                                        if energy1_new != energy1_max:
                                                                w_int(process, energy, energy1_max)
                                                        if keyboard.is_pressed('F1'):
                                                                print("Energy Script exited !\n")
                                                                break              
                                elif z == 5:
                                        print(f"\nYou Have:\n1- Vigor: {py.r_int(process, Vigor)}")
                                        print(f"2- Mind: {py.r_int(process, Mind)}")
                                        print(f"3- Endurance: {py.r_int(process, Endurance)}")
                                        print(f"4- Strength: {py.r_int(process, Strength)}")
                                        print(f"5- Dexterity: {py.r_int(process, Dexterity)}")
                                        print(f"6- Intelligence: {py.r_int(process, Intelligence)}")
                                        print(f"7- Faith: {py.r_int(process, Faith)}")
                                        print(f"8- Arcane: {py.r_int(process, Arcane)}")
                                        print(f"9- MODIFY ALL OF THEM")
                                        i = input("Which one to modify:\n")
                                        try:
                                                i = int(i)
                                                if i == 1:
                                                        z = input("Modifying Vigor, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Vigor, z)
                                                                print("Success")
                                                elif i == 2:
                                                        z = input("Modifying Mind, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Mind, z)
                                                                print("Success")
                                                elif i == 3:
                                                        z = input("Modifying Endurance, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Endurance, z)
                                                                print("Success")
                                                elif i == 4:
                                                        z = input("Modifying Strength, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Strength, z)
                                                                print("Success")
                                                elif i == 5:
                                                        z = input("Modifying Dexterity, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Dexterity, z)
                                                                print("Success")
                                                elif i == 6:
                                                        z = input("Modifying Intelligence, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Intelligence, z)
                                                                print("Success")
                                                elif i == 7:
                                                        z = input("Modifying Faith, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Faith, z)
                                                                print("Success")
                                                elif i == 8:
                                                        z = input("Modifying Arcane, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Arcane, z)
                                                                print("Success")
                                                elif i == 9:
                                                        z = input("MODIFYING ALL STATS, Enter a number:\n")
                                                        try:
                                                                z = int(z)
                                                        except:
                                                                print("Enter a Number ykosmk")
                                                        
                                                        if z <= 99 and z >= 0:
                                                                print("Writing...")
                                                                time.sleep(2)
                                                                w_int(process, Vigor, z)
                                                                w_int(process, Mind, z)
                                                                w_int(process, Endurance, z)
                                                                w_int(process, Strength, z)
                                                                w_int(process, Dexterity, z)
                                                                w_int(process, Intelligence, z)
                                                                w_int(process, Faith, z)
                                                                w_int(process, Arcane, z)
                                                                print("Success")
                                        except:
                                                return
                                        
                                elif z == 6:
                                        Type = py.r_int(process, Character_Type)
                                        if Type == 0:
                                                CharType = 'Original'
                                        elif Type == 1:
                                                CharType = 'White Phantom'
                                        elif Type == 2:
                                                CharType = 'Dark Spirit'
                                        elif Type == 3:
                                                CharType = 'Ghost'
                                        print(f"Your Current Character Type is {CharType}\n")
                                        i = input("Choose Character Type:\n1- Original\n2- White Phantom\n3- Dark Spirit\n4- Ghost\n")
                                        try:
                                                i = int(i)
                                                i -= 1
                                                if i <= 3 and i >= 0:
                                                        print("Writing...")
                                                        time.sleep(2)
                                                        py.w_int(process, Character_Type, i)
                                                        print("Success !")
                                                else:
                                                        print("\nkosmk\n")
                                        except:
                                                print("Yla Ya 5wl")
                                
                                elif z == 7:
                                        if state == False:
                                                state = True
                                                w_bytes(process, All_Health_Control_State_ADDR, bytes([0x90, 0x90, 0x90, 0x90, 0x90, 0x90]))
                                        
                                        elif state == True:
                                                state = False
                                                w_bytes(process, All_Health_Control_State_ADDR, bytes([0x89, 0x81, 0x38, 0x01, 0x00, 0x00]))
                                        
                                
        Starter()