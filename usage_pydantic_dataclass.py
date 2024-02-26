import yaml
from pydantic import BaseModel
from pathlib import Path


class Pet(BaseModel):
    name: str
    species: str
    skills: dict[str, str]


class User(BaseModel):
    name: str
    age: int
    file: Path

    pets: list[Pet] = []

    @property
    def greeting(self):
        return f"Hello, I'm {self.name}"


def main() -> None:
    with Path(r"config.yaml").open() as f:
        config = yaml.safe_load(f.read())

    config["users"][2]["pets"] = [Pet(name="Chocolately", species="cat", skills={})]

    users = [User(**u) for u in config["users"]]
    users[1].pets = [Pet(name="Muñeca", species="dog", skills={})]
    # print(users)

    users2 = [User.model_validate(u) for u in config["users"]]
    print(User.model_fields)
    print(users2)


if __name__ == "__main__":
    main()
