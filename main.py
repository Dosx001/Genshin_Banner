from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.chart()
    ban.new('Rosaria')
    ban.update(['Rosaria', 'Fischl', 'Barbara'])
    ban.table()

if __name__ == "__main__":
    main()
