Feature: Pathfinding and Reinforcement Learning POC
    As a developer
    I want to verify that all levels of the POC are functional
    So that I can ensure the didactic value of the project

    Scenario: Level 1 - A* Pathfinding logic (Unit Test)
        Given a grid environment with no obstacles
        When I calculate the path from (0,0) to (2,2)
        Then the path should have length 5
        And the path should start at (0,0) and end at (2,2)

    Scenario: Level 1 - Multiple Agents (Integration Test)
        Given a grid environment and two agents
        When I start both agents concurrently
        Then both agents should eventually reach their respective goals

    Scenario: Level 2 - PPO Training Initialization (Unit Test)
        Given a Lunar Lander environment
        When I initialize a PPO model
        Then the model should be ready for training
        And the action space should match the Lunar Lander discrete actions

    Scenario: Level 3 - Parkour progression (Integration Test)
        Given a Parkour environment with difficulty 0.1
        When the agent moves right 5 times
        Then the agent position should be greater than or equal to 5

    Scenario: End-to-End POC Flow (E2E)
        Given the complete POC repository
        When I execute the main pathfinding script
        And I check the model training initialization for level 2 and 3
        Then all scripts should execute without errors
