from banner import banner

def main():
    ban = banner()
    ban.table()
    #ban.chart()
    ban.new('Thoma')
    ban.update(['Noelle', 'Thoma', 'Barbara'])
    ban.table()
    #ban.save()

if __name__ == "__main__":
    main()
