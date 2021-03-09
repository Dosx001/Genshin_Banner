import json

class banner:
    def __init__(self):
        with open('banner.json') as f:
            info = json.load(f)
        self.count = info['count']
        self.characters = info['characters']

    def __repr__(self):
        output = f"count: {self.count}\n"
        for char in self.characters:
            output += f"{char}: {self.characters[char]}\n"
        return output

    def getChars(self):
        return [char for char in self.characters]

    def update(self, chars):
        self.count += 1
        for char in chars:
            self.characters[char].append(self.count)

    def save(self):
        with open('banner.json', 'w') as file:
            output = {'count': self.count}
            output.update({'characters': self.characters})
            json.dump(output, file, indent=2)

    def total(self, char):
        return len(self.characters[char])

    def last(self, char):
        try:
            return self.count - self.characters[char][-1]
        except IndexError:
            return 0

    def table(self):
        print(f"{'Name':15}| # of RUs | # of banner since last RU")
        for char in self.characters:
            print('-' * 55)
            print(f"{char:15}|{self.total(char): ^10}|{self.last(char):>5}")
