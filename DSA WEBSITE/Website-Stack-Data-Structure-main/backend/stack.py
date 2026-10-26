class HistoryBuffer:


    def __init__(self, items=None):
        self._records = list(items) if items is not None else []

    def push(self, item):

        self._records.append(item)

    def pop(self):

        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._records.pop()

    def peek(self):

        if self.is_empty():
            raise IndexError("The recovery tray is empty.")
        return self._records[-1]

    def is_empty(self):

        return len(self._records) == 0

    def size(self):

        return len(self._records)

    def to_list(self):

        return self._records.copy()
    
