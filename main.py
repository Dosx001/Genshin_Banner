from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.update(['Fischl', 'Sucrose', 'Barbara'])
    ban.table()
    ban.update(['Rosaria', 'Bennett', 'Razor'])
    #ban.update(['Ningguang', 'Bennett', 'Razor'])
    ban.table()
    ban.chart()

if __name__ == "__main__":
    main()
