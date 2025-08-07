# Removendo uma fruta pelo indice

fruta = ["maca", "banana", "laranja", "pitaya"]
print(fruta)
print("----------------------------------------------------")
fruta_excluir = str(input(" Qual fruta deseja excluir? ")).strip().lower
print("----------------------------------------------------")

if fruta_excluir == "maca":
    fruta.pop(0)
    print(fruta)
    print("----------------------------------------------------")

elif fruta_excluir == "banana":
    fruta.pop(1)
    print(fruta)
    print("----------------------------------------------------")

elif fruta_excluir == "pitaya":
    fruta.pop(2)
    print(fruta)
    print("----------------------------------------------------")

elif fruta_excluir == "laranja":
    fruta.pop(3)
    print(fruta)
    print("----------------------------------------------------")

else:
    print("A fruta nao existe!")
fruta_nova = fruta.copy()
print(f" Lista de Frutas {fruta}")
print("----------------------------------------------------")

print(f" Lista de Frutas nova{fruta_nova}")
print("----------------------------------------------------")


# # INSERIR ITEM NA LISTA FRUTA_NOVA

fruta_nova.append(" melancia ")

print(f" Lista de Frutas {fruta}")
print("----------------------------------------------------")
print(f" Lista de Frutas nova{fruta_nova}")
print("----------------------------------------------------")