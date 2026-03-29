# Nível 1: Otimização Tática (Pathfinding & Async)

Nesta fase, o foco é a **lógica algorítmica** aplicada a um ambiente de arena. Exploramos como resolver problemas de navegação de forma eficiente e concorrente.

## 🎯 Objetivos
* Implementar o algoritmo **A*** para encontrar o caminho mais curto.
* Usar **Python Asyncio** para simular múltiplos agentes movendo-se simultaneamente sem bloquear a execução.

## 📂 Arquivos
* `grid_env.py`: Define o mapa 2D com obstáculos aleatórios.
* `pathfinding.py`: Contém a lógica do algoritmo A* e a heurística de Manhattan.
* `main.py`: Ponto de entrada que cria o ambiente e coordena os agentes assíncronos.
* `test_performance.py`: Benchmark para medir o tempo de execução do algoritmo.

## 🚀 Como Executar
```bash
PYTHONPATH=. python3 level_1_pathfinding/main.py
```

### 📤 Saída Esperada (Terminal)
```text
Agent Agent 1 starting from (0, 0) to (29, 29)
Agent Agent 1 found path in 4.5ms
Agent Agent 2 starting from (0, 29) to (29, 0)
Agent Agent 2 found path in 4.2ms
Agent Agent 1 reached (29, 29)!
Agent Agent 2 reached (29, 0)!
```

## 🧠 Conceitos Chave
### Pathfinding (A*)
O algoritmo A* combina a distância percorrida com uma estimativa (heurística) da distância restante para encontrar o caminho ideal rapidamente.

### Concorrência Assíncrona
Em vez de esperar que um agente termine sua jornada para começar o próximo, o `asyncio` permite que o processador alterne entre as tarefas, simulando movimento em tempo real.
