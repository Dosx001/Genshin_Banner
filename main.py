from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.update(['Razor', 'Sucrose', 'Noelle'])
    ban.table()
    ban.new('Rosaria')
    ban.update(['Rosaria', 'Fischl', 'Xinyan'])
    ban.table()

if __name__ == "__main__":
    main()
