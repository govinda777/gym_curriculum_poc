import gymnasium as gym
import time
import argparse

def run_cartpole(episodes=1, max_steps=1000, render_mode="human", target_seconds=None):
    # Cria o ambiente com renderização visual
    try:
        env = gym.make("CartPole-v1", render_mode=render_mode)
    except Exception as e:
        print(f"❌ Erro ao criar o ambiente: {e}")
        print("💡 Certifique-se de ter instalado: pip install gymnasium[classic-control] pygame")
        return

    print(f"🚀 Iniciando simulação do CartPole...")
    if target_seconds:
        print(f"🎯 Meta: Ficar estável por {target_seconds} segundos (aprox. {int(target_seconds * 50)} passos).")
    
    episode = 0
    stable_achieved = False

    try:
        while not stable_achieved and (episodes == -1 or episode < episodes):
            observation, info = env.reset()
            episode += 1
            print(f"\n🎬 Episódio {episode} iniciado.")
            
            for step in range(max_steps):
                if render_mode:
                    env.render()

                # Escolhe uma ação aleatória
                action = env.action_space.sample()
                action_text = "ESQUERDA (0)" if action == 0 else "DIREITA (1)"
                
                # Exibe a jogada atual (sobrescrevendo a linha para não poluir o console)
                print(f"\r🤖 Jogada: {action_text} | Passo: {step + 1}", end="")

                # Executa a ação
                observation, reward, terminated, truncated, info = env.step(action)

                if terminated or truncated:
                    print(f"\n🏁 Episódio {episode} finalizado após {step + 1} passos.")
                    
                    # Verifica se atingiu a meta de estabilidade (50 passos = 1 segundo no CartPole-v1)
                    if target_seconds and step + 1 >= target_seconds * 50:
                        print(f"✅ META ATINGIDA! O agente ficou estável por {target_seconds}s!")
                        stable_achieved = True
                    break
                
                if render_mode == "human":
                    time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n🛑 Simulação interrompida pelo usuário.")
    finally:
        env.close()
        print("🔌 Ambiente fechado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executa uma simulação simples do CartPole.")
    parser.add_argument("--episodes", type=int, default=1, help="Número de episódios para rodar (-1 para infinito).")
    parser.add_argument("--steps", type=int, default=1000, help="Número máximo de passos por episódio.")
    parser.add_argument("--render", type=str, default="human", choices=["human", "rgb_array", "None"], 
                        help="Modo de renderização (human, rgb_array ou None).")
    parser.add_argument("--stable", type=float, default=None, help="Executar até atingir X segundos de estabilidade.")
    
    args = parser.parse_args()
    
    render_mode = None if args.render == "None" else args.render
    
    run_cartpole(episodes=args.episodes, max_steps=args.steps, render_mode=render_mode, target_seconds=args.stable)
