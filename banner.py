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

    def new(self, char):
        self.characters.update({char: []})
        self.characters = dict(sorted(self.characters.items()))

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
        output = f"{'Name':15}| # of RUs | # of banners since last RU\n"
        stack = []
        for char in sorted(self.characters, key=lambda x:(self.last(x), self.total(x)), reverse=True):
            if len(stack) == 0:
                stack.append(char)
            elif self.last(char) == self.last(stack[0]):
                stack.append(char)
            else:
                output += self.unstack(stack)
                stack.append(char)
        output += self.unstack(stack)
        print(output)

    def unstack(self, stack):
        output = ""
        while len(stack) != 0:
            char = stack.pop()
            output += '-' * 55 + '\n'
            output += f"{char:15}|{self.total(char): ^10}|{self.last(char):>5}\n"
        return output

