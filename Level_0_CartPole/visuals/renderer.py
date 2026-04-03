import pygame
import time
from visuals.theme import UITheme

class DashboardRenderer:
    """Handles visual representation of the simulation (SRP)."""
    def __init__(self, width=900, height=600):
        self.width = width
        self.height = height
        self.env_w, self.env_h = 600, 400
        
        pygame.font.init()
        try:
            self.fonts = {
                'header': pygame.font.SysFont("Segoe UI, Arial", 20, bold=True),
                'main': pygame.font.SysFont("Segoe UI, Arial", 16),
                'label': pygame.font.SysFont("Segoe UI, Arial", 12),
                'huge': pygame.font.SysFont("Consolas, Courier New", 32, bold=True)
            }
        except:
            self.fonts = {k: pygame.font.SysFont(None, s) for k, s in zip(['header', 'main', 'label', 'huge'], [20, 16, 12, 32])}

    def render(self, screen, frame, telemetry, action):
        screen.fill(UITheme.BG)
        
        # 1. Environment View
        if frame is not None:
            # gymnasium (H, W, 3) -> pygame (W, H, 3)
            surf = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            screen.blit(surf, (0, 0))
            
        # 2. Sidebar View
        self._draw_sidebar(screen, telemetry)
        
        # 3. Bottom HUD View
        self._draw_bottom_panel(screen, telemetry, action)

    def _draw_sidebar(self, screen, tel):
        x = self.env_w
        pygame.draw.rect(screen, UITheme.SIDEBAR, (x, 0, self.width - x, self.height))
        pygame.draw.line(screen, UITheme.GRID, (x, 0), (x, self.height), 1)
        
        y = 30
        self._draw_text(screen, "NEURAL DASHBOARD", (x + 30, y), UITheme.ACCENT, self.fonts['header'])
        y += 60
        
        self._draw_card(screen, "EPISODE", str(tel.episode), (x + 30, y), 110)
        self._draw_card(screen, "STEPS", str(tel.steps), (x + 150, y), 110)
        y += 80
        self._draw_card(screen, "HIGH SCORE", str(tel.high_score), (x + 30, y), 230, UITheme.SUCCESS)
        
        # Graphs
        y += 100
        angle_val = tel.angle_history[-1] if tel.angle_history else 0
        self._draw_graph(screen, "POLE ANGLE", tel.angle_history, -24, 24, (x + 30, y), UITheme.ACCENT, "°", angle_val)
        
        y += 130
        pos_val = tel.pos_history[-1] if tel.pos_history else 0
        self._draw_graph(screen, "POSITION", tel.pos_history, -2.4, 2.4, (x + 30, y), UITheme.SUCCESS, "m", pos_val)

    def _draw_bottom_panel(self, screen, tel, action):
        area = pygame.Rect(20, self.env_h + 20, self.env_w - 40, 160)
        pygame.draw.rect(screen, UITheme.SIDEBAR, area, border_radius=15)
        
        duration = time.time() - tel.start_time
        self._draw_text(screen, f"{duration:.1f}s", (area.x + 40, area.y + 40), UITheme.TEXT, self.fonts['huge'])
        self._draw_text(screen, "ELAPSED TIME", (area.x + 40, area.y + 80), UITheme.TEXT_DIM, self.fonts['label'])
        
        act_text = "LEFT" if action == 0 else "RIGHT"
        col = UITheme.ACCENT if action == 0 else UITheme.SUCCESS
        self._draw_text(screen, "DECISION", (area.right - 140, area.y + 40), UITheme.TEXT_DIM, self.fonts['label'])
        self._draw_text(screen, act_text, (area.right - 140, area.y + 60), col, self.fonts['header'])

    def _draw_text(self, screen, text, pos, color, font):
        screen.blit(font.render(text, True, color), pos)

    def _draw_card(self, screen, label, value, pos, width, color=UITheme.TEXT):
        rect = pygame.Rect(pos[0], pos[1], width, 60)
        pygame.draw.rect(screen, UITheme.CARD, rect, border_radius=8)
        self._draw_text(screen, label, (pos[0] + 12, pos[1] + 10), UITheme.TEXT_DIM, self.fonts['label'])
        self._draw_text(screen, value, (pos[0] + 12, pos[1] + 28), color, self.fonts['header'])

    def _draw_graph(self, screen, title, data, min_v, max_v, pos, color, unit, current_val):
        rect = pygame.Rect(pos[0], pos[1], 230, 80)
        self._draw_text(screen, f"{title}: {current_val:.1f}{unit}", (rect.x, rect.y - 22), UITheme.TEXT, self.fonts['main'])
        
        pygame.draw.rect(screen, (15, 15, 15), rect, border_radius=5)
        pygame.draw.rect(screen, UITheme.GRID, rect, 1, border_radius=5)
        
        zero_ratio = (0 - min_v) / (max_v - min_v)
        zero_y = rect.bottom - zero_ratio * rect.height
        pygame.draw.line(screen, UITheme.GRID, (rect.left, zero_y), (rect.right, zero_y))

        if len(data) < 2: return
        pts = []
        for i, v in enumerate(data[-100:]):
            px = rect.x + (i / 99) * rect.width
            ratio = max(0, min(1, (v - min_v) / (max_v - min_v)))
            py = rect.bottom - ratio * rect.height
            pts.append((float(px), float(py)))
        pygame.draw.lines(screen, color, False, pts, 2)
