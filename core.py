import debian

print("""
File Description: 
1. CLI Code goes here
2. CLI Options will create object based on what system is selected
3. Once object is created runner will be called which should at the end send scores to the DB

Tasks:
1. TODO: Save audit output as json so that it can be safely used later(Like when saving everything to mongo)
2. TODO: Figure out good CLI library.
3. TODO: Descide what coding part you want to take up and discuss timelines with others.
4. TODO:
""")

obj = debian.Debian()
obj.runner()
print("Score: " + str(obj.score_getter()))