import os

#a = input('請輸入要轉換的檔案名稱含副檔名：')

#if os.path.isfile(filename):
#	print('找到檔案了！')
#else:
#	print('沒有找到檔案。')

def read_file(filename): #讀取檔案
	chat = []
	with open(filename, 'r' , encoding = 'utf-8-sig' ) as f:
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):#轉換
	new = []
	person = None
	for tline in chat:
		if tline == 'Allen':
			person = 'Allen'
			continue
		elif tline == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + tline)
	return new

def wirte_file(filename , chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	wirte_file('output.txt', chat)#（要轉換的檔名,寫入的list）
	print('轉檔完畢')


main()