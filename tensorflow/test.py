#encoding=utf-8
import tensorflow as tf
import numpy as np
# ==========================
# build graph
# ==========================
# input
x = tf.placeholder(tf.float32, name = 'x')
y = tf.placeholder(tf.float32, name = 'y')

# parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

#output
linear_model = W * x + b

# loss
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

# SGD
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# 将loss加入summary。除了scalar， 还可以有其它类型
tf.summary.scalar('squred_loss', loss)        

# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
sess = tf.Session()

# 创建FilterWriter， 它负责将传入的数据写入event 文件。
merged = tf.summary.merge_all()
train_writer = tf.summary.FileWriter('/tmp/tf_test', sess.graph)
tf.global_variables_initializer().run(session = sess)

for i in range(10000):
    summary, _, curr_W, curr_b, curr_loss  = sess.run([merged, train, W, b, loss], {x:x_train, y:y_train})
    if i %200 == 0:
        print("Iteration %d, W: %s, b: %s, loss: %s"%(i, curr_W, curr_b, curr_loss))
    train_writer.add_summary(summary, i)
