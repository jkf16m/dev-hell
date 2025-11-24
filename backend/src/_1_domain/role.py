import dataclasses
import _1_domain.permission as m_permission
import _1_domain.user as m_user

@dataclasses.dataclass
class Role:
    """
    Stores a set of permissions, which can then be applied to a specific
    user
    """

    id: int
    name: str
    permissions: list[m_permission.Permission]


def add_permission(role: Role, permission: m_permission.Permission):
    role.permissions.append(permission)