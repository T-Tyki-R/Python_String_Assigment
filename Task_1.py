# Product Review Analysis

# Task 1 Psuedocode
#     Define 2 list vars that stores strings = keywords and reviews
#     Define a string var that stores a default string
#     Create a func called keyword_Highlight that takes 2 para
#         Interate through the review list via loop
#         Define a condition statement where a keyword string is IN a review
#             if true -> store a replace() method where you replace the keyword with a uppercase version inside the string var
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

def keyword_Highlighter(keywords, reviews):
    for review in reviews: # look at each sentence individually
        review = review.lower() # make it all lowercase
        for keyword in keywords: # loop over keywords so we can see if we get any matches in the string
            if keyword in review: # if we do have a match, we need to replace it
                review = review.replace(keyword, keyword.upper())
        print(review) # prints each sentence for us


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
    pos_count = 0
    neg_count = 0
    review = ""
    print("\nAfter each review, we'll tally each one as either a positive or negative review\n")
    for i in text:
        review = i
        i = i.lower()
        for x in word1:
            if x in i:
                pos_count += 1
        for y in word2:
            if y in i:
                neg_count += 1
        print(f"{review}\nPostive Reviews Counter: {pos_count}\nNegative Review Counter: {neg_count}\n")
    return f"\"Python is an excellent product!\" Users rejoiced as Python was an amzaing product"  if pos_count > neg_count else "\"Avoid using Python at all cost!\" Users deemed Python to be trash..." 
 

# Task 3 Psuedocode
#     Create a func called review_Summary with a para
#         Interate through the para via loop
#               Define a conditional statement where a POSITIVE keyword is IN a review


def review_Summary(text):
    for i in text:
        return f"{i.partition(".")[0]}..." 
              

# print(keyword_Highlighter(keyword_finder, python_reviews))
# print(keyword_Counter(pos_word, neg_word, python_reviews))
print(review_Summary(python_reviews))
