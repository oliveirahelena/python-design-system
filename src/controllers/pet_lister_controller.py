from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from src.controllers.interfaces.pet_lister_controller import (
    PetListerControllerInterface,
)


class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self._pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self._get_pets_in_db()
        response = self._format_response(pets)
        return response

    def _get_pets_in_db(self) -> List[PetsTable]:
        pets = self._pet_repository.list_pets()
        return pets

    def _format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
