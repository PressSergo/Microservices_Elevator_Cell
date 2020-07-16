import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import math


#Настройки среды
from Example.algorims.reinforcementLearning.elevatorWorld.ElevatorWorld import Elevator
env = Elevator()


n_inputs = 4
n_hidden = 4

n_outputs = 1
initializer = tf.contrib.layers.variance_scaling_initializer()

X = tf.placeholder(tf.float32,shape=[None,n_inputs])
hidden = tf.layers.dense(X,n_hidden,activation=tf.nn.elu,kernel_initializer=initializer)
logistic = tf.layers.dense(hidden,n_outputs,kernel_initializer=initializer)
outputs = tf.nn.sigmoid(logistic)

p_up_down = tf.concat(axis = 1,values=[outputs,1-outputs])
action = tf.multinomial(tf.log(p_up_down),num_samples=1)
init = tf.global_variables_initializer()

y = 1. -tf.to_float(action)

learning_rate = 0.01
cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(labels=y,logits = logistic)
optimizer = tf.train.AdamOptimizer(learning_rate)
grads_and_vars = optimizer.compute_gradients(cross_entropy)
gradient_placeholders = []
grads_and_vars_feed = []
gradients = [grad for grad,variable in grads_and_vars]

for grad, variable in grads_and_vars:
    gradient_placeholder = tf.placeholder(tf.float32,shape=grad.get_shape())
    gradient_placeholders.append(gradient_placeholder)
    grads_and_vars_feed.append((gradient_placeholder,variable))

trainning_op = optimizer.apply_gradients(grads_and_vars_feed)
init = tf.global_variables_initializer()
saver = tf.train.Saver()

def discount_rewards(rewards, discount_rate):
    discounted_rewards = np.empty(len(rewards))
    cumulative_revards = 0
    for step in reversed(range(len(rewards))):
        cumulative_revards = rewards[step] + cumulative_revards*discount_rate
        discounted_rewards[step] = cumulative_revards
    return discounted_rewards

def discount_and_normalize_rewards(all_rewards,discount_rate):
    all_discount_rewards = [discount_rewards(rewards,discount_rate) for rewards in all_rewards]
    flat_rewards = np.concatenate(all_discount_rewards)
    rewards_mean = flat_rewards.mean()
    rewards_std = flat_rewards.std()
    return [(discounted_rewards - rewards_mean)/rewards_std
            for discounted_rewards in all_discount_rewards]

n_iterations = 200
n_max_steps = 30
n_games_per_update=20
save_iterations = 10
discount_rate = 0.95

with tf.Session() as sess:
    init.run()
    for iteration in range(n_iterations):
        all_rewards = []
        all_gradients = []

        for game in range(n_games_per_update):
            current_rewards = []
            current_gradients=[]

            obs = np.array([0,0,0,0])

            print("new_game !!!")
            for step in range(n_max_steps):
                action_val, gradients_val = sess.run(
                    [action,gradients],
                    feed_dict={X:obs.reshape(1,n_inputs)}
                )

                #добавить взаимодействие со средой
                obs, reward = env.action(action_val[0][0])
                current_rewards.append(reward)
                current_gradients.append(gradients_val)
                all_rewards.append(current_rewards)
                all_gradients.append(current_gradients)

            env.reset()
            all_rewards = discount_and_normalize_rewards(all_rewards,discount_rate)
            feed_dict = {}

            for var_index, grad_placeholder in enumerate(gradient_placeholders):
                mean_gradient = np.mean(
                    [reward * all_gradients[game_index][step][var_index]
                     for game_index, rewards in enumerate(all_rewards)
                     for step, reward in enumerate(rewards)],axis=0
                )
                feed_dict[grad_placeholder] = mean_gradient
            sess.run(trainning_op,feed_dict=feed_dict)
            if iteration % save_iterations == 0:
                saver.save(sess,"./ElevatorWorld.ckpt")