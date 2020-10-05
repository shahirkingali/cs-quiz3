#sportfile-sf
# sf = open("sports.txt", "w")
# sf.write('basketball\n softball\n football\n baseball\n track\n')
# sf.close()

# sf = open("sports.txt")
# sf = sf.read()
# print(sf)

#sample code
# def c(a):
#     b=0
#     for i in a:
#         b+=i
#     return b

# print(c([4,5,2,-3]))

#rewritten code
# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum

# print(listsum([4,5,2,-3]))


hats = {'snapback':10, 'beanie':5, 'baseballcap':3}
hats['weird top hat'] = 1
hats['snapback'] = 11
del hats['weird top hat']
for key, value in hats.items(): 
    print(f'{key}: {value}')

