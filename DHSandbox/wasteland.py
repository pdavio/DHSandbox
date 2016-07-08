#Retrieve and structure wastland from UTF
import nltk
import codecs

def rawText():
    path = 'C:\\Users\\pdavio\\Desktop\\DigitalHumanities\\wasteland\\1321-0.txt'
    text = codecs.open(path, 'r', 'UTF-8').read()
    return text

def getLines() :
    text = rawText().split('\n');
    for line in text:
        print(line)

def getTokens(): 
    #tokens = nltk.word_tokenize(rawText())
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rawText())
    return tokens

def getScrubbedTokens():
    tokens = getTokens()
    from nltk.corpus import stopwords
    filtered_word_list = tokens[:] #make a copy of the word_list
    #print(len(filtered_word_list))
   
    for word in tokens: # iterate over word_list
        word.strip()
        if word in stopwords.words('english') or len(word) == 1:
            filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword
    #print(len(filtered_word_list))

        #newlist = [for w in tokens if w.lower() not in stopwords and len(w) > 3 and w.isalpha()]

    filtered_word_list = sorted(list(set(filtered_word_list)))
    return filtered_word_list

def getStems():
   tokens = getScrubbedTokens()
   #porter = nltk.PorterStemmer()
   porter = nltk.LancasterStemmer()
   porter_stems = [porter.stem(t) for t in tokens]    
   print(len(porter_stems))
   return porter_stems

def getLemma():
    tokens = getScrubbedTokens()
    print(len(tokens))
    wnl = nltk.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    print(len(lemmas))
    #for lemma in lemmas:
        #print(lemma)
    return lemmas

def getPoS():
    tokens = getScrubbedTokens()
    pos = nltk.pos_tag(tokens)
    #for p in pos:
     #   print(p)
    return pos

def getNouns():
    #nltk.help.upenn_tagset()
    pos = getPoS()
    nouns = list()
    for i in range(0,len(pos)):
        if pos[i][1].startswith('N'):
            nouns.append(pos[i][0])
    for n in nouns:
        print(n)
    return nouns
    

def getEpub():
    import epub
    path = 'C:\\Users\\pdavio\\Desktop\\DigitalHumanities\\wasteland\\1321-0.epub'
    book = epub.open_epub(path)






  

            


