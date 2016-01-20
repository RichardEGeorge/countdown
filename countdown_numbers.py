#!/usr/bin/env python

import itertools;
import sys;

def operation(a,b,c):
	if c==1:
		return a+b;
	elif c==2:
		return a-b;
	elif c==3:
		return a*b;
	elif c==4:
		return a/b;
	elif c==5:
		return a;

operations = {};

operations[1]="+";
operations[2]="-";
operations[3]="*";
operations[4]="/";
operations[5]=" + 0 *";

n0 = {};

for j in range(1,7):
	n0[j-1] = int(sys.argv[j]);

target = int(sys.argv[7]);

print "Trying to make %d from %d,%d,%d,%d,%d,%d" % (target,n0[0],n0[1],n0[2],n0[3],n0[4],n0[5]);
print "";

n = {};

def display_result(n,m1,m2,m3,m4,m5,value):
	print "((((%d %s %d) %s %d) %s %d) %s %d) %s %d = %d" % (n[0],operations[m1],n[1],operations[m2],n[2],operations[m3],n[3],operations[m4],n[4],operations[m5],n[5],value);

def display_result2(a,b,o):
	if o==1:
		return str(a)+" + "+str(b);
	elif o==2:
		return str(a)+" - "+str(b);
	elif o==3:
		return str(a)+" * "+str(b);
	elif o==4:
		return str(a)+" / "+str(b);
	elif o==5:
		return str(a);
	
def apply_all_combinations(n,target,current_error):
	for m5 in range(1,6):
		for m4 in range(1,6):
			for m3 in range(1,6):
				for m2 in range(1,6):
					for m1 in range(1,6):

						value = operation(operation(operation(operation(operation(n[0],n[1],m1),n[2],m2),n[3],m3),n[4],m4),n[5],m5);

						error = abs(value - target);

						if current_error == -1:
							current_error = error;
							display_result(n,m1,m2,m3,m4,m5,value);

						else:

							if current_error > error:

								current_error = error;
								display_result(n,m1,m2,m3,m4,m5,value);
						
	return current_error;


if __name__=="__main__":

	current_error = -1;

	for p in itertools.permutations(range(0,6)):

		for j in range(0,6):
			n[j] = n0[p[j]];
	
		current_error = apply_all_combinations(n,target,current_error);

		if current_error == 0:
			break;

	if current_error == 0:
		print "";
		print "Solved";
		print "";
	else:
		print "";
		print "%d points away" % (current_error);
		print "";

