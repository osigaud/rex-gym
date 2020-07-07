ENV_ID_TO_POLICY = {
    'gallop': ('rex_gym/policies/galloping/balanced', 'model.ckpt-3000000'),
    'walk': ('rex_gym/policies/walking/alternating_legs', 'model.ckpt-10000000'),
    'standup': ('rex_gym/policies/standup', 'model.ckpt-10000000'),
    'turn': ('rex_gym/policies/turn', 'model.ckpt-2000000'),
    'jump': ('rex_gym/policies/jump', 'model.ckpt-14000000')
}

ENV_ID_TO_ENV_NAMES = {
    'gallop': 'RexReactiveEnv',
    'walk': 'RexWalkEnv',
    'turn': 'RexTurnEnv',
    'standup': 'RexStandupEnv',
    'go': 'RexGoEnv',
    'poses': 'RexPosesEnv',
    'jump': 'RexJumpEnv'
}
