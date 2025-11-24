import src._1_domain.user as m_user 

def test_create_user_correctly():
    create_user_error_code, user = m_user.create("alias", "name", "lastname")

    assert create_user_error_code == 0

def test_error_wrong_type():
    create_user_error_code, user = m_user.create(89, True, "lastname")

    assert create_user_error_code == 1

def test_error_size_bound():
    create_user_error_code, user = m_user.create("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                               "name", "lastname")
    assert create_user_error_code == 2