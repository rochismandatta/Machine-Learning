import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

result =  tf.multiply(x1,x2) #computation graph which models everything     
                                #just defines the no of nodes, layers, starting
                                    #values
print(result)

##sess = tf.Session()
##print(sess.run(result))
##sess.close()

with tf.Session() as sess: #actually goes backend and runs the defined compuatation func
                            # no need to hard code the logic just set out what we
                                #want in the computation graph phase
    print(sess.run(result))
