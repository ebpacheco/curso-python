# conversao de tipos, coercao
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro 
# tipos imutaveis e primitivos:
# str, int, float, bool

print (1 + 1)
print ('a' + "b")

print("1", type("1")) # str
print(int("1"), type(int("1"))) # int

#print ("1" + 1) #Erro
print (int("1") + 1) # 2

print (float("1") + 1) # 2.0

print(bool("")) #False
print(bool(" ")) # True

# print(10 + "a") # Erro
print (str(10) + "a")