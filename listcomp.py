def check_pass(password):
    return True in [ c.isupper() for c in password ] and True in [ c.islower() for c in password ] and True in [c.isdigit() for c in password ]

print check_pass('Jasjda0908hd') # t
print check_pass('Jaad')         # f
print check_pass('0908hd')       # f
print check_pass('$#@@%')        # f
print check_pass('90855')        # f

'''
Gives passwords a strength score based on the following:
- 1/3 points for an uppercase, lowercase, or numeric character
- 2/3 points for special characters
Maxes out at 10, minimum is 1 for checked passwords
'''
def pass_strength(password):
    raw = sum([ 1 for c in password if c.isupper() ]) + sum([ 1 for c in password if c.islower() ]) + sum([ 1 for c in password if c.isdigit() ]) + sum([2 for c in password if not c.isalnum() ])
    return min(10, raw / 3) # possible range of values are 1-10

print pass_strength('Jasjda0908hd(*$%&($))')
print pass_strength('Abc123')
print pass_strength('1De')
