from stable_baselines3 import A2C
from stable_baselines3 import PPO
from stable_baselines3 import SAC

import gym
env = gym.make('Humanoid-v2', render_mode="human")
model = SAC("MlpPolicy", env, verbose=1)

MAX_EP = 1000000

for i in range(MAX_EP):
    if i % 10 == 0:
        print("Ep {}. start".format(i))
    model.learn(total_timesteps=10000, log_interval=4)

    if i % 100 == 0:
        print("Eval Start EP.{}".format(i))
        obs, info = env.reset()
        while True:
            action, _state = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            # vec_env.render("human")
            if terminated or truncated:
                break




"""
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000, log_interval=4)
model.save("ppo_humanoid_1000")

del model

model = PPO.load("ppo_humanoid_1000")

while True:
    print("Ep start")
    obs, info = env.reset()
    while True:
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        # vec_env.render("human")
        if terminated or truncated:
            break


"""
