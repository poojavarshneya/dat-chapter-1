import csv

count_1981 = 0
songs = []
with open('rock.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		songs.append(row)
		if (row['Release Year'] == '1981'):
			count_1981 = count_1981 + 1

print "Total songs released in 1981 = ", count_1981
 
ss = sorted(songs, key=lambda song: int(song['PlayCount']), reverse=True)
print "Top 20 Songs:"
for i in range(0, 20):
	print i+1,".",ss[i]['Song Clean']
