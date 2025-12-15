# detect spam
spam = ['make a lot of money', 'buy now', 'subscribe this', 'click this']

comment = input('enter your comment:')

if comment.lower() in spam:
    print('Spam detected!')

else:
    print('Spam not detected!')

