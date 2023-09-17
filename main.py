def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'После веселья в баре утка-маляр 🦆 вышла на улицу. '
        'Увидела как с крыши дома 🏠 падает банка краски, '
        'которую она забыла убрать. '
        'Вспомнив о зонтике ☂, она резко его открыла и спасла '
        'свой новый костюм от старых пятен. '
    )


def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 после веселья в баре вышла на улицу. '
        'Увидела как с крыши дома 🏠 падает банка краски, '
        'которую она забыла убрать. '
        'Банка краски упала ей на голову и '
        'избавила новый костюм от старых пятен. '
    )


if __name__ == '__main__':
    step1()
