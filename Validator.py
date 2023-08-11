import os


class Validator:
    def __init__(self, path: str) -> None:
        cwd = os.path.abspath(os.path.dirname(__file__))
        self.path = os.path.abspath(os.path.join(cwd, path))
        self.path_year = ''
        self.path_month = ''
        self.path_day = ''

    def valid_path(self) -> bool:
        if os.path.exists(self.path) is True:
            return True
        else:
            return False

    def tree_of_dir_year(self) -> list:
        if os.path.exists(self.path) is True:
            return os.listdir(self.path)

    def tree_of_dir_month(self, year: str) -> list:
        if os.path.exists(os.path.join(self.path, year)) is True:
            self.path_year = os.path.join(self.path, year)
            return os.listdir(os.path.join(self.path, year))

    def tree_of_dir_day(self, year: str, month: str) -> list:
        if os.path.exists(os.path.join(self.path, os.path.join(year, month))) is True:
            self.path_month = os.path.join(os.path.join(self.path, os.path.join(year, month)))
            return os.listdir(os.path.join(self.path, os.path.join(year, month)))

    def tree_of_dir_record(self, year: str, month: str, day: str) -> list:
        if os.path.exists(os.path.join(self.path, os.path.join(year, os.path.join(month, day)))) is True:
            self.path_day = os.path.join(os.path.join(self.path, os.path.join(year, os.path.join(month, day))))
            return os.listdir(os.path.join(self.path, os.path.join(year, os.path.join(month, day))))

    def create_dir_year(self, name_of_year: str) -> None:
        if os.path.exists(os.path.join(self.path, name_of_year)) is False:
            # print(os.path.join(self.path, name_of_year))
            os.mkdir(os.path.join(self.path, name_of_year))

    def create_dir_month(self, name_of_month: str) -> None:
        if os.path.exists(os.path.join(self.path_year, name_of_month)) is False:
            # print(os.path.join(self.path_year, name_of_month))
            os.mkdir(os.path.join(self.path_year, name_of_month))

