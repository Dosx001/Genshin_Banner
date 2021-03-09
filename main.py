from banner import banner

def main():
    ban = banner()
    for i in ban.characters:
        print(i)
        print(ban.last(i))
        print(ban.total(i))

if __name__ == "__main__":
    main()
