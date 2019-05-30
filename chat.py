
def read_file(filename):
	chatbox = []
	with open(filename, 'r') as f:
		for data in f:
			chatbox.append(data.strip())
	return chatbox

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person: 
			new.append(person + ':' + line)
	return new

def write_file(filename, new):
	with open(filename, 'w') as f:
		for chat in new:
			f.write(chat + '\n')


def main():
	lines = read_file('chat.txt')
	new = convert(lines)
	write_file('output.txt',new)

main()