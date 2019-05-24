import nltk
#nltk.download_gui()


   # SENTENCE TOKENIZATION
"""

TEXT = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios, it's time for the practical part of the course. We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a token is the outcome of whatever was spread up, based on some set of rules. Every word is a token if a sentence is tokenized. A sentence can also be a token if we tokenize sentences out of an article. Let's check out how it works. First we can start by opening up PyCharm Community Edition, and as you can see here I've created a new project called NLTK tasks. And you can do the same by clicking on file, new project, and in type in here the name of the project. And as you can see I'm using Python 3.7. Let's create a file, a Python file, called pre-processing. The next thing we need to do is create a configuration"\
    "click on add configuration, click on this plus sign here, Python, click here, and then add the patch or project. Let's select pre-process indoor py. Click on apply and ok. The next thing is installing NLTK. Let's click on file, settings for new projects selects, select Python 3.7, and make sure to select the interpreter or the Python version you are using for your project. Click on this plus sign here, in type in NLTK. Select this one, NLTK, and click on install package. Now as you can see here it's blue because I have already installed it for Python 3.7 interpreter. Let's start coding by important NLTK. As we said before, NLTK comes with a bunch of corpora and already trained models, so let's download some corpora so that we can work with him. To do that we type in NLTK dot download UI, and let's run our program. And once we run NLTK download, you can see here this GOI for NLTK downloader. It has collections, corpora, models, and if you want to download all the packages. And as you can see here for my case everything is green, which means I have downloaded or installed everything. Please make sure to download brown corpora and also ABC, because we will use them later. Here also we have collections, like if you wanna download all the corpora, all NLTK, the popular ones, and also the things covered from NLTK comm tutorial book. And if you want to check where NLTK downloads all the data or all the corpora, you can go to this directory here now. Let's stop it, let's remove this line and let's start with sentence tokenization. But before we start tokenizing text, let's add a piece of text."\

from nltk import sent_tokenize

sentences = sent_tokenize(TEXT)

print("**********ORIGIONAL TEXT:**********\n"+TEXT+"\n\n")
print("**********Sentences:**********\n" + str(len(sentences)) + "\n\n")

i = 0
for sentence in sentences:
    i=i+1
    print("Sentenc-"+str(i)+"  : "+sentence)
"""

    # Word Tokenization
"""

from nltk import word_tokenize

WORDS = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. " \
        "Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios," \
        " it's time for the practical part of the course. " \
        "We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a" \
        " programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens" \
        " out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a" \

words = word_tokenize(WORDS)

print("**********ORIGIONAL TEXT:**********\n"+WORDS+"\n\n")
print("**********Words:**********\n" + str(len(words)) + "\n\n")

i =0
for word in words:
    i = i+1
    print("words "+str(i)+"   :"+word )
"""
"""
# remove stop[ words



WORDS = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. " \
        "Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios," \
        " it's time for the practical part of the course. " \
        "We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a" \
        " programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens" \
        " out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a" \

from nltk import word_tokenize
words = word_tokenize(WORDS)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanWords = [w for w in words if not w in stop_words]
print("**********Words:**********\n" + str(len(words)) + "\n\n")
print("**********clean Words:**********\n" + str(len(cleanWords)) + "\n\n")
i =0
for word in cleanWords:
    i = i+1
    print("words "+str(i)+"   :"+word)
"""
"""
#pos (parts of speech)

WORDS = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. " \
        "Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios," \
        " it's time for the practical part of the course. " \
        "We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a" \
        " programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens" \
        " out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a" \

from nltk import word_tokenize
words = word_tokenize(WORDS)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanWords = [w for w in words if not w in stop_words]
from nltk import pos_tag

taggedWords = pos_tag(cleanWords)
print(nltk.help.upenn_tagset())
i =0
for words in taggedWords:
    i=i+1
    print("set "+str(i)+" :"+str(words))
"""

"""
#stemming
WORDS = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. " \
        "Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios," \
        " it's time for the practical part of the course. " \
        "We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a" \
        " programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens" \
        " out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a" \

from nltk import word_tokenize
words = word_tokenize(WORDS)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanWords = [w for w in words if not w in stop_words]

from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')

i=0
for word in cleanWords:
    i =i+1
    print("-"+str(i)+" : : " +word+" : : "+stemmer.stem(word))

#lemetization
from nltk.stem import WordNetLemmatizer
limit = WordNetLemmatizer()
i=0
for word in cleanWords:
    i =i+1
    print("-"+str(i)+" : : " +word+" : : "+limit.lemmatize(word, pos="v"))

"""

"""
#NER

WORDS = "Hello all and welcome to the first video of the second section, called dive into NLTK or Natural Language Toolkit. " \
        "Now that we got familiar with NLP, what it means, its libraries in some of the real world, applications and uses scenarios," \
        " it's time for the practical part of the course. " \
        "We will start by discovering and applying some common NLP tasks, of course using NLTK as a library in Python as a" \
        " programming language. The first task we will talk about is tokenization. To tokenize a piece of text or to get the tokens" \
        " out of a text is the process of breaking it up into smaller individual words or sentences, known as tokens. By definition a" \

from nltk import word_tokenize
words = word_tokenize(WORDS)
from nltk.corpus import stopwords
import string
stop_words = set(stopwords.words('english'))
stop_words = stop_words.union(string.punctuation)
cleanWords = [w for w in words if not w in stop_words]
from nltk import pos_tag

taggedWords = pos_tag(cleanWords)
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
from nltk.stem import WordNetLemmatizer
limit = WordNetLemmatizer()

from nltk import ne_chunk, sent_tokenize
sentences = sent_tokenize(WORDS)


for senctence in sentences:
    word = word_tokenize(senctence)
    tags = pos_tag(word)
    ner = ne_chunk(tags)
    ner.draw()
"""


















