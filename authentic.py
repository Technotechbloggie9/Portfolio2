import hashlib
class Authentic:
    def __init__(self):
        self.start = 78
        self.end = 115
        self.midend = 69
        self.midstart = 110
        self.hash = "870912e5e4be933fd5175614c455a2b1529f6f4993c4fce63d62e33fad75e64b"
    def startstring(self):
        xstring = "" + chr(self.start) + chr((19 + self.start)) + chr((38 +self.start))
        ystring = "" + chr(self.midstart) + chr((self.midstart - 13)) + chr((self.midstart - 6))
        zstring = self.reverse(ystring)
        return xstring + zstring
    def endstring(self):
        xstring = "" + chr(self.midend) + chr((34 + self.midend)) + chr((34 + self.midend))
        ystring = "" + chr(self.end) + chr((self.end - 1)) + chr((self.end - 14))
        zstring = self.reverse(ystring)
        return xstring + zstring
    def reverse(self, x):
        return x[::-1]
    def information(self):
        return self.startstring() + " " + self.endstring()
    def authenticate(self):
        check = False
        string1 = self.information()
        result = hashlib.sha256(string1.encode())
        if (self.hash == result.hexdigest()):
            check = True
        return check
def main():
    a = Authentic()
    print(a.information())
    print(a.authenticate())
    
if __name__ == "__main__":
    main()
