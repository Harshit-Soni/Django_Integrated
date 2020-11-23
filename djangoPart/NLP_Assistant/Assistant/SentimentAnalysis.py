import nltk
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import classify
from nltk import NaiveBayesClassifier
import re, string,random
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from .AmazonReviewScrapping import getReviews
import pickle as p

classifier = p.load(open(r'H:\MajorProject\Project\Django_Integrated\djangoPart\NLP_Assistant\static\models\classifier_model_Amazon.pkl', 'rb'))

def getAntRepl(word):
    antonym=[]
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            for ant in lemma.antonyms():
                antonym.append(ant.name())
    
    if len(antonym)!=0:
        return antonym[0]
    else:
        return word

negations=["aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', 
"hasn't",'haven', "haven't",'isn',"isn't",'ma','mightn',"mightn't",'mustn',"mustn't",'needn',"needn't",'shan',
"shan't",'shouldn',"shouldn't",'wasn',"wasn't",'weren',"weren't",'won',"won't",'wouldn',"wouldn't",'never']

def remove_noise(tweet_tokens, stop_words=()):
    cleaned_tokens = []
    flag=False
    for token, tag in pos_tag(tweet_tokens):
        
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)
        
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        elif tag.startswith('JJ') and flag:
            token=getAntRepl(token.lower())
            flag=False
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        if token.lower() in negations:
            flag=True
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def analize(url):
    try:
        review_list,title=getReviews(url)
    except:
        return {'empty':True}
    if len(review_list)==0:
        return {'empty':True}
    print(title)

    pos,neg=0,0
    l=[]
    for r in review_list:
        tk=remove_noise(word_tokenize(r),stopwords.words('english'))
        sent=classifier.classify(dict([token,True] for token in tk))
        l.append(sent)
        if sent=='Positive':
            pos+=1
        else:
            neg+=1
    return {'title':title,'len':len(review_list),'list':l,'posR':pos,'negR':neg}
    # print(f'Total Positive Reviews: {pos} :: Total Negative Reviews: {neg}')
    # print('Customer Satisfaction via Reviews is {:.2f}%'.format((pos/(pos+neg))*100))
        
def singleTest(rev):
    tk=remove_noise(word_tokenize(rev),stopwords.words('english'))
    print(tk)
    print(classifier.classify(dict([token,True] for token in tk)))
