import matplotlib.pyplot as plt
import PIL, random
from wordcloud import WordCloud

def saveCloud(list):
    try:
       name = list.name #if corpus
    except:
       name = "text" + (''.join(str(random.randint(0,9)) for _ in range(5))) 
    
    text = ''.join(list)
    WordCloud.background_color = "white"
    wordcloud = WordCloud().generate(text)
    
    plt.axis("off")
    plt.imshow(wordcloud)
    #plt.show()
    plt.savefig(name)

