import gymnasium as gym
import pygame
import os
from cartpole import CartPoleHUD
import time
import numpy as np

def capture_ui():
    render_mode = "human"
    env = gym.make("CartPole-v1", render_mode=render_mode)
    hud = CartPoleHUD()

    observation, info = env.reset()
    start_time = time.time()

    # Run for a few steps to get some data
    for step in range(30):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        pos, vel, angle, angle_vel = observation

        env.render()
        hud.update_data(step + 1, angle, pos)
        hud.draw(env, step + 1, angle, pos, action, start_time)
        pygame.display.flip()

        if terminated or truncated:
            observation, info = env.reset()

    # Save the current screen
    screen = env.unwrapped.screen
    pygame.image.save(screen, "cartpole_ui_v2.png")
    print("Screenshot saved to cartpole_ui_v2.png")
    env.close()

if __name__ == "__main__":
    # Set SDL to use dummy video driver for headless if needed,
    # but xvfb-run handles the display.
    capture_ui()
