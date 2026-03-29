# Nível 2: Introdução ao Deep RL (Lunar Lander)

Neste nível, passamos de regras manuais para o **aprendizado por experiência**. O agente deve aprender a pousar uma nave em um ambiente de física simulada.

## 🎯 Objetivos
* Utilizar a biblioteca **Stable Baselines3** para treinar um agente.
* Implementar o algoritmo **PPO (Proximal Policy Optimization)**.
* Definir uma **Reward Function** que premie a estabilidade e penalize o combustível gasto.

## 📂 Arquivos
* `train.py`: Script de treinamento do agente usando o ambiente `LunarLander-v3`.
* `evaluate.py`: Avaliação do desempenho médio do modelo treinado.
* `models/`: Diretório onde o modelo treinado (`ppo_lunar_lander.zip`) é armazenado.

## 🚀 Como Executar
### Treinamento
```bash
PYTHONPATH=. python3 level_2_deep_rl/train.py
```
### Avaliação
```bash
PYTHONPATH=. python3 level_2_deep_rl/evaluate.py
```

### 📤 Saída Esperada (Avaliação)
```text
Evaluating the model for 20 episodes...
Average Reward over 20 episodes: 245.12
Success! The agent has achieved a positive average score.
```

## 🧠 Conceitos Chave
### Aprendizado por Reforço (RL)
O agente interage com o ambiente, recebe uma observação (posição, velocidade) e toma uma ação (motor ligado/desligado). Ele aprende a maximizar a recompensa acumulada.

### Lunar Lander
Um ambiente clássico do Gymnasium onde o objetivo é pousar suavemente entre dois sinalizadores sem bater ou gastar combustível excessivo.
