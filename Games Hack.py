import os
import time
from colorama import init, Fore, Style
import sys
import struct
import subprocess

init()

def check_root():
    try:
        subprocess.check_output(['su', '-c', 'id'])
        return True
    except:
        return False

class GameMemoryModifier:
    def __init__(self):
        self.process_handle = None
        self.game_process = None
        self.memory_addresses = {
            'Free Fire': {
                'coins': 0x13F89A24,
                'items': 0x13F89B24, 
                'level': 0x13F89C24,
                'abilities': 0x13F89D24,
                'health': 0x13F89E24,
                'damage': 0x13F89F24,
                'speed': 0x13F8A024,
                'jump': 0x13F8A124,
                'flight': 0x13F8A224,
                'wallhack': 0x13F8A324,
                'aimbot': 0x13F8A424,
                'invisibility': 0x13F8A524,
                'teleport': 0x13F8A624,
                'unlimited_ammo': 0x13F8A724,
                'no_recoil': 0x13F8A824,
                'radar_hack': 0x13F8A924,
                'auto_headshot': 0x13F8AA24,
                'character_skin': 0x13F8AB24,
                'weapon_skin': 0x13F8AC24,
                'vehicle_boost': 0x13F8AD24
            },
            'PUBG Mobile': {
                'coins': 0x14F89A24,
                'items': 0x14F89B24,
                'level': 0x14F89C24,
                'abilities': 0x14F89D24,
                'health': 0x14F89E24,
                'damage': 0x14F89F24,
                'speed': 0x14F8A024,
                'jump': 0x14F8A124,
                'flight': 0x14F8A224,
                'wallhack': 0x14F8A324,
                'aimbot': 0x14F8A424,
                'invisibility': 0x14F8A524,
                'teleport': 0x14F8A624,
                'unlimited_ammo': 0x14F8A724,
                'no_recoil': 0x14F8A824,
                'radar_hack': 0x14F8A924,
                'auto_headshot': 0x14F8AA24,
                'character_skin': 0x14F8AB24,
                'weapon_skin': 0x14F8AC24,
                'vehicle_boost': 0x14F8AD24
            }
        }

    def get_process_pid(self, package_name):
        try:
            cmd = f"su -c 'pidof {package_name}'"
            result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
            return int(result) if result else None
        except:
            return None

    def attach_to_process(self, game_name: str) -> bool:
        try:
            package_names = {
                'Free Fire': 'com.dts.freefireth',
                'PUBG Mobile': 'com.tencent.ig'
            }
            
            package_name = package_names.get(game_name)
            if not package_name:
                return False
                
            pid = self.get_process_pid(package_name)
            if not pid:
                return False
                
            mem_file = f"/proc/{pid}/mem"
            self.process_handle = open(mem_file, 'rb+')
            return True
        except:
            return False

    def write_memory(self, address: int, value: int, size: int = 4) -> bool:
        try:
            cmd = f"su -c 'dd if=/dev/zero of=/proc/{self.process_handle.name}/mem bs={size} count=1 seek={address} conv=notrunc'"
            subprocess.check_output(cmd, shell=True)
            return True
        except:
            return False

    def clear_screen(self):
        os.system('clear')

    def print_header(self):
        print(Fore.CYAN + """
    ╔═════════════════════════════╗
    ║     Mobile Game Modifier v3.0     ║
    ║       Root Access Required        ║
    ║          SquateDev               ║
    ╚═════════════════════════════╝
    """ + Style.RESET_ALL)

    def print_menu(self):
        print(Fore.GREEN + """
    [1] Free Fire
    [2] PUBG Mobile
    [3] Exit
    """ + Style.RESET_ALL)

    def loading_animation(self):
        print("\nПодключение", end="")
        for _ in range(5):
            time.sleep(0.5)
            print(Fore.YELLOW + ".", end="", flush=True)
        print(Style.RESET_ALL)

    def modify_game_value(self, game: str, modification: str) -> bool:
        modifications = {
            '1': ('coins', 999999),
            '2': ('items', 1),
            '3': ('level', 100),
            '4': ('abilities', 1),
            '5': ('health', 999999),
            '6': ('damage', 9999),
            '7': ('speed', 200),
            '8': ('jump', 150),
            '9': ('flight', 1),
            '10': ('wallhack', 1),
            '11': ('aimbot', 1),
            '12': ('invisibility', 1),
            '13': ('teleport', 1),
            '14': ('unlimited_ammo', 1),
            '15': ('no_recoil', 1),
            '16': ('radar_hack', 1),
            '17': ('auto_headshot', 1),
            '18': ('character_skin', 1),
            '19': ('weapon_skin', 1),
            '20': ('vehicle_boost', 1)
        }
        
        if modification not in modifications:
            return False
            
        param, value = modifications[modification]
        address = self.memory_addresses[game][param]
        return self.write_memory(address, value)

    def check_game_running(self, game_name: str) -> bool:
        package_names = {
            'Free Fire': 'com.dts.freefireth',
            'PUBG Mobile': 'com.tencent.ig'
        }
        package_name = package_names.get(game_name)
        if not package_name:
            return False
            
        pid = self.get_process_pid(package_name)
        return pid is not None

    def apply_modifications(self, game: str):
        try:
            self.clear_screen()
            print(Fore.CYAN + f"\nПодключение к игре {game}..." + Style.RESET_ALL)
            self.loading_animation()
            
            if self.attach_to_process(game):
                print(Fore.GREEN + "\n[✓] Подключение успешно установлено" + Style.RESET_ALL)
                
                while True:
                    print(Fore.YELLOW + "\nДоступные модификации:" + Style.RESET_ALL)
                    print("""
    1. Бесконечные монеты
    2. Разблокировать все предметы
    3. Максимальный уровень
    4. Особые способности
    5. Бесконечное здоровье
    6. Увеличенный урон
    7. Супер скорость
    8. Супер прыжок
    9. Полёт
    10. WallHack
    11. AimBot
    12. Невидимость
    13. Телепортация
    14. Бесконечные патроны
    15. Отключение отдачи
    16. Радар-хак
    17. Автохедшот
    18. Все скины персонажей
    19. Все скины оружия
    20. Ускорение транспорта

    0. Главное меню
                    """)
                    
                    choice = input(Fore.CYAN + "Выберите модификацию (0-20): " + Style.RESET_ALL)
                    
                    if choice == '0':
                        break
                        
                    if choice in [str(i) for i in range(1, 21)]:
                        print(Fore.YELLOW + "\nПрименение модификации..." + Style.RESET_ALL)
                        self.loading_animation()
                        
                        if self.modify_game_value(game, choice):
                            print(Fore.GREEN + "\n[✓] Модификация успешно применена!" + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "\n[×] Ошибка при применении модификации" + Style.RESET_ALL)
                        
                        time.sleep(2)
                    else:
                        print(Fore.RED + "\nНеверный выбор!" + Style.RESET_ALL)
                        time.sleep(1)
                
                return True
                
            else:
                print(Fore.RED + "\n[×] Ошибка: Игра не запущена или нет root-доступа" + Style.RESET_ALL)
                return False
                
        except Exception as e:
            print(Fore.RED + f"\n[×] Ошибка: {str(e)}" + Style.RESET_ALL)
            return False

    def run(self):
        if not check_root():
            print(Fore.RED + "\n[×] Ошибка: Root-доступ не обнаружен!" + Style.RESET_ALL)
            time.sleep(2)
            sys.exit()
            
        print(Fore.GREEN + "\n[✓] Root-доступ подтвержден" + Style.RESET_ALL)
        time.sleep(1)

        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = input(Fore.CYAN + "\nВыберите игру (1-3): " + Style.RESET_ALL)
            
            if choice == '3':
                self.clear_screen()
                print(Fore.YELLOW + "\nЗавершение работы..." + Style.RESET_ALL)
                time.sleep(1)
                sys.exit()
                
            if choice in ['1', '2']:
                game_names = {
                    '1': 'Free Fire',
                    '2': 'PUBG Mobile'
                }
                
                self.clear_screen()
                print(Fore.YELLOW + f"\nВыбрано: {game_names[choice]}" + Style.RESET_ALL)
                confirm = input(Fore.CYAN + "\nПродолжить? (да/нет): " + Style.RESET_ALL).lower()
                
                if confirm == 'да':
                    if self.apply_modifications(game_names[choice]):
                        input(Fore.GREEN + "\nНажмите Enter для возврата в меню..." + Style.RESET_ALL)
                    else:
                        input(Fore.RED + "\nНажмите Enter для возврата в меню..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "\nНеверный выбор!" + Style.RESET_ALL)
                time.sleep(2)

def main():
    try:
        if not check_root():
            print(Fore.RED + "\n[×] Для работы программы требуется root-доступ!" + Style.RESET_ALL)
            sys.exit(1)
            
        modifier = GameMemoryModifier()
        modifier.run()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nПрограмма завершена." + Style.RESET_ALL)
        sys.exit()

if __name__ == "__main__":
    main()
