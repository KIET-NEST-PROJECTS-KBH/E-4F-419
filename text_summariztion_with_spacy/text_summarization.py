import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
# FROM STRING IMPORT PUNCTUATION
document="""Reactive and proactive data streams¶
The origin of a data stream can vary, and usually it doesn't matter. You should be able to use River regardless of where your data comes from. It is however important to keep in mind the difference between reactive and proactive data streams.

Reactive data streams are ones where the data comes to you. For instance, when a user visits your website, that's out of your control. You have no influence on the event. It just happens and you have to react to it.

Proactive data streams are ones where you have control on the data stream. For example, you might be reading the data from a file. You decide at which speed you want to read the data, in what order, etc.

If you consider data analysis as a whole, you're realize that the general approach is to turn reactive streams into proactive datasets. Events are usually logged into a database and are processed offline. Be it for building KPIs or training models.

The challenge for machine learning is to ensure models you train offline on proactive datasets will perform correctly in production on reactive data streams.

"""
def summarizer(document):
  stopwords=list(STOP_WORDS)
  # print(len(stopwords))
  nlp=spacy.load('en_core_web_sm')
  doc=nlp(document)
  print(doc)
  tokens=[token.text for token in doc]
  # print(tokens)
  word_freq={}
  for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in  punctuation:
      if word.text not in word_freq.keys():
        word_freq[word.text]=1

      # word_freq[word.text]=1
      else:
        word_freq[word.text]+=1
  # print(word_freq) 
  max_freq=max(word_freq.values())
  # print(max_freq)
  for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq
    # print(word_freq)
  sent_token=[sent for sent in doc.sents]
  # print(sent_token)
  sent_scores={}
  for sent in sent_token:
    for word in sent:
      if word.text in word_freq.keys():
        if sent not in sent_scores.keys():
          sent_scores[sent]=word_freq[word.text]
        else:
          sent_scores[sent]+=word_freq[word.text]
  # print(sent_scores )
  select_len=int(len(sent_token)*0.3)
  summary=nlargest(select_len,sent_scores,key=sent_scores.get)
  # print(summary)
  final_summary=[word.text for word in summary]
  summary=' '.join(final_summary)

  print(summary)
  # print("length of the original text  ",len(document.split(' ')))
  # print("Length of the summary text ", len(summary.split(' ')))
  return summary,doc,len(document.split(' ')),len(summary.split(' '))
