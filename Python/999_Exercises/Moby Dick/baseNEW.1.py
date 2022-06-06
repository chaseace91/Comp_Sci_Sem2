sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"



with open('moby.txt') as f:
    counter = 0
    for line in f:
        sentence = line.strip()
        word = ""
        
        for x in range(len(sentence)):
            word = word + sentence[x]
            if sentence[x:x+5]==" ":
                if "whale" in word or "Whale" in word:
                    counter=counter+1
                    word = ""
    print(counter)

f.close()










#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
