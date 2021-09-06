
#DOES NOT WORK. Research Later
#multiple constructor techniques


class primaryClass():
    def __init__(self, xed, yed, zed):
        self.xed = xed
        self.yed = yed
        self.zed = zed
    @classmethod
    def altClass(cls):
        aed = 5
        bed = 18
        ced = 25



if __name__ == '__main__':

    fork = primaryClass(3, 8, 14)
    cork = primaryClass.altClass()

    print(fork.xed)

    #print(cork.altClass.aed)
