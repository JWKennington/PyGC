"""Sample python module for illustrating best practices
"""


class Particle:
    """Sample base class"""

    def __init__(self, name: str):
        """Create a Particle

        Args:
            name, str, name of particle
        """
        self.name = name

    @property
    def spin(self):
        """Stub method for particle spin"""
        raise NotImplementedError


class Graviton(Particle):
    """Sample class"""

    def __init__(self):
        """Create a graviton particle"""
        super().__init__(name='graviton')

    @property
    def spin(self):
        """Graviton spin"""
        return 2


def square_spin(spin: float) -> float:
    """Squared value of the spin

    Args:
        spin:
            float, the particle spin to be squared

    Returns:
        float, the squared spin
    """
    return spin ** 2
