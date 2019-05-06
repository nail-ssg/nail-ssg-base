from nail_ssg_base.check_rules import check_rule

#  [+] Определение к какому правилу относится файл

def test_filemask():
    assert check_rule('filemask=*', 'a')
    assert check_rule('filemask=*', 'a.a')
    assert check_rule('filemask=*.*', 'a.a')
    assert check_rule('filemask=?.?', 'a.a')
    assert check_rule('filemask=x*.*', 'x.a')
    assert check_rule('filemask=*.*x', 'a.x')
    assert not check_rule('filemask=?.??', 'a.a')
    assert not check_rule('filemask=', 'a')
    assert not check_rule('filemask=x*', 'a')
    assert not check_rule('filemask=a*.x', 'a')
    assert not check_rule('filemask=a*.x', 'a')


def test_regexp():
    assert check_rule('regexp=.*', 'a')
    assert not check_rule('regexp=.*b', 'a')
