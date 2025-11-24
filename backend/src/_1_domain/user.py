from dataclasses import dataclass
import shared.str as m_str

@dataclass
class User:
    id: int
    alias: str
    name: str
    lastname: str


def create(alias: str, name: str, lastname: str, id: int = 0):
    """Creates a user

    Parameters:
        id(int):
            Id of the user, can have default value equal to zero
            to represent a new user.
        alias(str):
            Alias of the user, cannot be longer than 50 characters long
        name(str):
            Name of the user, cannot be longer than 200 characters long
        lastname(str):
            Lastname of the user, cannot be longer than 200 characters long
    
    Returns:
        (int,User):A tuple, containing the error code, and the instance
        The following error codes, depending on the case:
        0: No error, the second element has the instance of the user.
        1: Wrong type Error: if any of the parameters are not of the
        expected type
        2: Size bound Error: if any of the parameters, do have information
        exceeding the expected length or size.
        3: Not implemented Error: The code doesn't have any implementation done
    """
    ret = User()
    return (3, None)