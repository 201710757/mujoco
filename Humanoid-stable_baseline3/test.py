from stable_baselines3 import A2C
from stable_baselines3 import PPO

import gym
env = gym.make('Humanoid-v2')

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=500000)
model.save("ppo_humanoid")


