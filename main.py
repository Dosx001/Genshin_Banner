from banner import banner

def main():
    ban = banner()
    ban.table()
    ban.chart()
    ban.update(['Noelle', 'Beidou', 'Xingqiu'])
    ban.table()
    #ban.save()

if __name__ == "__main__":
    main()
