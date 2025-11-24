import dataclasses
import enum

class OperationTypeBitFlag(enum.IntFlag):
    READ = 1
    WRITE = 2
    CREATE = 4
    UPDATE = 8
    DELETE = 16

@dataclasses.dataclass
class Permission:
    """
    Data structure to represent permissions assigned to either an user or a role
    """
    id: int
    user_id: int|None
    role_id: int|None
    module: int
    operation_type: OperationTypeBitFlag


def validate_permission(permission: Permission, operation_types: list[OperationTypeBitFlag]):
    for operation_type in operation_types:
        if permission.operation_type & operation_type:
            continue
        else:
            return False
    
    return True

