import os
import pyaes

## Abrir o arquivo que está criptografado

file_name = 'folha.txt.ransowarextrad'
file = open(file_name, 'rb')
file_date = file.read()
file.close()

## Setar a chave de descriptografia

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)


## Removendo o arquivo  criptografado

os.remove(file_name)


## Criar um novo arquivo descriptografado 

new_file = 'folha.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()

