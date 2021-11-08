import gym

from stable_baselines3 import DQN

env = gym.make("CartPole-v1")

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000000, log_interval=4)
model.save("dqn_cartpole_v1")

del model # remove to demonstrate saving and loading

model = DQN.load("dqn_cartpole_v1")

obs = env.reset()
for _ in range(10):
    r = 0
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        r += 1
        #env.render()
        if done:
            print("REWARD : ", r)
            obs = env.reset()
            break
