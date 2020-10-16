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
4. TODO: Maybe we can convert the core audit commands and outputs to a json file 
         which is parsed and according the the input 
         and expected output in that json our engine gets the score. This will complicate stuff but might reduce our code size

5. TODO: Maybe a good idea to shift helper functions which will be common for all operating systems to another class and then classes like Debian can extend those classes
6. TODO: Rather than calling all the functions manually in runner we can use dir(Debian) which will give a list of all functions. Extract list of functions and then auto run.
""")

obj = debian.Debian()
obj.runner()
print("Score: " + str(obj.score_getter()))
print("Non Compliant Score loss: " + str(obj.ncScore_getter()))