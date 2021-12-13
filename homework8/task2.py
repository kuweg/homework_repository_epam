import sqlite3


class TableData:
    """Wrapper class for database table which acts as collection object.

    :param database_path: path to database
    :type database_path: str
    :param table_name: name of chose table in database file
    :type table_name: str
    """

    def __init__(self, database_path, table_name) -> None:
        """Class constructor"""
        self.database_path = database_path
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def connect_to_database(self):
        """Connection or reconnecting to a database.
        Allows to reconnect to database without creating
        a new instance of object in case of disconection.
        """
        self.connection = sqlite3.connect(self.database_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """Closing connection to a database."""
        self.connection.close()

    def __len__(self):
        """Returns amount of rows in datatable"""
        self.cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        """Returns a row data with datatable[item] construction.
        :param item: requested element from database
        :type item: str
        :return: a row from data base
        :rtype: tuple
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {'item': item}
        )
        return tuple(self.cursor.fetchone())

    def __contains__(self, item):
        """Allows check contains of element using construction
            'element in datatable[item]'.

        :param item: requested element from database
        :type item: str
        :return: element if exist
        :rtype: bool
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:item", {'item': item}
        )
        return self.cursor.fetchone()

    def __iter__(self):
        """Allows iterating through datatable's row"""
        self.cursor.execute(
            f"SELECT * from {self.table_name}"
        )
        return self

    def __next__(self):
        """Allows iterating trough datatable's rows."""
        output = self.cursor.fetchone()
        if output is not None:
            return output
        raise StopIteration


if __name__ == "__main__":
    db_path = 'homework8/example.sqlite'
    presidents = TableData(db_path, 'presidents')
    print(len(presidents))
    print(presidents['Trump'])
    for president in presidents:
        print(president['name'])
