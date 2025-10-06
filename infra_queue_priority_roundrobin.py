from collections import deque
import heapq

# -----------------------------
# 1) Queue (FIFO)
# -----------------------------
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Insere no fim da fila."""
        self._data.append(item)

    def dequeue(self):
        """Remove do início da fila. Levanta IndexError se vazia."""
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        """Olha o primeiro elemento sem remover."""
        if not self._data:
            return None
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"Queue({list(self._data)})"

# -----------------------------
# 2) Priority Queue (menor número == maior prioridade)
# -----------------------------
class PriorityQueue:

    def __init__(self):
        self._heap = []
        self._counter = 0  # desempate de inserções

    def push(self, item, priority: int):
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        return item, priority

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0

    def __repr__(self):
        preview = [(p, i) for (p, _, i) in self._heap]
        return f"PriorityQueue({preview})"

# -----------------------------
# 4) Round Robin
# -----------------------------
class Process:
    def __init__(self, pid: str, burst_time: int):
        self.pid = pid
        self.remaining = burst_time

    def __repr__(self):
        return f"{self.pid}(restante={self.remaining})"


def round_robin(processes, quantum: int = 2):

    q = Queue()
    for p in processes:
        q.enqueue(p)

    log = []
    while not q.is_empty():
        proc = q.dequeue()
        # Executa por no máximo 'quantum' ou até terminar
        slice_exec = min(proc.remaining, quantum)
        proc.remaining -= slice_exec
        log.append(f"{proc.pid} executou {slice_exec} unidades (restam {proc.remaining})")
        # Se ainda tem tempo, volta para o fim da fila
        if proc.remaining > 0:
            q.enqueue(proc)
    log.append("Todos os processos foram concluídos!")
    return log

# -----------------------------
# Demonstração / "main"
# -----------------------------
def demo_queue():
    print("=== Demonstração: Queue (FIFO) ===")
    q = Queue()
    for item in ["A", "B", "C"]:
        q.enqueue(item)
        print(f"enqueue({item}) -> {q}")
    print(f"peek() -> {q.peek()} (fila: {q})")
    while not q.is_empty():
        rem = q.dequeue()
        print(f"dequeue() -> {rem} (fila: {q})")
    print()

def demo_priority_queue():
    print("=== Demonstração: Priority Queue (1=Alta, 2=Média, 3=Baixa) ===")
    pq = PriorityQueue()

    # 3) 5 altas, 5 médias, 5 baixas
    altas  = [f"A{i}" for i in range(1, 6)]   # A1..A5
    medias = [f"M{i}" for i in range(1, 6)]   # M1..M5
    baixas = [f"B{i}" for i in range(1, 6)]   # B1..B5

    for a in altas:
        pq.push(a, priority=1)
    for m in medias:
        pq.push(m, priority=2)
    for b in baixas:
        pq.push(b, priority=3)

    print("Itens enfileirados (não necessariamente em ordem dentro do heap):")
    print(pq)

    print("\nOrdem de remoção (respeitando prioridades):")
    ordem = []
    while not pq.is_empty():
        item, pr = pq.pop()
        ordem.append((item, pr))
        print(f"pop() -> {item} (prioridade {pr})")

    # Observação (resumo)
    # Como 1 < 2 < 3, todos os 'Alta' saem primeiro, na ordem de chegada (estabilidade),
    # depois 'Média' e por fim 'Baixa'.
    print("\nObservações:")
    print("- Itens de prioridade '1' (Alta) foram atendidos antes dos de prioridade '2' e '3'.")
    print("- Dentro da mesma prioridade, a estrutura mantém a ordem de inserção (estável).")
    print(f"- Tamanho total processado: {len(ordem)} itens (5 altas, 5 médias, 5 baixas).")
    print()

def demo_round_robin():
    print("=== Demonstração: Round Robin (quantum=2) ===")
    processos = [
        Process("P1", 5),
        Process("P2", 7),
        Process("P3", 3),
    ]
    log = round_robin(processos, quantum=2)
    for linha in log:
        print(linha)
    print()

if __name__ == "__main__":
    demo_queue()
    demo_priority_queue()
    demo_round_robin()
