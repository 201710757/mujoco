import gym

from stable_baselines3 import A2C

env = gym.make('Humanoid-v2')

model = A2C.load("ppo_humanoid")

r = 0
cus_r = 0
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
    r += rewards
    cus_r += 1
    if dones:
        print("r : ", r)
        print("cus r : ", cus_r)
        break
