from abc import ABC, abstractmethod
from database.in_memory_db import get_in_memory_db
from models.base_model import BaseModel

# ---------------------------------------------------------- #

class AbstractBaseDAO(ABC):

    @abstractmethod
    def create(self, obj: BaseModel):
        pass

    @abstractmethod
    def read(self, filter: dict | None = None):
        pass

    @abstractmethod
    def update(self, values: dict, fiter: dict | None = None):
        pass

    @abstractmethod
    def delete(self, filter: dict | None = None):
        pass


class BaseDAO(AbstractBaseDAO):

    def __init__(self, entity: str):
        self.db_cls = get_in_memory_db()
        if hasattr(self.db_cls, entity):
            self.entity_data = getattr(self.db_cls, entity)


    def create(self, obj: BaseModel) -> BaseModel:
        self.entity_data.append(obj)
        return self.entity_data[-1]


    def read(self, filter: dict | None = None) -> list[BaseModel] | list[None]:
        if not filter:
            return self.entity_data
        
        return [obj for obj in self.entity_data if self._match(obj, filter)]
    

    def update(self, values: dict, filter: dict | None = None) -> int:
        updated_count = 0
        
        if not filter:
            for obj in self.entity_data:
                for k, v in values.items():
                    setattr(obj, k, v)
                    updated_count += 1
        else:
            for obj in self.entity_data:
                if self._match(obj, filter):
                    for k, v in values.items():
                        setattr(obj, k, v)
                        updated_count += 1
                        
        return updated_count
    

    def delete(self, filter: dict | None = None):

        original_size = len(self.entity_data)

        if not filter:
            self.entity_data = []

        self.entity_data[:] = [obj for obj in self.entity_data if not self._match(obj, filter)]

        return original_size - len(self.entity_data)
        

    def _match(self, obj: BaseModel, filter):
        obj = obj.to_dict()
        return all(obj.get(k) == v for k, v in filter.items())