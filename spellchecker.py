import re, collections

def words(text):
	return re.findall('[a-z]+',text.lower())
def train (features):
	model=collections.defaultdict(lambda:1) #default value is 1 whenever called
	for i in features:
		model[i]+=1;
	return model

NWORDS = train (words(file('big.txt').read()))

alphabet = 'qwertyuiopasdfghjklzxcvbnm'

def edits1(word):
	splits		= [(word[:i],word[i:]) for i in range(len(word)+1)]
	deletes 	= [a+b[1:] for a,b in splits if b]
	transposes 	= [a+b[1]+b[0]+b[2:] for a,b, in splits if len(b)>1]
	replaces	= [a+c+b[1:] for a,b in splits for  c in alphabet if b ]
	inserts		= [a+c+b for a,b in splits for c in alphabet]
	return set (deletes+transposes+replaces+inserts)

def edits2(word):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known (words):
	return set(temp for temp in words if temp in NWORDS)
def correct(word):
	if (word not in NWORDS):
		candidates = known([word]) or known(edits1(word)) or edits2(word) or [word]
		return max(candidates,key=NWORDS.get)
	else:
		return word

#string = raw_input("Enter a Word\n")
#print correct(string)," "
f = open('test.txt')
for word in f.read().split():
    print(correct(word)),

