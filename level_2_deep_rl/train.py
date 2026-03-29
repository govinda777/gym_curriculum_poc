import gymnasium as gym
from stable_baselines3 import PPO
import os

# Create model directory
os.makedirs("level_2_deep_rl/models", exist_ok=True)

def train_lunar_lander(total_timesteps=100000):
    """
    Train a PPO agent on the LunarLander-v3 environment.
    The agent must learn to land safely, premiating stability and penalizing erratic behavior.
    """
    # Create the environment
    env = gym.make("LunarLander-v3")

    # Initialize the agent
    # PPO is used here as suggested in the POC strategy
    model = PPO("MlpPolicy", env, verbose=1)

    print(f"Starting training for {total_timesteps} timesteps...")
    model.learn(total_timesteps=total_timesteps)

    # Save the model
    model_path = "level_2_deep_rl/models/ppo_lunar_lander"
    model.save(model_path)
    print(f"Model saved at {model_path}")

    env.close()

if __name__ == "__main__":
    train_lunar_lander()
