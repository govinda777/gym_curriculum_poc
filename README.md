
## Estratégia da POC: Trilha de Automação e RL

### 🛡️ Nível 1: Otimização Tática (Pathfinding & Async)
Nesta fase, o foco é a **lógica algorítmica** aplicada a um ambiente de arena.
* **Ação:** Desenvolver um agente capaz de navegar em um grid 2D (estilo RPG) para capturar objetivos enquanto desvia de obstáculos.
* **Componente Técnico:** Implementar algoritmos de **Pathfinding (A* ou Dijkstra)**. O "tempero" da gamificação aqui é o uso de **funções assíncronas** para gerenciar múltiplos agentes ou eventos em tempo real sem bloquear a execução principal.
* **KPI de Sucesso:** O agente deve encontrar o caminho mais curto em < 100ms e gerenciar colisões de forma eficiente.

### 🤖 Nível 2: Introdução ao Deep RL (Agente Huggy)
Aqui, saímos das regras manuais (if/else) para o **aprendizado por experiência**.
* **Ação:** Utilizar a biblioteca **Hugging Face Deep RL** para treinar um agente em um ambiente pré-existente (como o *Lunar Lander* ou o próprio *Huggy*).
* **Componente Técnico:** Implementação de algoritmos **Q-Learning** (para estados discretos) e **PPO (Proximal Policy Optimization)**. Definir uma **Reward Function** que penalize movimentos erráticos e premie a estabilidade.
* **KPI de Sucesso:** O agente deve atingir uma pontuação média positiva após 100.000 passos de treinamento, demonstrando que "entendeu" as leis da física do ambiente.

### 🏃 Nível 3: Generalização & Curriculum Learning (Parkour 2D)
A fase final foca na **estabilidade do aprendizado** em ambientes que mudam de dificuldade.
* **Ação:** Criar um ambiente de "Parkour 2D" onde os obstáculos (buracos, plataformas, altura) aumentam de complexidade conforme o agente melhora.
* **Componente Técnico:** Implementar **Automatic Curriculum Learning (ACL)**. Em vez de jogar o agente em um nível impossível, o sistema ajusta o ambiente dinamicamente. Isso evita a "falha catastrófica" (onde o agente desaprende tudo ao encontrar um desafio muito difícil).
* **KPI de Sucesso:** O agente deve ser capaz de completar um nível gerado proceduralmente que nunca viu antes, provando a generalização do modelo.

---

### Stack Tecnológica Sugerida

| Camada | Ferramenta |
| :--- | :--- |
| **Ambiente** | Gymnasium (OpenAI Gym) / Pygame |
| **Framework RL** | Stable Baselines3 / Hugging Face Transformers |
| **Linguagem** | Python 3.10+ |
| **Orquestração** | NotebookLM ou Google Colab para prototipagem |

---

> **Dica de Engenharia:** Para o Nível 1, você pode usar o **CodeCombat** como inspiração para a interface, mas implementar a lógica de `pathfinding` em um repositório Python separado para garantir total controle sobre o custo computacional.

