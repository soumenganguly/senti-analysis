from nltk.tokenize import WordPunctTokenizer,sent_tokenize
from nltk.corpus import stopwords
import collections
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier

def bag_of_words(f):
  return dict([j,True] for j in f)

def label_feats_from_corpus(corp,feature_detector=bag_of_words):
  label_feats=collections.defaultdict(list)
  for label in corp.categories():
p    for fileid in corp.fileids(categories=[label]):
      feats=feature_detector(corp.words(fileids=[fileid]))
      label_feats[label].append(feats)
  lfeats=label_feats
  split_label_feats(lfeats)

train_feats=[]
test_feats=[]

def split_label_feats(lfeats,split=0.75):
  for label,feats in lfeats.iteritems():
    cutoff=int(len(feats)*split)
    train_feats.extend([(feat,label) for feat in feats[:cutoff]])
    test_feats.extend([(feat,label) for feat in feats[cutoff:]])




print("Enter a Text")
a=raw_input(">>")
li=sent_tokenize(a)
li_=[]
tokenizer_=WordPunctTokenizer()
for i in li:
  li_.append(tokenizer_.tokenize(i))
li__=[]
for i in range(len(li_)):
  for j in li_[i]:
    li__.append(j)
words=[]
stopfile=stopwords.words('english')
for i in li__:
  if i not in stopfile:
    words.append(i)

label_feats_from_corpus(movie_reviews)

p=bag_of_words(li__)
nb=NaiveBayesClassifier.train(train_feats)
print nb.classify(p)



 
