#!/usr/bin/env python

import sys;

def frequency_for_word(w):
	result = {};
	for c in w:
		if c not in result:
			result[c]=1;
		else:
			result[c]+=1;
	return result;

def can_make_word(keyword,test):
	for ch in test:
		if ch not in keyword:
			return False;
		else:
			if keyword[ch] < test[ch]:
				return False;

	return True;

def test_countdown2(word):
	d0 = frequency_for_word(letters.strip());

	with open("words.txt") as f:
		for l1 in f.readlines():
	
			l = l1.strip();
	
			d1 = frequency_for_word(l);
			
			if can_make_word(d0,d1):
				yield l;


def test_countdown(word):
	best = {};

	for a in test_countdown2(word):
		if len(a) not in best:
			best[len(a)] = a;
		else:
			best[len(a)] += " ";
			best[len(a)] += a; 

	n_max = 0;
	for j in best:
		if n_max < j:
			n_max = j;

	for j in range(1,n_max+1):
		if j in best:
			print "%d: %s" % (j,best[j]);

if __name__=="__main__":

	if len(sys.argv)<=1:
		print "usage: python countdown.py (letters)"
		print "";
		print "Finds English words that can be formed using (letters)";
		print "";
	else:
		letters = sys.argv[1].strip();
		print "Looking for words that can be made using ``%s''" % (letters);
		print "";
		test_countdown(letters);
		print "";

