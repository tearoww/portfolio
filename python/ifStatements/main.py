male = True
tall = True

if male and tall:
    print("I am for sure a tall male!")
# elif male or tall:
#     print("I'm male, tall or both!")
elif not male and tall:
    print("I am not a male but I am tall!")
elif male and not tall:
    print("I am a male but I am not tall!")
else:
    print("I am not a male or tall!")
