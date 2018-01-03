import enum

#class BugStatus(enum.Enum):
#
#    new = 7
#    incomplete = 6
#    invalid = 5
#    wont_fix = 4
#    in_progress = 3
#    fix_committed = 2
#    fix_released = 1

# print('\nMember name: {}'.format(BugStatus.wont_fix.name))
# print('Member value: {}'.format(BugStatus.wont_fix.value))
#
# for status in BugStatus:
#     print('{:15} = {}'.format(status.name, status.value))

# actual_state = BugStatus.wont_fix
# desired_state = BugStatus.fix_released
#
# print('Equality:',
#       actual_state == desired_state,
#       actual_state == BugStatus.wont_fix)
#
# print('Identity:',
#       actual_state is desired_state,
#       actual_state is BugStatus.wont_fix)

class BugStatus(enum.IntEnum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('Ordered by value:')
try:
    print('\n'.join(' ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print(' Cannot sort: {}'.format(err))
