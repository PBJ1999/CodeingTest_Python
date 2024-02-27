dataset = ["abcabc", "bbab", "cccc", "abaaa", "bdfad"]

total = 0

for data in dataset:
    count = data.count('a')
    total = total + count

print('a의 개수는', total)
