import gymnasium as gym
from stable_baselines3 import PPO
from level_3_curriculum.parkour_env import ParkourEnv

def test_single_episode(model_path="level_3_curriculum/models/ppo_parkour_final"):
    env = ParkourEnv(difficulty=0.8)
    model = PPO.load(model_path)
    obs, info = env.reset()
    done = False
    print("Initial state:")
    env.render()

    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        env.render()
        print(f"Action: {action}, Reward: {reward}")

if __name__ == "__main__":
    test_single_episode()
