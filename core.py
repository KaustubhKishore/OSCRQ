import debian

print(
    """
File Description: 
1. CLI Code goes here
2. CLI Options will create object based on what system is selected
3. Once object is created runner will be called which should at the end send scores to the DB
"""
)

obj = debian.Debian()
obj.runner()
print("Score: " + str(obj.score_getter()))
print("Non Compliant Score loss: " + str(obj.ncScore_getter()))