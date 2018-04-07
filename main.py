
import time

f = open("test.txt",'r')

n = int(f.readline())  # number of cases

dict = []

for i in xrange(0,n):
    dict.append(f.readline().split())

def damage(string):
    power = 1
    dmg = 0
    for i in xrange(0, len(string)):
        if string[i] == 'C':
            power = power*2
        else:
            dmg = dmg +power

    print "potenital damage is " + str(dmg)
    return dmg


def swap(shield,string):
    swaps =0
    string = list(string)
    while True:
        for i in xrange(0, len(string)-1): # TEST FOR ALL CASES
            if shield >= damage(string):  # if we are okay
                print "We're okay \n swaps : " + str(swaps)
                return False
            else:
                if string[len(string)-i-1] == 'S' and string[len(string)-i-2] == 'C':  # CASE CCCCCS

                    string[len(string) - i - 1] = 'C'
                    string[len(string) - i - 2] = 'S'
                    swaps = swaps + 1


                elif string[len(string)-i-1] == 'S' and string[len(string)-i-2] == 'S': # CASE CCCCSS
                    print "CURRENTLY NOTHING"
                    #time.sleep(1)








swap(3,'CSCSS')

