# Atividade – Infraestrutura de Software (ADS 3º Período)

**Linguagem utilizada:** Python 3.11+  
**Disciplina:** Infraestrutura de Software  
**Tema:** Estruturas de Filas (Queue, Priority Queue) e Escalonamento Round Robin  

---

## Objetivos da Atividade

1. Pesquisar e implementar uma **fila (Queue)**.  
2. Verificar se existe e implementar uma **fila de prioridade (Priority Queue)**.  
3. Definir 5 itens de **alta**, 5 de **média** e 5 de **baixa prioridade**, executar e observar o comportamento.  
4. Implementar uma **simulação de Round Robin**, com:
   - Processos: P1 (5), P2 (7), P3 (3)
   - Quantum = 2
   - Operações apenas `enqueue` e `dequeue`.

---

## 1. Implementação da Queue (FIFO)

A estrutura **Queue** foi criada com `collections.deque`, que permite inserir no fim e remover do início de forma eficiente.

### Print 1 – Execução da Queue
<img width="1854" height="1044" alt="image" src="https://github.com/user-attachments/assets/924dc5c2-238a-43ae-97b9-cb2fc69fec4c" />

### Observação

A fila segue a lógica **FIFO** (First In, First Out): o primeiro elemento inserido é o primeiro a ser removido.

---

## 2. Implementação da Priority Queue

Foi utilizada a biblioteca `heapq`, que cria uma **min-heap** (menor número = maior prioridade).

* 1️⃣ = Alta prioridade
* 2️⃣ = Média prioridade
* 3️⃣ = Baixa prioridade

Para manter a ordem de inserção dentro da mesma prioridade, foi adicionado um contador de desempate.

### Print 2 – Execução da Priority Queue
<img width="1854" height="1044" alt="image" src="https://github.com/user-attachments/assets/e6aae15f-ce3f-4ea2-8405-1590db34df30" />

### Observação

* Todos os itens de **prioridade alta (1)** são processados primeiro.
* Dentro de cada prioridade, a **ordem de inserção** foi mantida.
* Isso demonstra o funcionamento de uma **fila de prioridade estável**.

---

## 3. Simulação de Round Robin (Quantum = 2)

Cada processo executa no máximo 2 unidades de tempo.
Quando ainda há tempo restante, o processo volta ao fim da fila.
Quando termina, é removido da fila definitivamente.

### Código principal:

### Print 3 – Execução do Round Robin
<img width="1854" height="1044" alt="image" src="https://github.com/user-attachments/assets/e53e27bc-9946-4fac-b2f3-cea995f6e6c9" />

### Observação

* O escalonamento Round Robin distribui o tempo de CPU entre os processos.
* Nenhum processo monopoliza o processador; todos recebem tempo de execução proporcional.
* O algoritmo continua até que todos os processos sejam concluídos.

---

## Conclusão

Com esta implementação, observamos:

* A **fila comum** (Queue) segue a ordem de chegada.
* A **fila de prioridade** respeita os níveis definidos e mantém estabilidade.
* O **Round Robin** demonstra um escalonamento equilibrado, simulando o comportamento real de sistemas operacionais multitarefa.

