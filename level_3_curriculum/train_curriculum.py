import gymnasium as gym
from stable_baselines3 import PPO
from level_3_curriculum.parkour_env import ParkourEnv
import os

# Create model directory
os.makedirs("level_3_curriculum/models", exist_ok=True)

def train_curriculum():
    """
    Train a PPO agent on the ParkourEnv environment using Curriculum Learning.
    Increase difficulty over time as the agent improves.
    """
    difficulty_levels = [0.1, 0.2, 0.4, 0.6, 0.8]
    model = None

    # Increase training time per level
    timesteps_per_level = 50000

    for i, diff in enumerate(difficulty_levels):
        print(f"\n--- Training Phase {i+1} with Difficulty: {diff} ---")

        env = ParkourEnv(difficulty=diff)

        if model is None:
            model = PPO("MlpPolicy", env, verbose=0, learning_rate=0.001)
        else:
            model.set_env(env)

        model.learn(total_timesteps=timesteps_per_level)
        model.save(f"level_3_curriculum/models/ppo_parkour_diff_{diff}")

    model.save("level_3_curriculum/models/ppo_parkour_final")
    print("\nCurriculum Training Complete!")

if __name__ == "__main__":
    train_curriculum()
