"""Sample dependent Python module for illustrating best practices
"""

from pygc.graviton import Particle


class Gravitino(Particle):
    """Sample class"""

    def __init__(self):
        """Create a gravitino particle"""
        super().__init__(name='gravitino')

    # Purposefully Not Implemented to show dependency failure
    # @property
    # def spin(self):
    #     """Graviton spin"""
    #     return ?
