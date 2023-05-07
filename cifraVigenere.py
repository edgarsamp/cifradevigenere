import math

class Vigenere:
    def __init__(self):
        self.alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.ling_props = {
            "PT": [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.30, 1.28, 6.18, 0.40, 0.02, 2.78, 4.74, 5.05, 10.73, 2.52, 1.20, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47],
            "EN": [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
        }
        self.tamanho_max_chave = 10

    def _tratar_texto(self, texto):
        # mapeamento de caracteres acentuados para caracteres sem acento
        mapa_acentos = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i',
            'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u',
            'ç': 'c'
        }

        # remove acentos
        texto_tratado = ""
        for letra in texto:
            if letra in mapa_acentos:
                letra = mapa_acentos[letra]
            texto_tratado += letra

        # remove pontuações
        for p in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n0123456789—“”":
            texto_tratado = texto_tratado.replace(p, "")

        return texto_tratado.upper()
    
    def cifrar(self, mensagem, key):
        key = self._tratar_texto(key)
        mensagem = self._tratar_texto(mensagem)
        mensagem_cifrada = ""
        for i, letra in enumerate(mensagem):
            k = key[(i)%len(key)]
            ki = self.alfabeto.index(k)

            li = self.alfabeto.index(letra)
            mensagem_cifrada += self.alfabeto[(li+ki) % 26]
        
        return mensagem_cifrada

    def decifrar(self, mensagem, key):
        key = self._tratar_texto(key)
        mensagem = self._tratar_texto(mensagem)

        mensagem_decifrada = ""

        for i, letra in enumerate(mensagem):
            k = key[(i)%len(key)]
            ki = self.alfabeto.index(k)

            li = self.alfabeto.index(letra)
            mensagem_decifrada += self.alfabeto[(li-ki) % 26]
        
        return mensagem_decifrada
    
    def _encontra_letra(self, probability, language):
        diferencas =[]

        #calcula a diferença entre a probabilidade da letra atual na lingua nativa do texto
        for i in range(26):
            soma = 0
            for j in range(26):
                soma += abs(probability[(i+j) % 26] - self.ling_props[language][j])
            
            diferencas.append(soma)

        #retorna a que tem a menor diferença
        return self.alfabeto[diferencas.index(min(diferencas))]

    def _encontrar_chave(self, text, language):
        tamanho = self._tamanho_chave(text)
        chave = ""

        for i in range(tamanho):
            freq_letra_bloco = {}

            # Divide o texto em blocos do tamanho da chave
            # e calcula a quantidade de vezes em que cada letra aparece na posição i do bloco
            for j in range(i, len(text), tamanho):
                freq_letra_bloco[text[j]] = freq_letra_bloco.get(text[j], 0) + 1

            prop_alfabeto = []

            # Calcula a probabilidade de cada letra do alfabeto nos blocos
            for letra in self.alfabeto:
                prop_alfabeto.append(100*freq_letra_bloco.get(letra, 0)/sum(freq_letra_bloco.values()))
            
            chave += self._encontra_letra(prop_alfabeto, language)
        return chave

    def _tamanho_chave(self, mensagem):
        tamanhos_possiveis = []

        for tamanho in range(2, len(mensagem)-2):
            dist = []
            for i in range(len(mensagem)-2):
                for j in range(i+tamanho, len(mensagem)-tamanho, tamanho):
                    if mensagem[i:i+3] == mensagem[j:j+3]:
                        dist.append(j-i)
            if dist:
                gcd = self._calcula_mdc(dist)
                if gcd > 1 and tamanho < self.tamanho_max_chave:
                    tamanhos_possiveis.append((tamanho, len(dist)/(len(mensagem)/gcd)))
        return [x[0] for x in sorted(tamanhos_possiveis, key=lambda x: x[1], reverse=True)[:5]][0]

    def _calcula_mdc(self, dist):
        gcd = dist[0]
        for i in dist[1:]:
            gcd = math.gcd(gcd, i)
        return gcd

    def ataque(self, mensagem):
        mensagem = self._tratar_texto(mensagem)
        chaves = []

        chaves.append(self._encontrar_chave(mensagem, "PT"))
        chaves.append(self._encontrar_chave(mensagem, "EN"))

        return chaves