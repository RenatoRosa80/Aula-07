fruta = ["maca", "banana", "laranja", "pitaya"]

print(f" Todas as frutas:  {fruta[0]}")
print(f" Todas as frutas:  {fruta[3]}")
print(f" Todas as frutas:  {fruta[-2]}")
tamanho_lista = len(fruta)
print("-----------------------------------------------------------")
print(f" Tamanho da lista:  {tamanho_lista}")
print("-----------------------------------------------------------")
fruta[1] = "uva"
print("------------------------------------------------------------")
print(f" Tamanho da lista:  {fruta}")
print("------------------------------------------------------------")
fruta.insert(1, "Abacaxi")
print(f" Lista de fruta atualizada: {fruta}")
tamanho_lista = len(fruta)
print("--------------------------------------------------------------")
print(f" Novo tamanho da lista: {tamanho_lista}")
print("--------------------------------------------------------------")
