# que:wap to remove "" from a string s
# use  continue for removing "" from s

# s='apple is "good" for health'
# for i in s:
#     if i=='"':
#         continue
#     print(i,end="")

    # que: write a program remove all vovel from the string s

s='apple is "good" for health'
v="AEUIOaeuio"
for i in s:
        if i in v:
            continue
        print(i,end="") 
#  que: write a program remove all conconent from the string s
s='apple is "good" for health'
c="plghPLGH"
for i in s:
        if i in c:
            continue
        print(i,end="")    