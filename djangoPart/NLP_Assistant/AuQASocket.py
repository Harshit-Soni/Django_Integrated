import asyncio
import websockets
import json

#################################################################################

import re
import gensim
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import gensim.downloader as api
import numpy
from nltk.tokenize import sent_tokenize

print('Loading Model...')
v2wModel=None
try:
    v2wModel=gensim.models.KeyedVectors.load(r'H:\MajorProject\Project\Django_Integrated\djangoPart\NLP_Assistant\static\models\w2vModel.mod')
    print('Model Loaded')
except:
    print('model Not Found \ndownloading model...')
    v2wModel=api.load('word2vec-google-news-300')
    v2wModel.save('./w2vModel.mod')
    print('model Downloaded and saved')
# w2vecEmbeddings_size=len(v2wModel['computer'])
sent_embeddings=[]
cleaned_answers=''

def cleanSentences(sentence,stopwords=False):
    sentence=sentence.lower().strip()
    sentence=re.sub(r'[^a-z0-9\s—]','',sentence)
    sentence=re.sub('[—-]',' ',sentence)
    sentence=re.sub('\n',' ',sentence)
    if stopwords:
        sentence=remove_stopwords(sentence)
    return sentence

def getCleaned(data,stopwords=False):
    cleaned=[]
    for sentence in data:
        x=cleanSentences(sentence,stopwords)
        cleaned.append(x)
    return cleaned


def getQA(question_emb,sent_emb,data):
    max_sim=-1
    max_sim2=-1
    index_sim=-1
    index_sim2=-1
    for index,faq_emb in enumerate(sent_emb):
        sim=cosine_similarity(faq_emb,question_emb)[0][0]
        if sim>max_sim:
            max_sim=sim
            index_sim=index
        if sim>max_sim2 and sim<max_sim:
            max_sim2=sim
            index_sim2=index
    print('Retrieved: ',data[index_sim])
    return data[index_sim]+'\n'+data[index_sim2]


def getWordVec(word,model):
    samp=model['computer']
#     vec=[0]*len(samp)
    try:
        vec=model[word]
    except:
        vec=[0]*len(samp)
    return (vec)

def getPhraseEmbedding(phrase,embeddingModel):
    samp=getWordVec('computer',embeddingModel)
    vec=numpy.array([0]*len(samp))
    den=0
    for word in phrase.split():
        den+=1
        vec=vec+numpy.array(getWordVec(word,embeddingModel))
    return vec.reshape(1,-1)

def driver(data):
    data=data.split('\n\n')
    data=' '.join(data)
    data=sent_tokenize(data)
    data=getCleaned(data,stopwords=False)
    global cleaned_answers
    cleaned_answers=data
    for sent in data:
        sent_embeddings.append(getPhraseEmbedding(sent,v2wModel))
    # question='which company has largest foreign acquisition till now'
    # question_embedding=getPhraseEmbedding(question,v2wModel)
    # return getQA(question_embedding,sent_embeddings,data)

################################################################


async def chat_receiver(websocket, path):
    async for message in websocket:
        message = json.loads(message)
        ques = message['text']
        global sent_embeddings
        # print(message['comp'])
        if len(sent_embeddings)==0 or len(message['comp'])!=0:
            sent_embeddings=[]
            driver(message['comp'])

        question_embedding=getPhraseEmbedding(ques,v2wModel)
        chat_response=getQA(question_embedding,sent_embeddings,cleaned_answers)
        print(chat_response)
        await websocket.send(json.dumps({'response': chat_response}))

async def router(websocket, path):
	if path == "/":
		await chat_receiver(websocket, path)

    #the code below is how you add other path's
    
	# elif path == "/shade-area":
	# 	await get_shaded_area(websocket, path)
	# elif path == '/render':
	# 	await render(websocket, path)

asyncio.get_event_loop().run_until_complete(websockets.serve(router, '0.0.0.0', 8770))

asyncio.get_event_loop().run_forever()