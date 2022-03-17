myDict={
    "Fast":"In a quick manner",
    "Satyam":"A coder",
    "Marks":[5,3,6],
    "anotherdict":{
        "harry":"player"
    },
    1:2
}

print(myDict["Fast"])
print(myDict["Satyam"])
print(myDict["Marks"])
myDict["Marks"]=[34,67,89]   #It is mutable,unordered,cannot contain duplicate keys
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"]["harry"])
print(myDict[1])

print(myDict.keys())
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())

print(myDict)
updateDict={
    "Aman":"friend", #update the dictionary by adding 
    "Satyam":"Bro"   #replace because cannot contain duplicate keys
}
myDict.update(updateDict)
print(myDict)


# Both .get and [] will return value associated with key
print(myDict.get("Satyam"))
print(myDict["Satyam"])
# The difference between .get and [] syntax in Dictionary
print(myDict.get("Satyam2"))  #returns none as Satyam2 is not present in the dictionary
print(myDict["Satyam2"])      #thrpws an error as Satyam2 is not present in the dictionary