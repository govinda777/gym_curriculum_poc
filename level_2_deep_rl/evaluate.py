import gymnasium as gym
from stable_baselines3 import PPO
import numpy as np

def evaluate_lunar_lander(model_path="level_2_deep_rl/models/ppo_lunar_lander", n_episodes=20):
    """
    Evaluate the trained PPO agent on the LunarLander-v3 environment.
    Check if the agent achieved a positive average score.
    """
    # Create the environment
    env = gym.make("LunarLander-v3")

    # Load the trained model
    try:
        model = PPO.load(model_path)
    except FileNotFoundError:
        print(f"Error: Model not found at {model_path}. Please train the model first.")
        return

    print(f"Evaluating the model for {n_episodes} episodes...")

    all_rewards = []

    for episode in range(n_episodes):
        obs, info = env.reset()
        episode_reward = 0
        done = False

        while not done:
            # Predict the action based on the observation
            action, _states = model.predict(obs, deterministic=True)

            # Step in the environment
            obs, reward, terminated, truncated, info = env.step(action)
            episode_reward += reward
            done = terminated or truncated

        all_rewards.append(episode_reward)
        # print(f"Episode {episode + 1}: Reward = {episode_reward:.2f}")

    average_reward = np.mean(all_rewards)
    print(f"\nEvaluation finished!")
    print(f"Average Reward over {n_episodes} episodes: {average_reward:.2f}")

    # KPI Check: Average score should be positive
    if average_reward > 0:
        print("Success! The agent has achieved a positive average score.")
    else:
        print("Failure. The agent achieved a negative average score. It may need more training.")

    env.close()
    return average_reward

if __name__ == "__main__":
    evaluate_lunar_lander()
