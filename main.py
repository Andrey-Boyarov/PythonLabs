class Record:
    def __init__(self, unique_id: int):
        self.__age: int = 18
        self.__unique_id: int = unique_id
        self.__name: str = ""

    def __str__(self) -> str:
        return "uniqueId: " + str(self.__unique_id) + " | Name: " + self.name + " | Age : " + str(self.__age)

    def __repr__(self):
        return f"Record(uniqueId : '{self.__unique_id}', Name: '{self.__name}', Age: '{self.age}')"

    @property
    def unique_id(self) -> int:
        return self.__unique_id

    @property
    def age(self) -> int:
        return self.__age

    @property
    def name(self) -> str:
        return self.__name

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name


class RecordList:
    def __init__(self):
        self.__records = {}

    def __str__(self) -> str:
        return "\n".join(str(i) for i in self.__records.values())

    def read_records(self, string_arg):
        with open(string_arg, 'r') as f:
            for i in f.readlines():
                if i == '' or i == '\n':
                    continue
                data = i.strip("\n").split(',')
                if len(data) != 3:
                    continue
                try:
                    unique_id = int(data[0])
                    age = int(data[2])
                except ValueError:
                    continue
                if unique_id in self.__records.keys():
                    continue
                record = Record(unique_id)
                record.age = age
                record.name = data[1]
                self.__records[unique_id] = record

    def load(self, file: str) -> None:
        self.read_records(file)

    def save(self, file: str) -> None:
        with open(file, "wt") as output:
            print(str(self), file=output)

    def sort_by_id(self) -> None:
        self.__records = dict(sorted(self.__records.items(), key=lambda x: x[1].unique_id, reverse=False))

    def sort_by_name(self) -> None:
        self.__records = dict(sorted(self.__records.items(), key=lambda x: x[1].name, reverse=False))

    def sort_by_age(self) -> None:
        self.__records = dict(sorted(self.__records.items(), key=lambda x: x[1].age, reverse=False))

    @property
    def records(self) -> dict:
        return self.__records

    @records.setter
    def records(self, records: dict) -> None:
        self.__records = records

    def record(self, unique_id: int) -> Record:
        return self.__records[unique_id]

    def set_record(self, unique_id: int, record: Record):
        self.__records[unique_id] = record

    @staticmethod
    def merge(record_1, record_2):
        result = RecordList()
        result.__records = {**record_1.__records, **record_2.__records}
        return result

    @staticmethod
    def intersect(record_1, record_2):
        a = dict()
        for i in record_1.__records.keys() & record_2.__records.keys():
            a[i] = record_1.__records[i]
        return {i: record_1.__records[i] for i in record_1.__records.keys() & record_2.__records.keys()}


if __name__ == '__main__':
    recordList1 = RecordList()
    recordList1.load('test_one.csv')
    print("\n\nList one\n", recordList1)

    recordList2 = RecordList()
    recordList2.load('test_two.csv')
    print("\n\nList two\n", recordList2)

    print("\n\nMerged\n")
    print(RecordList.merge(recordList1, recordList2))
    print("\n\nIntersect\n")
    print(RecordList.intersect(recordList1, recordList2))

    recordList3 = RecordList()
    recordList3.load('test_two.csv')
    print("\n\nSort by id\n")
    print('Before sort', recordList3)
    recordList3.sort_by_id()
    print('\nAfter sort', recordList3)

    recordList3.load('test_two.csv')
    print("\n\nSort by name\n")
    print('Before sort', recordList3)
    recordList3.sort_by_name()
    print('\nAfter sort', recordList3)

    recordList3.load('test_two.csv')
    print("\n\nSort by age\n")
    print('Before sort', recordList3)
    recordList3.sort_by_age()
    print('\nAfter sort', recordList3)
