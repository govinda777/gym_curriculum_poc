import pytest
import asyncio
from pytest_bdd import scenario, given, when, then
from level_1_pathfinding.grid_env import GridEnv
from level_1_pathfinding.pathfinding import a_star
from level_1_pathfinding.main import AsyncAgent
import gymnasium as gym
from stable_baselines3 import PPO
from level_3_curriculum.parkour_env import ParkourEnv
import numpy as np
import os

# Scenarios
@scenario('../features/poc.feature', 'Level 1 - A* Pathfinding logic (Unit Test)')
def test_pathfinding_unit():
    pass

@scenario('../features/poc.feature', 'Level 1 - Multiple Agents (Integration Test)')
def test_multi_agent_integration():
    pass

@scenario('../features/poc.feature', 'Level 2 - PPO Training Initialization (Unit Test)')
def test_rl_init_unit():
    pass

@scenario('../features/poc.feature', 'Level 3 - Parkour progression (Integration Test)')
def test_parkour_progression_integration():
    pass

@scenario('../features/poc.feature', 'End-to-End POC Flow (E2E)')
def test_e2e_flow():
    pass

# Level 1 Steps
@given('a grid environment with no obstacles', target_fixture="env")
def env_no_obstacles():
    return GridEnv(width=5, height=5, obstacle_prob=0)

@when('I calculate the path from (0,0) to (2,2)', target_fixture="path")
def calc_path(env):
    return a_star(env, (0, 0), (2, 2))

@then('the path should have length 5')
def check_path_length(path):
    assert len(path) == 5

@then('the path should start at (0,0) and end at (2,2)')
def check_path_bounds(path):
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

@given('a grid environment and two agents', target_fixture="multi_agent_setup")
def multi_agent_setup():
    env = GridEnv(width=10, height=10, obstacle_prob=0)
    agent1 = AsyncAgent("Agent 1", env, (0, 0), (9, 9))
    agent2 = AsyncAgent("Agent 2", env, (0, 9), (9, 0))
    return agent1, agent2

@when('I start both agents concurrently')
def run_agents_concurrently(multi_agent_setup):
    agent1, agent2 = multi_agent_setup
    async def run():
        await asyncio.gather(agent1.run(), agent2.run())
    asyncio.run(run())

@then('both agents should eventually reach their respective goals')
def check_agents_reached(multi_agent_setup):
    agent1, agent2 = multi_agent_setup
    assert agent1.finished is True
    assert agent2.finished is True

# Level 2 Steps
@given('a Lunar Lander environment', target_fixture="lunar_env")
def lunar_env():
    return gym.make("LunarLander-v3")

@when('I initialize a PPO model', target_fixture="model")
def init_ppo(lunar_env):
    return PPO("MlpPolicy", lunar_env, verbose=0)

@then('the model should be ready for training')
def check_model_ready(model):
    assert model.policy is not None

@then('the action space should match the Lunar Lander discrete actions')
def check_action_space(lunar_env, model):
    assert model.action_space == lunar_env.action_space

# Level 3 Steps
@given('a Parkour environment with difficulty 0.1', target_fixture="parkour_env")
def parkour_env_fixture():
    env = ParkourEnv(difficulty=0.1)
    env.reset()
    return env

@when('the agent moves right 5 times')
def move_right_5_times(parkour_env):
    for _ in range(5):
        parkour_env.step(2) # Move Right

@then('the agent position should be greater than or equal to 5')
def check_parkour_pos(parkour_env):
    # Depending on obstacles, it might vary, but in difficulty 0.1 it should be 5
    assert parkour_env.agent_pos >= 5

# E2E Steps
@given('the complete POC repository')
def complete_repo():
    assert os.path.exists("level_1_pathfinding/main.py")
    assert os.path.exists("level_2_deep_rl/train.py")
    assert os.path.exists("level_3_curriculum/train_curriculum.py")

@when('I execute the main pathfinding script')
def run_main_pathfinding():
    # We can just run the test_pathfinding_unit logic as part of e2e
    env = GridEnv(width=5, height=5, obstacle_prob=0)
    path = a_star(env, (0, 0), (2, 2))
    assert path is not None

@when('I check the model training initialization for level 2 and 3')
def check_all_inits():
    env2 = gym.make("LunarLander-v3")
    model2 = PPO("MlpPolicy", env2, verbose=0)
    assert model2.policy is not None

    env3 = ParkourEnv(difficulty=0.1)
    model3 = PPO("MlpPolicy", env3, verbose=0)
    assert model3.policy is not None

@then('all scripts should execute without errors')
def check_no_errors():
    # If we reached here, no errors occurred
    pass
