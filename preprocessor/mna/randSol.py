import sys
from random import uniform

deviation=0.4
dd=0.4

#Calls randomWrong 'cnt' times, ensuring that there is no repeated wrong answer
#for the correct answer 'cs'
def randomWrongs(cs,cnt):
	filled=0
	wrongs=list()
	while filled!=cnt:
		if type(cs)==tuple or type(cs)==list:
			tmp=list()
			for c in cs:
				tmp.append(randomWrong(c))
		else:
			tmp=randomWrong(cs)
		if tmp not in wrongs:
			wrongs.append(tmp)
			filled+=1
	return wrongs

#Generates and returns a wrong answer based on the correct (not complex) answer 'cs'
def randomWrong(cs):
	ldv=uniform(1-dd,1+dd)*deviation
	hdv=uniform(1-dd,1+dd)*deviation
	ws=uniform(1-ldv,1+hdv)*cs if cs!=0 else uniform(1-ldv,1+hdv)

	#if int(cs)==cs:
	#	ws=int(ws)
	#FIXME need more intelligent way

	if cs==ws:
		return randomWrong(cs)

	return ws

#Main used for testing only
def main(argv):
	for i in range(int(argv[2])):
		print(randomWrong(float(argv[1])))
	
if __name__ == "__main__":
	main(sys.argv)
