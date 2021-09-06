import requests

class makeReq():
    def __init__(self):
        self.reqPage = requests.get('https://boingboing.com')
        #print(self.reqPage.text)

    def printSlicer(self):
        for zed in range(len(self.reqPage.text)):
            print(self.reqPage.text[zed:zed + 100])



if __name__ == '__main__':
    print('main running')
    #instantiate
    oneObj = makeReq()
    #This slices
    #oneObj.printSlicer()

theCommands = '''
print(help(oneObj.reqPage))
print( '                ')
oneObj.reqPage.text
oneObj.reqPage.links
oneObj.reqPage.headers
oneObj.reqPage.content


'''
