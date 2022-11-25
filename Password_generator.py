# password generator

import random

lower_case = 'qwertyuioplkmjnhbgvfcdxsza'
upper_case = 'ZXCVBNMLKJHGFDSAQWERTYUIOP'
number = '0293847561'
symbols = '!@#$%^&*?\|><'

use_for = lower_case + symbols + number + upper_case
lenth_for_pass = 10

password =''.join(random.sample(use_for, lenth_for_pass))

print('Your Generated password is: ', password)
