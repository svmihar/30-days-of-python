import gym, time
import random
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam, SGD

env = gym.make('CartPole-v1')
env.reset()
goal_steps = 500
score_ = 100
game_init = 10000


def main(): 
    training_data = model_prep()
    trained_model = train(training_data)

    scores = []
    choices = []

    for e in range(game_init): 
        score = 0
        prev_obs = []

        for step in range(goal_steps): 
            # env.render()
            if len(prev_obs) == 0: 
                action = random.randrange(0,2)
            else: 
                action = np.argmax(trained_model.predict(prev_obs.reshape(-1, len(prev_obs)))[0])
            choices.append(action)
            new_obs, reward, done, info = env.step(action)
            prev_obs = new_obs
            score +=reward
            if done: 
                break

        env.reset()
        scores.append(score)

    print(f"""
    {scores}
    Average Score: {sum(scores)/len(scores)}
    choice1: {choices.count(1)/len(choices)}
    choice2: {choices.count(0)/len(choices)}
    """)


def model_prep():
    training_data = []
    accepted_scores = []
    for game_index in range(game_init):
        score = 0
        game_memory = [] 
        previous_observation = []
        for step_index in range(goal_steps): 
            action = random.randrange(0,2)
            observation, reward, done, info = env.step(action)

            if len(previous_observation) > 0: 
                game_memory.append([previous_observation, action])
            
            previous_observation = observation
            score+=reward

            if done: 
                break

        if score >= score_: 
            accepted_scores.append(score)
            for data in game_memory: 
                if data[1] == 1: 
                    output = [0,1]
                elif data[1] == 0: 
                    output = [1,0]

                training_data.append([data[0],output])
        env.reset()

    print(accepted_scores)
    return training_data

def build_model(i,o):
    model = Sequential()
    model.add(Dense(128, input_dim = i, activation='relu'))
    model.add(Dense(52, activation='relu'))
    model.add(Dense(o, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())
    return model

def train(trainin_data):
    X = np.array([i[0] for i in trainin_data]).reshape(-1, len(trainin_data[0][0]))
    y = np.array([i[1] for i in trainin_data]).reshape(-1, len(trainin_data[0][1]))

    model = build_model(i=len(X[0]), o=len(y[0]))

    model.fit(X,y,epochs=29)
    return model


if __name__ == "__main__":
    main()

# for step_index in range(1000): 
#     env.render()
#     action =env.action_space.sample()
#     observation, reward, done, info = env.step(action)
#     print(f"""
#     Step: {step_index}
#     action: {action}
#     observation: {observation}
#     reward: {reward}
#     done: {done}
#     info: {info}
#     """)
#     time.sleep(.1)
#     if done:
#         break


