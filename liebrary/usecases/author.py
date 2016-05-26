class AuthorListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, filter_params=None):
        return self.repo.list(filter_params)
