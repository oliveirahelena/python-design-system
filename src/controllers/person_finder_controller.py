from typing import Dict
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from src.controllers.interfaces.person_finder_controller import (
    PersonFinderControllerInterface,
)
from src.errors.error_types.http_not_found import HttpNotFoundError


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self._people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self._find_person_in_db(person_id)
        return self._format_response(person)

    def _find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self._people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoa não encontrada")
        return person

    def _format_response(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                },
            }
        }
