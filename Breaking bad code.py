cast = ["Mr. walter white","Saul goodman","walter junior","hank","Mr. gus","skyler white","tuco","jesse pinkman"]

print("Enter a Breaking Bad dialogue:")

user_input = input()


if user_input == "yo yo 1,4,8,3 to the 6 to 9 reprsent in the ABQ.what up..." :
    speaker = "jesse pinkman"
if user_input == "I am the danger, I am the danger.":
    speaker = "Mr. walter white"
elif user_input == "Say my name":
    speaker = "Mr. walter white"
elif user_input == "Better call Saul":
    speaker = "Saul goodman"
elif user_input == "Tread lightly":
    speaker = "Mr. walter white"
elif user_input == "Yeah science":
    speaker = "walter junior"
elif user_input == "I am the one who knocks":
    speaker = "Mr. walter white"
elif user_input == "Tight tight tight":
    speaker = "tuco"
elif user_input == "I hide in plain sight":
    speaker = "Mr. gus"
elif user_input == "Say hello to my little friend":
    speaker = "tuco"
elif user_input == "My name is ASAC Schrader":
    speaker = "hank"
elif user_input == "You are not the boss of me":
    speaker = "walter junior"
elif user_input == "Shut up Skyler":
    speaker = "Mr. walter white"
elif user_input == "What is wrong with you":
    speaker = "skyler white"
elif user_input == "A man provides":
    speaker = "Mr. gus"
elif user_input == "A man provides for his family":
    speaker = "Mr. gus"
elif user_input == "I will kill your wife":
    speaker = "Mr. gus"
elif user_input == "I built an empire":
    speaker = "Mr. gus"
    print("You are godammn right.")
else:
    speaker = "unknown"
if speaker!="unknown":
    print("You are godammn right. You have watched breaking bad with interest.")
    score=1
    print("Your score is", score)

elif user_input== "end":
    print("Thanks for playing,"+"Game ended") 
i=0
while i< len(cast):
    print(cast[i])
    i+=1