# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

hat = prob_calculator.Hat(blue=5, red=4, green=2)
probability = prob_calculator.experiment(hat=hat,
                                         expected_balls={
                                           "green": 2,
                                           "red": 1
                                         },
                                         num_balls_drawn=4,
                                         num_experiments=3000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
