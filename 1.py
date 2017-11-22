import tensorflow as tf
import numpy
import matplotlib.pyplot as plt # 这个库是绘图高手，有空练练手
rng = numpy.random

# Parameters
learning_rate = 0.01
training_epochs = 2000 #训练的次数
display_step = 50

# Training Data
train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float") # 预定义，这里预定义字符类型
Y = tf.placeholder("float")

# Create Model

# Set model weights
W = tf.Variable(rng.randn(), name="weight") #变量，这里是随机数
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model
activation = tf.add(tf.multiply(X, W), b) # tf.multiply 两个数相加

# Minimize the squared errors
cost = tf.reduce_sum(tf.pow(activation-Y, 2))/(2*n_samples) #L2 loss tf.reduce_sum计算输入tensor元素的和
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) #Gradient descent
#GradientDescentOptimizer 实现梯度下降算法的优化器

# Initializing the variables
init = tf.initialize_all_variables() # 初始化所有变量

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        #Display logs per epoch step
        if epoch % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", \
                "{:.9f}".format(sess.run(cost, feed_dict={X: train_X, Y:train_Y})), \
                "W=", sess.run(W), "b=", sess.run(b))

    print ("Optimization Finished!")
    print ("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}), \
          "W=", sess.run(W), "b=", sess.run(b))
    writer = tf.summary.FileWriter("./xianxing",sess.graph)
    #Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data') # plt.plot(x,y)
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

writer.close()
    
