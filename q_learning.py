# -*- coding: utf-8 -*-
"""Q-Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D3NxEl4hXf_ZSrJ1QFjAubbEhABXa-nz

**Aprendizagem Por Reforço com Q-Learning**
**Reinforcement Learning with Q-Learning**

[Fonte](https://gym.openai.com/)
"""

!pip install plotly --upgrade

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

import gym
import random

env = gym.make('Taxi-v3').env

env.render()

"""**Temos 6 ações possíveis para realizar**"""
"""**We have 6 possible actions to perform**"""

# 0 = south 1 = north 2 = east 3 = west 4 = pickup 5 = dropoff
print(env.action_space)

print(env.observation_space)

q_table = np.zeros([env.observation_space.n, env.action_space.n])
q_table.shape

# Commented out IPython magic to ensure Python compatibility.
# %%time
# from IPython.display import clear_output
# 
# alpha = 0.1
# gamma = 0.6
# epsilon = 0.1
# 
# for i in range(100000):
#   estado = env.reset()
# 
#   penalidades, recompensa = 0, 0
#   done = False
#   while not done:
#     if random.uniform(0, 1) < epsilon:
#       acao = env.action_space.sample()
#     else:
#       acao = np.argmax(q_table[estado])
# 
#     proximo_estado, recompensa, done, info = env.step(acao)
# 
#     q_antigo = q_table[estado, acao]
#     proximo_maximo = np.max(q_table[proximo_estado])
# 
#     q_novo = (1 - alpha) * q_antigo + alpha * (recompensa + gamma * proximo_maximo)
#     q_table[estado, acao] = q_novo
# 
#     if recompensa == -10:
#       penalidades += 1
#     estado = proximo_estado
# 
#   if i % 100 == 0:
#     clear_output(wait=True)
#     print('Episódio: ', i)
# 
# print('Treinamento Concluido')

"""**Avaliação**"""
"""**Assessment**"""

total_penalidades = 0
episodios = 50
frames = []

for _ in range(episodios):
  estado = env.reset()
  penalidades, recompensa = 0, 0
  done = False
  while not done:
    acao = np.argmax(q_table[estado])
    estado, recompensa, done, info = env.step(acao)

    if recompensa == -10:
      penalidades += 1

    frames.append({
        'frame': env.render(mode='ansi'),
        'state': estado,
        'action': acao,
        'reward': recompensa
    })

  total_penalidades += penalidades

print('Epísodios', episodios)
print('Penalidades', total_penalidades)

from time import sleep
for frame in frames:
  clear_output(wait=True)
  print(frame['frame'])
  print('Estado', frame['state'])
  print('Ação', frame['action'])
  print('Recompensa', frame['reward'])
  sleep(.1)
