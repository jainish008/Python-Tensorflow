#Importing the tensorflow library 
import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4,5])
x2 = tf.constant([10,11,12,13,14])

# Multiply
result = tf.multiply(x1, x2)

# Print the result
print(result)

#the above code of result doesn't actually calculate, it has just
#define the model of it. This means tensorflow has different in evaluation

#Below is the code through we can get result of multiplication of the 
#two constants

y1 = tf.constant([6,7,8,9])
y2 = tf.constant([16,17,18,19])

#Multiply
results = tf.multiply(y1,y2)

# Intialize the Session
ses = tf.Session()

#Print the result
print(ses.run(result))


#Close the Sesssion
ses.close()