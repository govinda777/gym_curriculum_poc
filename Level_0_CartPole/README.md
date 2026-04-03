# 🕹️ Level 0: CartPole Experiment (Gymnasium)

Bem-vindo ao primeiro passo da sua jornada em **Reinforcement Learning**. Este repositório contém a implementação base para o ambiente **CartPole-v1**, utilizando a biblioteca modernizada `gymnasium`.

---

## 🎯 Objetivo
O objetivo deste nível é configurar o ambiente de desenvolvimento e executar uma simulação básica do CartPole, onde um agente toma ações aleatórias para tentar equilibrar um mastro sobre um carrinho.

## 📦 Pré-requisitos

### 🐍 Python
- **Recomendado:** Python 3.10 ou 3.11.
- **Aviso:** Evite Python 3.12+ (incompatibilidades conhecidas com `pygame`).

### 🛠️ Bibliotecas
- `gymnasium[classic-control]`
- `pygame` (para renderização gráfica)
- `numpy`

---

## 🚀 Instalação e Configuração

Siga os passos abaixo no seu terminal para preparar o ambiente:

1. **Criar Ambiente Virtual (Recomendado)**
   ```powershell
   python -m venv venv
   ```

2. **Ativar o Ambiente**
   - **Windows:** `.\venv\Scripts\activate`
   - **Linux/macOS:** `source venv/bin/activate`

3. **Instalar Dependências**
   ```powershell
   pip install gymnasium[classic-control] pygame
   ```

---

## ▶️ Como Executar

Para iniciar a simulação, execute o script principal:

```powershell
python cartpole.py
```

---

## 🛠️ Automação (Taskfile)

Se você tiver o [Task](https://taskfile.dev/) instalado, pode usar comandos curtos para gerenciar o projeto:

- **`task setup`**: Cria o ambiente virtual e instala dependências.
- **`task run`**: Executa a simulação padrão.
- **`task run:stable`**: Executa o agente (aleatório) até que ele consiga ficar estável por 5 segundos.
- **`task run:many`**: Executa episódios continuamente até ser interrompido.
- **`task clean`**: Remove o ambiente virtual e arquivos temporários.

---

### 🎮 Controle do Ambiente
O CartPole possui um **Espaço de Ação Discreto**:
- `0`: Empurrar o carrinho para a **esquerda**.
- `1`: Empurrar o carrinho para a **direita**.

> [!NOTE]
> Por padrão, este script executa ações aleatórias. O comportamento parecerá caótico até que um agente de IA real seja implementado.

---

## 📁 Estrutura do Projeto
```text
Level_0_CartPole/
├── venv/           # Ambiente virtual (será criado por você)
├── cartpole.py     # Script principal de execução
└── README.md       # Documentação do projeto
```

---

## 🛠️ Solução de Problemas

| Erro | Causa Provável | Solução |
| :--- | :--- | :--- |
| `ModuleNotFoundError: gymnasium` | Biblioteca não instalada. | `pip install gymnasium` |
| `No module named pygame` | Falta o motor de renderização. | `pip install pygame` |
| Falha no build do `pygame` | Versão do Python incompatível. | Use Python 3.11. |
| Importações amarelas no VS Code | Interpretador incorreto selecionado. | `Ctrl+Shift+P` -> Python: Select Interpreter. |

---

## 🧠 Próximos Passos
Agora que o ambiente está funcional, você pode avançar para:
- Implementar **Q-Learning**.
- Explorar algoritmos de **Deep RL** (DQN, PPO).
- Criar seu próprio currículo de treinamento.

---
*Desenvolvido como parte do POC de Currículo Gym.*