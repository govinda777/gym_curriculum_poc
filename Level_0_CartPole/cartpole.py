import gymnasium as gym
import time
import argparse
import pygame
import numpy as np

class CartPoleHUD:
    def __init__(self, screen_width=600, screen_height=400, sidebar_width=200):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sidebar_width = sidebar_width
        self.total_width = screen_width + sidebar_width

        self.high_score = 0
        self.angle_history = []
        self.max_history = 100

        # Colors
        self.COLOR_TEXT = (224, 224, 224)    # #E0E0E0
        self.COLOR_ALERT = (255, 75, 75)    # #FF4B4B
        self.COLOR_BG = (30, 30, 30)
        self.COLOR_SIDEBAR = (20, 20, 20)
        self.COLOR_GRAPH = (0, 255, 127)

        pygame.font.init()
        # Fallback to default if Arial or Consolas are not found
        try:
            self.font_main = pygame.font.SysFont("Arial", 18)
            self.font_bold = pygame.font.SysFont("Arial", 22, bold=True)
            self.font_mono = pygame.font.SysFont("Consolas", 16)
        except:
            self.font_main = pygame.font.SysFont(None, 18)
            self.font_bold = pygame.font.SysFont(None, 22)
            self.font_mono = pygame.font.SysFont(None, 16)

    def update_data(self, steps, angle, position):
        if steps > self.high_score:
            self.high_score = steps

        self.angle_history.append(angle)
        if len(self.angle_history) > self.max_history:
            self.angle_history.pop(0)

    def draw(self, env, steps, angle, position, action, start_time):
        # 1. Expand screen width if not already expanded
        screen = env.unwrapped.screen
        if screen.get_width() != self.total_width:
            # Create new display surface
            screen = pygame.display.set_mode((self.total_width, self.screen_height))
            # Sync Gymnasium's internal reference to the new surface
            env.unwrapped.screen = screen

        # 2. Draw Sidebar Background
        sidebar_rect = pygame.Rect(self.screen_width, 0, self.sidebar_width, self.screen_height)
        pygame.draw.rect(screen, self.COLOR_SIDEBAR, sidebar_rect)
        pygame.draw.line(screen, (100, 100, 100), (self.screen_width, 0), (self.screen_width, self.screen_height), 2)

        # 3. OSD (On-Screen Display)
        survival_time = time.time() - start_time
        angle_deg = np.degrees(angle)

        # Color based on stress level
        text_color = self.COLOR_ALERT if abs(angle_deg) > 10 else self.COLOR_TEXT

        # OSD: Top Left
        self._draw_text_box(screen, f"Time: {survival_time:.1f}s", (10, 10), text_color)
        self._draw_text_box(screen, f"Angle: {angle_deg:.2f}°", (10, 40), text_color)

        # OSD: Top Right
        self._draw_text_box(screen, f"High Score: {self.high_score}", (self.screen_width - 150, 10), self.COLOR_TEXT)

        # OSD: Action Indicator (Replacing emojis with arrows for compatibility)
        action_arrow = "<-" if action == 0 else "->"
        action_text = "LEFT" if action == 0 else "RIGHT"
        self._draw_text_box(screen, f"Action: {action_arrow} {action_text}", (10, 70), self.COLOR_TEXT)

        # 4. Stability HUD
        # Position Bar at the bottom
        bar_y = self.screen_height - 30
        bar_width = self.screen_width - 40
        pygame.draw.rect(screen, (50, 50, 50), (20, bar_y, bar_width, 10))
        # cart position range is roughly -2.4 to 2.4
        pos_ratio = (position + 2.4) / 4.8
        pos_ratio = max(0, min(1, pos_ratio))
        marker_x = 20 + pos_ratio * bar_width
        pygame.draw.circle(screen, self.COLOR_GRAPH, (int(marker_x), bar_y + 5), 8)

        # 5. Performance Graph (Sidebar)
        graph_rect = pygame.Rect(self.screen_width + 10, 50, self.sidebar_width - 20, 150)
        pygame.draw.rect(screen, (40, 40, 40), graph_rect)
        self._draw_text_box(screen, "Angle variation", (self.screen_width + 10, 20), self.COLOR_TEXT)

        if len(self.angle_history) > 1:
            points = []
            for i, h_angle in enumerate(self.angle_history):
                # Map angle to graph coordinates
                x = graph_rect.left + (i / (self.max_history - 1)) * graph_rect.width
                # Map angle (-24 to 24 degrees) to graph height
                # Ensure values are within range to prevent drawing outside graph
                y_deg = np.degrees(h_angle)
                y_ratio = (y_deg + 24) / 48
                y_ratio = max(0, min(1, y_ratio))
                y = graph_rect.bottom - y_ratio * graph_rect.height
                points.append((int(x), int(y)))
            pygame.draw.lines(screen, self.COLOR_GRAPH, False, points, 2)

    def _draw_text_box(self, screen, text, pos, color):
        # Draw background box for better legibility
        text_surf = self.font_mono.render(text, True, color)
        bg_rect = text_surf.get_rect(topleft=pos)
        bg_rect.inflate_ip(10, 6)

        # Transparent background box
        s = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        s.fill((0, 0, 0, 160)) # Alpha 160
        screen.blit(s, bg_rect.topleft)
        screen.blit(text_surf, pos)

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
    
    # Initialize HUD
    hud = CartPoleHUD() if render_mode == "human" else None

    episode = 0
    stable_achieved = False

    try:
        while not stable_achieved and (episodes == -1 or episode < episodes):
            observation, info = env.reset()
            episode += 1
            print(f"\n🎬 Episódio {episode} iniciado.")
            
            start_time = time.time()
            for step in range(max_steps):
                if render_mode == "human":
                    env.render()
                    # Custom drawing on env.unwrapped.screen
                    # Observation contains [cart_pos, cart_vel, pole_angle, pole_vel]
                    pos, vel, angle, angle_vel = observation
                    # Choose a temporary action just to show in HUD (actual action below)
                    # We need the action that WILL be executed
                    action = env.action_space.sample()

                    hud.update_data(step + 1, angle, pos)
                    hud.draw(env, step + 1, angle, pos, action, start_time)
                    # Use flip() but note that env.render() already does it in human mode
                    # However, since we added HUD elements, we need to flip again to show them.
                    # To avoid flicker, Gymnasium's internal flip should ideally be avoided,
                    # but since we can't easily change env.render() behavior, we flip here.
                    pygame.display.flip()
                elif render_mode == "rgb_array":
                    env.render()

                if render_mode == "human":
                    # Reuse the same action we sampled for HUD
                    pass
                else:
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
                    # Add small delay to keep it fluid
                    pygame.time.wait(10)

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
