import string
path='C:\\Users\\JKyukino\\Desktop\\test.txt' #test.txt为自定义文件
with open(path, 'rb') as text:
	words=[word.decode().strip(string.punctuation).lower() for word in text.read().split()]
	words_index=set(words)
	word_dict={index:words.count(index) for index in words_index}
for word in sorted(word_dict,key=lambda k:word_dict[k],reverse=True):
	print('{}:{}'.format(word,word_dict[word]))