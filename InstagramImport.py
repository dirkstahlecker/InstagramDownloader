class InstagramImport:
    goodChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z','-','\'',
                 '/','\\''\:''.']
    URLs = []
    doc= ''

    def __init__(self):
        tempFile = open('pagecode.txt', 'r')
        self.doc = tempFile.read()
        tempFile.close()
        self.parse()
        self.checkURL()

    def parse(self):
        word = ''
        adding = False
        profilePic = False
        inFrame = False
        holder = ''
        for char in self.doc:
            char = char.lower()

            #words are URLs
            if char == '{': #curly cbraces separate URLs
                inFrame = True
            elif char == '}':
                inFrame = False

            #determines if URL is a profile pic
            if inFrame:
                holder += char
                if len(holder) > 7:
                    holder = holder[1:]
                if holder == 'profile':
                    profilePic = True
            
            if word == '' and not adding: # word is empty
                if char == '\"': #quotes start words
                    adding = True
            elif adding: #word not empty
                if char == '\"': #quotation marks separate
                    if not profilePic:
                        self.URLs.append(word)
                    word = ''
                    adding = False
                    profilePic = False
                else:
                    word += char

    def checkURL(self):
        tempURLs = []
        for url in self.URLs:
            if '.jpg' in url:
                tempURLs.append(url)
        self.URLs = tempURLs

    def printURLs(self):
        for url in self.URLs:
            print url

    #def writeToHTML(self):
        

i = InstagramImport()
i.printURLs()
