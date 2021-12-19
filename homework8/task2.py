import abc
import os
import sqlite3
from contextlib import contextmanager


class AbsctractDatabaseClass:
    """
    Abstract class for future databases realizations.
    """

    @abc.abstractmethod
    def connection_manager(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def select(self, * args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def count(self, * args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def select_by_name(self, * args, **kwargs):
        raise NotImplementedError


class SQLiteClass(AbsctractDatabaseClass):
    """
    Class for sql request based tables, which can be accessed
    using sqlite3 library.

    :param db_path: path to database
    :type db_path: str

    """

    _select_template = 'SELECT * FROM {}'
    _count_template = 'SELECT COUNT(*) FROM {}'
    _select_by_name_template = 'SELECT * FROM {} WHERE name=:name'

    def __init__(self, db_path) -> None:
        if os.path.isfile(db_path):
            self. db_path = db_path
        else:
            raise FileExistsError('File does not exist')
        super().__init__()

    @contextmanager
    def connection_manager(self):
        """
        Safe connection manager for database accessing.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            yield cursor
        finally:
            connection.close()

    def count(self, table_name):
        """
        Generates a 'SELECT COUNT(*)...' request
        with provided table name.

        :param table_name: name of table
        :type table_name: str
        :return: result of sql request
        :rtype: int
        """
        with self.connection_manager() as cursor:
            cursor.execute(
                self._count_template.format(table_name)
            )
            return cursor.fetchone()[0]

    def select(self, table_name):
        """
        Generates a 'SELECT * FROM ...' request
        with provided table name.

        :param table_name: name of table
        :type table_name: str
        """
        with self.connection_manager() as cursor:
            cursor.execute(
                self._select_template.format(table_name)
                )
            return cursor.fetchall()

    def select_by_name(self, table_name, item):
        """
        Generates a request to get a row by provided item
        from a certain table.

        :param table_name: name of table
        :type table_name: str
        :param item: provied item
        :type item: str
        :return: sql request
        :rtype: sqlite3.Row
        """
        with self.connection_manager() as cursor:
            cursor.execute(
                self._select_by_name_template.format(
                    table_name), {"name": item}
            )
            return cursor.fetchone()


class TableData:
    """
    Wrapper class for database table which acts as collection object.

    :param database_path: path to database
    :type database_path: str
    :param table_name: name of chose table in database file
    :type table_name: str
    """

    def __init__(self, Database, table_name) -> None:
        """
        Class constructor.
        """
        if not table_name.isalnum():
            raise NameError
        self.table_name = table_name
        self.db = Database

    def __len__(self):
        """Returns amount of rows in datatable."""
        return self.db.count(self.table_name)

    def __getitem__(self, item):
        """
        Returns a row data with datatable[item] construction.

        :param item: requested element from database
        :type item: str
        :return: a row from data base
        :rtype: tuple
        """
        row = self.db.select_by_name(self.table_name, item)
        print(type(row))
        return tuple(row)

    def __contains__(self, item):
        """
        Allows check contains of element using construction
            'element in datatable[item]'.

        :param item: requested element from database
        :type item: str
        :return: element if exist
        :rtype: bool
        """
        return self.db.select_by_name(self.table_name, item)

    def __iter__(self):
        """Allows iterating through datatable's row."""
        yield from self.db.select(self.table_name)


if __name__ == "__main__":
    db_path = "homework8/example.sqlite"
    db = SQLiteClass(db_path)
    presidents = TableData(db, "presidents")
    print(len(presidents))
    print(presidents["Trump"])
    print('Putin' in presidents)
    for president in presidents:
        print(president["name"])
