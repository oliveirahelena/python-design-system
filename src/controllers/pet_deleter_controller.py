from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.controllers.interfaces.pet_deleter_controller import (
    PetDeleterControllerInterface,
)


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self._pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self._pet_repository.delete_pets(name)
