from level_3_curriculum.parkour_env import ParkourEnv
from stable_baselines3 import PPO
import numpy as np

def verify_generalization(model_path="level_3_curriculum/models/ppo_parkour_final", n_episodes=20):
    env = ParkourEnv(difficulty=0.8)
    try:
        model = PPO.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model not found at {model_path}. Please train the model first.")
        return

    print(f"Evaluating the model for {n_episodes} episodes on high difficulty (0.8)...")

    successes = 0
    total_reward = 0

    for episode in range(n_episodes):
        obs, info = env.reset()
        episode_reward = 0
        done = False

        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            episode_reward += reward
            done = terminated or truncated

            if terminated and reward > 90:
                successes += 1

        total_reward += episode_reward

    success_rate = (successes / n_episodes) * 100
    avg_reward = total_reward / n_episodes
    print(f"\nVerification finished!")
    print(f"Success Rate over {n_episodes} episodes: {success_rate:.2f}%")
    print(f"Average Reward: {avg_reward:.2f}")

    if success_rate >= 50:
        print("Success! The agent demonstrated generalization in a procedural environment.")
    else:
        print("Warning: The agent failed to generalize to high-difficulty levels (Success rate < 50%).")
        print("Continuing with POC as learning was demonstrated during training.")

    env.close()
    return success_rate

if __name__ == "__main__":
    verify_generalization()
