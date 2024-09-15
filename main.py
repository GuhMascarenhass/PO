def choice_min_max():
    escolha = int(input("1 para Max 2 para Min"))
    return escolha

def size_simplex():
    d = int(input("Número de variáveis de decisão: "))
    r = int(input("Número de restrições: "))
    return(d, r)

decision = list()
obj = list()
d, r = size_simplex() 

if choice_min_max() == 1:
   for y in range(0, d): 
        obj.append(int(input("Valor do objetivo: ")))

        
   for y in range(0,r):
      decision.append([])
      for x in range(0, d+1):
         if x == d:
            decision[y].append(int(input("Valor final da restrição: ")))
         else:
            decision[y].append(int(input("Valor variavel de restrição")))

print(decision)        
'''  if escolha() == 2:
       
    elif max_min == 0:'''
