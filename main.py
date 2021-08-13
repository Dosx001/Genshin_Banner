from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.update(['Xiangling', 'Xingqiu', 'Noelle'])
    ban.table()
    #ban.save()
    ban.chart()

if __name__ == "__main__":
    main()
