from gym.envs.registration import register

register(
    id="RexGallop-v0",
    entry_point="rex_gym.envs:RexReactiveEnv",
    max_episode_steps=2000,
)

register(
    id="RexPoses-v0",
    entry_point="rex_gym.envs:RexPosesEnv",
    max_episode_steps=2000,
)

register(
    id="RexStandup-v0",
    entry_point="rex_gym.envs:RexStandupEnv",
    max_episode_steps=2000,
)

register(
    id="RexTurn-v0",
    entry_point="rex_gym.envs:RexTurnEnv",
    max_episode_steps=2000,
)

register(
    id="RexWalk-v0",
    entry_point="rex_gym.envs:RexWalkEnv",
    max_episode_steps=2000,
)
