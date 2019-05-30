
def read_file(filename):
	chatbox = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for data in f:
			chatbox.append(data.strip())
	return chatbox

def convert(lines):
	counter = 0
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_sticker_count, '個貼圖')
	print('Allen傳了', allen_image_count, '張圖片')

	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_sticker_count, '個貼圖')
	print('Viki傳了', viki_image_count, '張圖片')
	
	return allen_word_count
	return viki_word_count


def write_file(filename, new):
	with open(filename, 'w') as f:
		for chat in new:
			f.write(chat + '\n')


def main():
	lines = read_file('-line-Viki.txt')
	new = convert(lines)
	# write_file('output.txt',new)


main()