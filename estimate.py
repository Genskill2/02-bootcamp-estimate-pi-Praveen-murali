import math
import unittest
import random

def monte_carlo(n):
  A_circle = 0
  A_square = 0
  for i in range(n):
    x = random.random()
    y = random.random()
    dist_origin = math.sqrt((x * x) + (y * y))
    if(dist_origin <= 1.):
      A_circle = A_circle + 1
      A_square = A_square + 1
    else:
      A_square = A_square + 1
  return(4 * (A_circle / A_square))

def wallis(n):
  res = 2.
  for i in range(1, n):
    first = ((2. * i) / (2. * i - 1.))
    second = ((2. *i) / (2. * i + 1.))
    res = res * first * second
  return res    

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
