# Nível 3: Generalização & Curriculum Learning (Parkour 2D)

O nível final foca na **estabilidade do aprendizado** em ambientes que mudam de dificuldade. O agente deve aprender a completar um percurso de "Parkour" enquanto os obstáculos se tornam mais complexos.

## 🎯 Objetivos
* Criar um ambiente de "Parkour 2D" procedural usando o **Gymnasium**.
* Implementar **Curriculum Learning** para ajustar o ambiente dinamicamente.
* Provar a **Generalização** do modelo em níveis que ele nunca viu.

## 📂 Arquivos
* `parkour_env.py`: Ambiente customizado com obstáculos procedurais baseados na `difficulty`.
* `train_curriculum.py`: Loop de treinamento escalonado em fases (ex: dificuldade 0.1 -> 0.4 -> 0.8).
* `verify_generalization.py`: Avaliação final em um nível difícil para testar o conhecimento do agente.
* `debug_render.py`: Script para visualizar a trajetória do agente em tempo real no console.

## 🚀 Como Executar
### Treinamento Completo
```bash
PYTHONPATH=. python3 level_3_curriculum/train_curriculum.py
```
### Verificação de Generalização
```bash
PYTHONPATH=. python3 level_3_curriculum/verify_generalization.py
```

### 📤 Saída Esperada (Generalização)
```text
Evaluating the model for 20 episodes on high difficulty (0.8)...
Verification finished!
Success Rate over 20 episodes: 85.00%
Average Reward: 88.45
Success! The agent demonstrated generalization in a procedural environment.
```

## 🧠 Conceitos Chave
### Curriculum Learning (Escalonamento de Dificuldade)
Em vez de jogar o agente em um nível impossível, o sistema começa com obstáculos fáceis e aumenta a complexidade. Isso evita a "falha catastrófica" (catastrophic forgetting).

### Generalização Procedural
O ambiente gera níveis diferentes a cada execução. O agente não pode "decorar" o mapa, ele precisa realmente aprender a lógica de como pular buracos e se mover para a direita.
