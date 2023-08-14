import unittest
import prob_calculator

prob_calculator.random.seed(95)


class UnitTests(unittest.TestCase):

  def test_hat_class_contents(self):
    hat = prob_calculator.Hat(red=2, blue=3)
    actual = hat.contents
    expected = ["red", "red", "blue", "blue", "blue"]
    self.assertEqual(
      actual, expected,
      'Expected creation of hat object to add correct contents.')

  def test_hat_draw(self):
    hat = prob_calculator.Hat(red=4, green=2)
    actual = hat.draw(2)
    expected = ['green', 'green']
    self.assertEqual(
      actual, expected,
      'Expected hat draw to return two random items from hat contents.')
    actual = len(hat.contents)
    expected = 4
    self.assertEqual(
      actual, expected,
      'Expected hat draw to reduce number of items in contents.')

  def test_prob_experiment(self):
    hat = prob_calculator.Hat(black=6, red=4, green=3)
    probability = prob_calculator.experiment(hat=hat,
                                             expected_balls={
                                               "red": 2,
                                               "green": 1
                                             },
                                             num_balls_drawn=5,
                                             num_experiments=2000)
    actual = probability
    expected = 0.3585
    self.assertAlmostEqual(
      actual,
      expected,
      delta=0.01,
      msg='Expected experiment method to return a different probability.')
    hat = prob_calculator.Hat(red=5, orange=4, black=1, blue=0, pink=2, stripped=9)
    probability = prob_calculator.experiment(hat=hat,
                                             expected_balls={
                                               "orange": 2,
                                               "pink": 2,
                                               "stripped": 1
                                             },
                                             num_balls_drawn=5,
                                             num_experiments=500)
    actual = probability
    expected = 0.002
    self.assertAlmostEqual(
      actual,
      expected,
      delta=0.01,
      msg='Expected experiment method to return a different probability.')


if __name__ == "__main__":
  unittest.main()
