import numpy as np
def get_vocab(vocab_path,tag_path):
    vocab={}
    tag_map={}
    with open(vocab_path,'r') as file:
        for i,l in enumerate(file.read().splitlines()):
            vocab[l]=i
        vocab['<PAD>']=len(vocab)
    with open(tag_path,'r') as file:
        for i,tag in enumerate(file.read().splitlines()):
            tag_map[tag]=i
    return vocab,tag_map


def get_params(vocab, tag_map, sentences_file, labels_file):
    sentences=[]
    labeles=[]

    with open(sentences_file,'r') as file:
        for sentence in file.read().splitlines():
            s=[]
            for token in sentence.split(' '):
                if token in vocab:
                    s.append(vocab[token])
                else:
                    s.append(vocab['UNK'])
            sentences.append(s)
        
    with open(labels_file,'r') as file:
            for label_line in file.read().splitlines():
                l=[]
                for label in label_line.split(' '):
                    l.append(tag_map[label])
                labeles.append(l)
    return sentences,labeles,len(sentences)
# print('Hello world')