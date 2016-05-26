from unittest import mock
from datetime import date

from liebrary.models import Author
from liebrary.usecases import author as auth


def test_retrieve_an_empty_usecase_list():
    repo = mock.Mock()
    repo.list.return_value = []

    uc = auth.AuthorListUseCase(repo)
    response = uc.execute()

    repo.list.assert_called_with()
    assert response == []


def test_list_authors():
    repo = mock.Mock()
    repo.list.return_value = [
        Author('Isaac Asimov', date(1920, 1, 2)),
        Author('J.K. Rowling', date(1965, 7, 31))
    ]

    uc = auth.AuthorListUseCase(repo)
    response = uc.execute()

    assert len(response) == 2
