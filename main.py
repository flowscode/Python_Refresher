# a = "heosoososo000"
import functions

mylist = ["RED", "BLUE", "GREEN", "PINK"]
myTuple = ("RED", "BLUE", "GREEN", "PINK")
mySet = {"RED", "BLUE", "GREEN", "PINK"}
myDiction = {
    "brand": "ford",
    "model": "focus",
    "year": "2003"
}

print(myDiction["year"])
print(len(myDiction))
print()
print()

functions.function("hello")

i = 0
while i <= 7:
    print(i)
    i += 1
else:
    print("i is no longer less than or equal to 7")
    print("i = ", i)
