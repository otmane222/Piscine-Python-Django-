

def start():
	fd  = open('numbers.txt', 'r')
	data = fd.read()
	fd.close()
	if data == '':
		print('No data found in the file')
		return
	data = data.split(',')
	for i in data:
		print(i)

if __name__ == '__main__':
	start()