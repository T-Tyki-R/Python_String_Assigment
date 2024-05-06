# Product Review Analysis

# Task 1 Psuedocode
#     Define 2 list vars that stores strings = keywords and reviews
#     Define a string var that stores a default string
#     Create a func called keyword_Highlight that takes 2 para
#         Interate through the review list via loop
#         Define a condition statement where a keyword string is IN a review
#             if true -> store a replace() method where you replace the keyword with a upper version inside the string var
#             print the string var             

keyword_finder = ["good", "excellent", "bad", "poor", "average"]
pos_word = ["good", "excellent"]
neg_word = ["bad", "poor", "average"]
python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." 
]   

def keyword_Highlighter(keyword, text):   
    cap_words = ""   
    for word in range(len(text)):       
        if keyword[word] in text[word].lower():
            x = keyword[word].upper()
            cap_words += x + " "
    print(f"{cap_words}") # <- prints out all the keywords in caps, but not the sentences
           
# Task 2 Psuedocode
#     Create a func called keyword_Score with 3 para
#         Define 2 integer vars = posCount and negCount
#         Interate through the review list via loop
#               Define a conditional statement where a POSITIVE keyword is IN a review
#                   if true -> increment posCount var by 1
#               Define a conditional statement where a NEGATIVE keyword is IN a review
#                   if true -> increment negCount var by one
#         return the 2 integer vars

def keyword_Counter(word1, word2, text):
    posCount = 0
    negCount = 0
    for i in range(len(text)):
        if word1[i] in text[i]:
            posCount += 1
        if word2[i] in text[i]:
            negCount += 1
    print(f"Postive Reviews Count for Python: {posCount}\nNegative Review Count for Python: {negCount}") 
# ^ Getting an IndexError 

# Task 3 Psuedocode
#     Create a func called review_Summary with a para
#         Interate through the para via loop
#               Define a conditional statement where a POSITIVE keyword is IN a review


def review_Summary(text):
    for i in range(len(text)):
        print(f"{text[i].partition(".")[0]}...") 
              

print(keyword_Highlighter(keyword_finder, python_reviews))
# print(keyword_Counter(posWord, negWord, python_Reviews))
# print(review_Summary(python_Reviews))
