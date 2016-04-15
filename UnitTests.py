def test_greedy():
    realOutput = greedy(63,coins) # calls greedy function
    expectedOutput = 6
    print "\n\n########TESTING GREEDY()##########\n\n "
    if (realOutput == expectedOutput): #compares outputs
        print "TEST PASSED \nEXPECTED: "+str(expectedOutput)+", VALUE: "+str(realOutput)
    else:
        print "TEST FAILED \nEXPECTED: "+str(expectedOutput)+", VALUE: "+str(realOutput)

def test_dynamic():
    realOutput = dynamic(63,coins) # calls dynamic function
    expectedOutput = 6
    print "\n\n########TESTING DYNAMIC()##########\n\n "
    if (realOutput == expectedOutput):#compares outputs
        print "TEST PASSED \nEXPECTED: "+str(expectedOutput)+", VALUE: "+str(realOutput)
    else:
        print "TEST FAILED \nEXPECTED: "+str(expectedOutput)+", VALUE: "+str(realOutput)
