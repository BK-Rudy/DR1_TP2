# ------------------- Questão 1 ------------------- #

# Função 1
def funcao1(n):
    for i in range(n):
        print(i)

"""
Resposta: O laço for percorre de "0" até "n − 1", realizando uma operação constante para cada iteração. 
A função executa "n" iterações, resultando em uma complexidade linear O(n).
"""

# Função 2
def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

"""
Resposta: A função possui dois laços "for" aninhados. O laço externo executa "n" iterações, e o laço interno 
também executa "n" iterações, resultando em um total de "n × n = n²" operações. A complexidade é quadrática O(n²).
"""

# Função 3
def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)

"""
Cada chamada de funcao3(n) resulta em duas novas chamadas: funcao3(n - 1) e funcao3(n - 2). 
O número de chamadas cresce à medida que n aumenta. A árvore de recursão tem aproximadamente 2^n chamadas no pior caso, 
resultando em uma complexidade exponencial O(2^n).
"""


# ------------------- Questão 2 ------------------- #

def question2():
    import random

    list = [random.randint(1, 1000000) for _ in range(5000000)]

    def MergeSort(array):
        if len(array) > 1:
            
            middle = len(array) // 2
            start = array[:middle]
            end = array[middle:]
        
            MergeSort(start)
            MergeSort(end)
            
            s = 0 # id início
            e = 0 # id final
            m = 0 # id merge
            
            while s < len(start) and e < len(end):
                if start[s] < end[e]:
                    array[m] = start[s]
                    s += 1
                else:
                    array[m] = end[e]
                    e += 1
                m += 1
            
            while s < len(start):
                array[m] = start[s]
                s += 1
                m += 1
            
            while e < len(end):
                array[m] = end[e]
                e += 1
                m += 1

    MergeSort(list)
    print(list[:100])

"""
Resposta: A complexidade de tempo da função MergeSort é O(n log n) porque o algoritmo divide o 
array em duas metades recursivamente (O(log ⁡n)) e, a cada nível, percorre todos os elementos 
para combiná-los (O(n)). Assim, a combinação dessas etapas resulta em O(n log n).
"""


# ------------------- Questão 3 ------------------- #
def question3():
    import random
    import time

    # Força Bruta O(n²):
    def Rough(list):
        duplicates = []
        
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                if list[i] == list[j] and list[i]:
                    duplicates.append(list[i])
                    
        return duplicates


    # Estrutura Eficiente O(n):
    def Efficient(list):
            arr = [0] * (len(list)+1)
            
            duplicates = []  

            for num in list:
                arr[num] += 1 
                if arr[num] == 2: 
                    duplicates.append(num)

            return duplicates

    array = list(range(1, 20001))
    array += [100, 200, 300, 400, 500]

    random.shuffle(array)

    start_time_rough = time.time()
    print("Duplicados (Rough):", Rough(array))
    rough_time = time.time() - start_time_rough

    start_time_efficient = time.time()
    print("Duplicados (Efficient):", Efficient(array))
    efficient_time = time.time() - start_time_efficient

    print(f"Tempo de execução da função Rough: {rough_time:.2f} segundos.")
    print(f"Tempo de execução da função Efficient: {efficient_time:.2f} segundos.")


# ------------------- Questão 4 ------------------- #

class Pilha:
    def __init__(self):
        self.itens = []
        
    def is_empty(self):
        return len(self.itens) == 0
        
    def push(self, item):
        self.itens.append(item)

    def ascending(self):
        itens = []
        while self.itens:
            itens.append(self.pop())
            
        itens.sort()
    
        for item in itens:
            self.push(item)

    def display(self):
        print("Pilha:", self.itens)

def question4():
    pilha = Pilha()
    pilha.push(10)
    pilha.push(90)
    pilha.push(80)
    pilha.push(15)
    pilha.push(30)

    pilha.display()
    pilha.ascending()
    pilha.display()


# ------------------- Questão 5 ------------------- #
    
class Pilha2:
    def __init__(self):
        self.itens = []
        
    def is_empty(self):
        return len(self.itens) == 0
        
    def push(self, item):
        self.itens.append(item)

    def display(self):
        print("Pilha:", self.itens)
        
    def tarefa_no_topo(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

def question5():
    pilha = Pilha2()
    pilha.push("Tarefa 1")
    pilha.push("Tarefa 2")
    pilha.push("Tarefa 5")
    pilha.push("Tarefa 4")
    pilha.push("Tarefa 3")

    pilha.display()
    print(pilha.tarefa_no_topo())


# ------------------- Questão 6 / Questão 7 ------------------- #
    
class Pilha3:
    def __init__(self):
        self.itens = []
        
    def is_empty(self):
        return len(self.itens) == 0
        
    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def display(self):
        print("Pilha:", self.itens)
    
    def odd(self):
        count = 0
        items = []
        
        while not self.is_empty():
            order = self.pop()
            if order % 2 != 0: 
                count += 1
            items.append(order)
        
        while items:
            self.push(items.pop())
        
        return count
    
    def even(self):
        count = 0
        items = []
        
        while not self.is_empty():
            order = self.pop()
            if order % 2 == 0: 
                count += 1
            items.append(order)
        
        while items:
            self.push(items.pop())
        
        return count

def question6():
    pilha = Pilha3()
    pilha.push(1)
    pilha.push(2)
    pilha.push(3)
    pilha.push(4)
    pilha.push(5)
    pilha.push(6)
    pilha.push(7)
    pilha.push(8)
    pilha.push(9)
    pilha.push(10)
    pilha.push(11)
    pilha.push(13)
    pilha.push(15)

    pilha.display()

    #Questão 6
    print("Ímpares:", pilha.odd())

    #Questão 7
    print("Pares:", pilha.even())


# ------------------- Questão 8 ------------------- #

def question8():
    def inverter_fila(queue):
        inverted_queue = queue
        
        inverted_queue[0], inverted_queue[-1] = inverted_queue[-1], inverted_queue[0]

        return inverted_queue

    queue = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4", "Paciente 5"]

    print("Fila: ", queue)
    print("Fila invertida: ", inverter_fila(queue))


# ------------------- Questão 9 ------------------- #
def question9():
    def order(list):
        n = len(list)
        
        for i in range(n):
            check = False
            for j in range(0, n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                    check = True

            if (check == False):
                break


    list = [3, 35, 21, 100, 69, 92, 32, 4, 2, 1]
    print(list)
    
    order(list)

    print(list)


# ------------------- Questão 10 ------------------- #
def question10():
    def odd(list_id):

        total = 0

        for i in list_id:
            if i % 2 != 0:
                total += 1
            
        return total

    id_books = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]

    print(odd(id_books))



# ------------------- Questão 11 ------------------- #

class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo cliente: {cliente_atendido}")
            return cliente_atendido
        else:
            print("Não há clientes na fila.")
            return None

    def tamanho_fila(self):
        return len(self.fila)

def question11():
    queue = FilaAtendimento()

    queue.adicionar_cliente("Cliente 1")
    queue.adicionar_cliente("Cliente 2")
    queue.adicionar_cliente("Cliente 3")
    queue.adicionar_cliente("Cliente 4")
    queue.adicionar_cliente("Cliente 5")

    print("Tamanho fila: ", queue.tamanho_fila())

    queue.atender_cliente()

    print("Tamanho fila: ", queue.tamanho_fila())

    queue.atender_cliente()
    queue.atender_cliente()

    print("Tamanho fila: ", queue.tamanho_fila())


# ------------------- Questão 12 ------------------- #

class TabelaHash:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def inserir(self, chave, valor):
        idx = self.hash(chave)

        for pair in self.table[idx]:
            if pair[0] == chave:
                pair[1] = valor
                return

        self.table[idx].append([chave, valor])
        self.size += 1

    def buscar(self, chave):
        idx = self.hash(chave)

        for pair in self.table[idx]:
            if pair[0] == chave:
                return pair[1]

        return None
        
    def remover(self, chave):
        idx = self.hash(chave)

        for i, pair in enumerate(self.table[idx]):
            if pair[0] == chave:
                del self.table[idx][i]
                self.size -= 1
                return True

        return False
    
    def __str__(self):
        result = []

        for listTable in self.table:
            for pair in listTable:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{ " + ", ".join(result) + " }"


def question12():
    hashTable = TabelaHash()
    hashTable.inserir("key1", "Valor 1")
    hashTable.inserir("key2", "Valor 2")
    hashTable.inserir("key3", "Valor 3")

    print(hashTable.buscar("key2"))

    hashTable.remover("key2")

    print(hashTable)


#Execução
if __name__ == "__main__":
    print("Escolha a questão para executar:")
    print("2 - Questão 2")
    print("3 - Questão 3")
    print("4 - Questão 4")
    print("5 - Questão 5")
    print("6 - Questão 6 / Questão 7")
    print("8 - Questão 8")
    print("9 - Questão 9")
    print("10 - Questão 10")
    print("11 - Questão 11")
    print("12 - Questão 12")

    selected = input("Digite o número da função a ser executada: ")

    functions = {
        "2": question2,
        "3": question3,
        "4": question4,
        "5": question5,
        "6": question6,
        "8": question8,
        "9": question9,
        "10": question10,
        "11": question11,
        "12": question12
    }

    if selected in functions:
        functions[selected]()
    else:
        print("Opção inválida!")