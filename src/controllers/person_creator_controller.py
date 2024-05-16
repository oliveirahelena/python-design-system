import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.controllers.interfaces.person_creator_controller import (
    PersonCreatorControllerInterface,
)


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, peopple_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = peopple_repository

    def create(self, person_info: dict) -> None:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        return self.__format_response(person_info)

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        non_valid_caracters = re.compile(r"[^a-zA-Z]")

        if non_valid_caracters.search(first_name) or non_valid_caracters.search(
            last_name
        ):
            raise ValueError("First name and last name can only contain letters")

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {"data": {"type": "Person", "count": 1, "attributes": person_info}}
