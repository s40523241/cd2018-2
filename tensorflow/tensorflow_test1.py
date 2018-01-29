import unittest
import numpy as np
import tensorflow as tf

# https://guillaumegenthial.github.io/testing.html


def get_entry_tf(t, indices_d1, indices_d2, batch_size):
    """
    Args:
        t: shape = [batch, d1, d2]
        indices_1d: shape = [batch]
        indices_2d: shape = [batch]

    Returns:
        o: shape = [batch], with o[i] = t[i, indices_1d[i], indices_2d[i]]

    """
    indices = tf.stack([tf.range(batch_size), indices_d1, indices_d2], axis=1)
    return tf.gather_nd(t, indices)


def get_entry_np(t, indices_d1, indices_d2, batch_size):
    """Naive numpy implementation"""
    result = np.zeros(batch_size)
    for i in range(batch_size):
        result[i] = t[i, indices_d1[i], indices_d2[i]]
    return result


class Test(unittest.TestCase):

    def test_get_entry(self):
        success = True
        for _ in range(10):
            # sample input
            batch_size, d1, d2 = map(int, np.random.randint(low=2, high=100, size=3))
            test_input = np.random.random([batch_size, d1, d2])
            test_indices_d1 = np.random.randint(low=0, high=d1-1, size=[batch_size])
            test_indices_d2 = np.random.randint(low=0, high=d2-1, size=[batch_size])
            # evaluate the numpy version
            test_result = get_entry_np(test_input, test_indices_d1, test_indices_d2, batch_size)
            # evaluate the tensorflow version
            with tf.Session() as sess:
                tf_input = tf.constant(test_input, dtype=tf.float32)
                tf_indices_d1 = tf.constant(test_indices_d1, dtype=tf.int32)
                tf_indices_d2 = tf.constant(test_indices_d2, dtype=tf.int32)
                tf_result = get_entry_tf(tf_input, tf_indices_d1, tf_indices_d2, batch_size)
                tf_result = sess.run(tf_result)
                # check that outputs are similar
                success = success and np.allclose(test_result, tf_result)

        self.assertEqual(success, True)


if __name__ == '__main__':
    unittest.main()
