words=input("enter a string:")
words_list=list(map(str,words.split())) 
positive_words=["good","happy","great","wow","awesome"]
negative_words=["sad","worst","bad","unhappy"]
if words in positive_words:    
    print("Positive words")
elif words in negative_words:
    print("negative words")   
