import abc
import os
import sqlite3


class MetaSingleton(type):
    """Sigleton metaclass"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls
                ).__call__(*args, **kwargs)
        return cls._instances[cls]


class AbsctractDatabaseClass:
    """
    Abstract class for future databases realizations.
    """

    @abc.abstractmethod
    def select(self, * args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def count(self, * args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def select_by_name(self, * args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def close_connection(self, * args, **kwargs):
        raise NotImplementedError


class RelationalDataBase:
    """
    Base class for relational databases requests.
    """
    @property
    def _select_template(self):
        return 'SELECT * FROM {}'

    @property
    def _count_template(self):
        return 'SELECT COUNT(*) FROM {}'

    @property
    def _select_by_name_template(self):
        return 'SELECT * FROM {} WHERE name=:name'


class DatabaseConnection(metaclass=MetaSingleton):
    """A Singleton class which provides connection to a database."""

    def __init__(self, database_path) -> None:
        """Initalize connection to databese if database file exists.

        :param database_path: path to database file
        :type database_path: str
        """
        self.db_path = database_path
        if os.path.isfile(database_path):
            self.connection = sqlite3.connect(database_path)
        else:
            raise FileExistsError('File does not exist')

    def get_cursor(self):
        """Initialize cursor object with row factory sqlite3.Row.

        :return: cursor object
        """
        self.connection.row_factory = sqlite3.Row
        self.cursorobj = self.connection.cursor()
        return self.cursorobj

    def close_connection(self):
        """Close connection"""
        self.connection.close()


class SQLiteClass(AbsctractDatabaseClass,
                  RelationalDataBase):
    """
    Class for sql request based tables, which can be accessed
    using sqlite3 library.

    :param db_path: path to database
    :type db_path: str

    """

    def __init__(self, db_path) -> None:
        self.db_connection = DatabaseConnection(db_path)
        self.cursor = self.db_connection.get_cursor()
        super().__init__()

    def count(self, table_name):
        """
        Generates a 'SELECT COUNT(*)...' request
        with provided table name.

        :param table_name: name of table
        :type table_name: str
        :return: result of sql request
        :rtype: int
        """
        self.cursor.execute(
                self._count_template.format(table_name)
            )
        return self.cursor.fetchone()[0]

    def select(self, table_name):
        """
        Generates a 'SELECT * FROM ...' request
        with provided table name.

        :param table_name: name of table
        :type table_name: str
        """
        self.cursor.execute(
                self._select_template.format(table_name)
                )
        return self.cursor.fetchall()

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

        self.cursor.execute(
                self._select_by_name_template.format(
                    table_name), {"name": item}
            )
        return self.cursor.fetchone()

    def close_connection(self):
        """Closing connection"""
        self.db_connection.close_connection()


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

    def close_connection(self):
        """Closing connection """
        self.db.close_connection()


if __name__ == "__main__":
    db_path = "homework8/example.sqlite"
    db = SQLiteClass(db_path)
    presidents = TableData(db, "presidents")
    print(len(presidents))
    print(presidents["Trump"])
    print('Putin' in presidents)
    for president in presidents:
        print(president["name"])
    db2 = SQLiteClass(db_path)
    p = TableData(db2, 'presidents')
    print(id(presidents.db.db_connection))
    print(id(p.db.db_connection))
