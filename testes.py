orig = {
    'A': 1,
    'B': 2,
    'C': 3
}

extra = {
    'D': 4,
    'E': 5
}

dest = {}

#dest.update(orig['A'])


#print(orig['A'])
#print(orig)

nome = "aline"
total = 0 
for letra in nome:
    print(letra)
    total += 1 
#print(total)


#Dado um parametro *args qual o tipo do objeto args?
#tuple 

#Dado um parametro **kwargs qual o tipo do objeto kwargs?
#dict 

x = 3
y = 2

print(f"/ operator {x/y}")
print(f"// operator {x//y}")
print(f"% operator {x%y}")