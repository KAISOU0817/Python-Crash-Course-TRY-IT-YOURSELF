foods = ('pizza', 'falafel', 'cake','fruits','fries')
for i in foods:
    print(i)

# foods[0] = 'orange'
# (base) yuhuaizong@YUs-MacBook-Air python % /usr/local/bin/python3 "/Users/yuhuaizong/Desktop/python/Chapter 4/4-13 Buffet 231109.py"
# pizza
# falafel
# cake
# fruits
# fries
# Traceback (most recent call last):
#   File "/Users/yuhuaizong/Desktop/python/Chapter 4/4-13 Buffet 231109.py", line 5, in <module>
#     foods[0] = 'orange'
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# (base) yuhuaizong@YUs-MacBook-Air python % 

foods = ('ramen', 'bbq', 'cake','fruits','fries')
for i in foods:
    print(i)