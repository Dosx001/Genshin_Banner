from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.chart()
    ban.update(['Noelle', 'Fischl', 'Barbara'])
    ban.table()
    ban.show()
    #ban.save()

if __name__ == "__main__":
    main()
