from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.new('Rosaria')
    ban.update(['Rosaria', 'Fischl', 'Barbara'])
    ban.table()

if __name__ == "__main__":
    main()
