import random
def greet():
    name=input("ENTER YOUR NAME\n")
    print("Hello ", name)
    print("WELCOME IN THE GAME ")
    
word_list=["apple","banana","cat","bat","float","boat"]

chosen_word=random.choice(word_list)

len_word=len(chosen_word)
display=[]
for _ in range (len_word):
    display += "_"
print(display)

print(chosen_word)

lives=3
while lives>0:
    guess=input("guess a letter ").lower()
    for position in range(len_word):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter          
    print(display)
            