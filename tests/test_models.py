from datetime import date

from liebrary.models import Author


def test_authors_equality():
    asimov_birthday = date(1920, 1, 2)
    a1 = Author(1, 'Isaac Asimov', asimov_birthday)
    a2 = Author(1, 'Isaac Asimov', asimov_birthday)

    assert a1 == a2


def test_authors_equality():
    asimov_birthday = date(1920, 1, 2)
    a1 = Author(1, 'Isaac Asimov', asimov_birthday)
    a2 = Author(2, 'Isaac Asimov', asimov_birthday)

    assert a1 != a2


def test_author_with_mandatory_attributes():
    asimov_birthday = date(1920, 1, 2)
    asimov = Author(1, 'Isaac Asimov', asimov_birthday)

    assert asimov.id == 1
    assert asimov.name == 'Isaac Asimov'
    assert asimov.birth_date == asimov_birthday
