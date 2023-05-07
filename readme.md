# Cifra de Vigenère

Este é um projeto de criptoanálise de cifra de Vigenère desenvolvido em Python. Ele tem como objetivo permitir a cifragem e decifragem de mensagens utilizando a cifra de Vigenère, bem como a realização de ataques para quebrar a cifra.

###Funcionalidades
O projeto conta com as seguintes funcionalidades:

- Cifragem de mensagens utilizando a cifra de Vigenère
- Decifragem de mensagens cifradas com a cifra de Vigenère
- Ataque para quebrar a cifra de Vigenère e encontrar a chave utilizada para cifrar a mensagem.

###Como utilizar
A execução do programa é feita através do arquivo **main.py**. O programa recebe como entrada dois arquivos: **input.txt** e **output.txt**. O arquivo **input.txt** deve conter a mensagem a ser cifrada, decifrada ou atacada e a chave para os dois primeiros casos. O arquivo output.txt é onde o resultado da operação é salvo.

As informações que devem constar no arquivo input.txt são as seguintes:

A primeira linha deve conter a chave de cifração (caso deseja cifrar ou decifrar)
A segunda linha deve conter a mensagem a ser cifrada, decifrada ou atacada.

Exemplo de arquivo input.txt para cifragem:

```
Chave
Ataque a base de operações 3
```

Exemplo de arquivo input.txt para ataque:

```
CAALYGHBVWGKEJTGYAXSGZ
```

O resultado da operação será salvo no arquivo output.txt. Caso a operação seja de cifragem ou decifragem, o arquivo conterá apenas a mensagem resultante. Já no caso de operação de ataque, o arquivo conterá as chaves encontradas para cada idioma (português e inglês).
