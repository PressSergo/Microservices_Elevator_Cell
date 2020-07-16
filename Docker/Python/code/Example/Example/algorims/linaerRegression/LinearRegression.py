import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

train_X = np.array([[1,3],
 [3,8],
 [5,3],
 [9,1],
 [9,10],
 [1,0],
 [11,2],
 [2,10],
 ],float)
train_Y = np.array([1, 2, 3, 8, 9,10, 11, 9, 5, 3, 2,1, 0],float)
test_X = train_X
test_Y = train_Y

num_features = train_X.shape[1]
num_classes = train_Y.shape[1]

X = tf.placeholder("float", [None, num_features])
Y = tf.placeholder("float",[None, num_classes])

W = tf.Variable(tf.zeros([num_features,num_classes]))
B = tf.Variable(tf.zeros([num_classes]))

pY = tf.nn.softmax(tf.matmul(X, W) + B)

cost_fn = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pY, Y))

opt = tf.train.AdamOptimizer(0.01).minimize(cost_fn)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

num_epochs = 40
for i in range(num_epochs):
  sess.run(opt, feed_dict={X:train_X, Y:train_Y})