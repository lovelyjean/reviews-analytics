data = []
count = 0
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length = length + (len(line))
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('Total data:', len(data))

print('Average length:', length / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])