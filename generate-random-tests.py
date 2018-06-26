import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num_tests', type=int, help='Number of tests')
parser.add_argument('input_size', type=int, help='Number of bits in an input')
parser.add_argument('input_number', type=int, nargs='?', help='Number of inputs per test', default=0)
args = parser.parse_args()

num_tests = args.num_tests
input_size = args.input_size
input_number = args.input_number

is_random_input_number = False
if input_number == 0:
    is_random_input_number = True

random.seed(0)
 
for x in range(1, num_tests+1):

  if is_random_input_number:
    input_number = random.randint(4, 50)

  newnums = [str(random.randint(0, 1)) for n in range(0, input_size*input_number)]
  print(str(x) + ' ' + ''.join(newnums))
