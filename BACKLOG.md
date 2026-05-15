# Project Backlog

## Level 1 (Pathfinding & Async)
- [ ] Add BDD testing (`pytest-bdd`) in `features/` and `tests/test_bdd.py`.

## Level 2 (Deep RL)
- [ ] Add BDD testing for training and evaluation.

## Level 3 (Curriculum Learning)
- [ ] Add BDD testing for parkour environment and generalization logic.

## Visuals
- [ ] Standardize HUD classes across environments using `#E0E0E0` for text, `#FF4B4B` for alerts, and modern fonts (Arial/Consolas). Ensure reset methods are implemented.

## Documentation
- [ ] Ensure detailed file descriptions, Mermaid diagrams, Expected Output blocks, and execution screenshots are added to all levels' READMEs.
- [ ] Create or update `generate_images.py` to generate visual assets using `matplotlib`.

## Environment/Build
- [ ] Guarantee `swig` and `gymnasium[box2d]` are correctly documented for setup in all task automations (Taskfile.yml).

## Refactoring
- [ ] Apply SOLID principles and directory structure (agents, core, visuals) established in Level 0 to Levels 1, 2, and 3.
