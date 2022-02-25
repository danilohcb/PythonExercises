# Brazilian's right to vote
# Under 16 reads Denied, 16 to 18 reads Optional, 18+ reads Obligatory


def voting(y):
    """
    Returns whether or not a person is able to vote.
    :param y: Year of birth
    :return: clarified above
    """
    from datetime import date
    age = date.today().year - year
    if age < 16:
        status = 'Denied'
    elif 18 > age <= 16:
        status = 'Optional'
    else:
        status = 'Obligatory'
    print(f'At age of {age} your right to vote is: ', end='')
    return status


year = int(input('Insert your year of birth: '))
print(voting(year))
