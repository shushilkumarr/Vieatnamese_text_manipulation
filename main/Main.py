import csv

def convert_to_dict(word_freq):
    dict={}
    for word in word_freq:
        #print(word)
        if word[1]=='':
            continue
        if(word[1][0] not in dict.keys()):
            dict[word[1][0]]=[]
            dict[word[1][0]].append([word[1],word[0]])
        else:
            if(word[1] not in dict[word[1][0]]):
                dict[word[1][0]].append([word[1],word[0]])
    return dict

def decode(string, mapping):
    point=0
    for map in mapping:
        if point==3:
            break
        string1=string.replace(map[1],map[2])
        if(string1!=string):
            if point>map[0]:
                pass
            else:
                point=map[0]
                string=string1
    return string



file=open('character_mapping.txt','r')
reader = csv.reader(file)
mapping=[]
print("reading mappings..")
for row in reader:
    map=row[0].split('\t')
    map.append(len(map[1]))
    map.reverse()
    mapping.append(map)
mapping=mapping[1:]
mapping.sort(reverse=True)
file.close()

file=open('word_corpus.txt','r')
reader=csv.reader(file)
word_freq=[]



print("reading corpus...")
for row in reader:
    map=row[0].split('\t')
    map[1]=decode(map[1],mapping)
    try:
        map[0]=int(map[0])
    except:
        continue
    word_freq.append(map)

file.close()

file=open("word_frequency.txt",'w')
for line in word_freq:
    file.write(str(line[0])+","+line[1]+"\r")
word_freq=word_freq[1:]
word_freq.sort(reverse=True)
file.close()

print("Generating Index...")
index_dict=convert_to_dict(word_freq)

print("Generated Index...")
print("Input Key: ")
key=str(input())
word_list=index_dict[key[0]]
key_len=len(key)
result=[]
for word in word_list:
    if(word[0][:key_len]==key):
        result.append(word)

for word in result:
    print(word[0]+"\t("+str(word[1])+")")