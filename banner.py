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

    def update(self, chars):
        self.count += 1
        for char in chars:
            self.characters[char].append(self.count)

    def save(self):
        with open('banner.json', 'w') as file:
            output = {'count': self.count}
            output.update({'characters': self.characters})
            json.dump(output, file, indent=2)
