# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr -s " " "\n" | sort | uniq -c | sort -r | awk '{print $2, $1}'

"""
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:
  words.txt contains only lowercase characters and space ' ' characters.
  Each word must consist of lowercase characters only.
  Words are separated by one or more whitespace characters.


➜ cat Words.txt
the day is sunny the the
the sunny is is
➜ cat Words.txt| tr -s ' ' '\n'
the
day
is
sunny
the
the
the
sunny
is
is
➜ cat Words.txt| tr -s ' ' '\n' | sort
day
is
is
is
sunny
sunny
the
the
the
the
➜ cat Words.txt| tr -s ' ' '\n' | sort | uniq -c
1 day
3 is
2 sunny
4 the
➜ cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r
4 the
3 is
2 sunny
1 day
➜ cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
the 4
is 3
sunny 2
day 1
"""
