"""Test module for testing graviton
"""
import pytest

from pygc import gravitino


class TestGravitino:
    """Sample Test-Group-class for Gravitino class"""

    def test_name_without_fixture(self):
        """Test name, notice the 'g' argument in the signature

        Note: This test is failing on purpose to show Assertion Error
        """
        g = gravitino.Gravitino()
        assert g.name == 'graviton'

    @pytest.fixture(scope='class')
    def g(self):
        """Sample fixture only available within a class"""
        return gravitino.Gravitino()

    def test_name_with_fixture(self, g):
        """Test name, notice the 'g' argument in the signature"""
        assert g.name == 'gravitino'

    def test_gravitino_spin_error(self, g):
        """Test Gravitino spin raises error"""
        with pytest.raises(NotImplementedError):
            g.spin
