



def damage(string):
    power = 1
    dmg = 0
    for i in xrange(0, len(string)):
        if string[i] == 'C':
            power = power*2
        else:
            dmg = dmg +power
    return dmg

def swap(shield,string):
    swaps =0
    string = list(string)
    impossiblemeter = 0
    while True:
        for i in xrange(0, len(string)-1): # TEST FOR ALL CASES
            if shield >= damage(string):  # if we are okay
                return swaps
                break
            else:
                if string[len(string)-i-1] == 'S' and string[len(string)-i-2] == 'C':  # CASE CCCCCS

                    string[len(string) - i - 1] = 'C'
                    string[len(string) - i - 2] = 'S'
                    swaps = swaps + 1
                    impossiblemeter = 0

                elif impossiblemeter == len(string):
                    return "IMPOSSIBLE"
                    break

                elif string[len(string)-i-1] == 'S' and string[len(string)-i-2] == 'S': # CASE CCCCSS
                    impossiblemeter = impossiblemeter +1


dict = []
n = int(raw_input())
for i in xrange(0,n):
    dict.append(raw_input().split())
    print "Case #" + str(i + 1) + ": " + str(swap(int(dict[i][0]), dict[i][1]))









