money=450
request=800
if(request>money):
    request=money
while request>0:
    if(request>=100 ):
        print "give 100"
        request=request-100
    else:
        if(request>=50):
            print "give 50"
            request=request-50
        else:
            if(request>=10):
                print "give 10"
                request=request-10
            else:
                if(request>=5 ):
                    print "give 5"
                    request=request-5
                else:
                     print "give "+str(request)
                     request=0

