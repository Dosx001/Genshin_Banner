from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.chart()
    ban.update(['Ningguang', 'Bennett', 'Razor'])
    ban.table()

if __name__ == "__main__":
    main()
