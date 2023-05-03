class StringUtility:
    def init(self, input_str):
        self.str = input_str

    def str(self):
        return self.string

    def vowels(self):
        vowel_count = sum(1 for c in self.str if c.lower() in 'aeiou')
        if vowel_count < 5:
            return str(vowel_count)
        else:
            return 'many'

    def bothEnds(self):
        if len(self.str) <= 2:
            return ''
        else:
            return self.str[:2] + self.str[-2:]

    def fixStart(self):
        if len(self.str) <= 1:
            return self.str
        else:
            first_char = self.str[0]
            return first_char + self.str[1:].replace(first_char, '*')

    def asciiSum(self):
        return sum(ord(c) for c in self.str)

    def cipher(self):
        shift = len(self.str)
        result = ''
        for c in self.str:
            if c.isalpha():
                if c.islower():
                    result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += c
        return result
