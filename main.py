from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.chart()
    ban.new('Thoma')
    ban.update(['Thoma', 'Noelle', 'Barbara'])
    ban.table()
    ban.show()
    #ban.save()

if __name__ == "__main__":
    main()
