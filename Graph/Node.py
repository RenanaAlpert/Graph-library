class Node:
    """This class represents vertex in graph."""

    def __init__(self, value, id_count: int):
        """ Constructor. """
        self.__value = value
        self.__id = id_count
        self.info = {}

    def get_value(self):
        """
        Returns the value of the node.
        @return: __value
        """
        return self.__value

    def get_id(self) -> int:
        """
        Returns the id of the node.
        :return: __id
        """
        return self.__id

    def __lt__(self, other):
        return self.info['key'] < other.info['key']
