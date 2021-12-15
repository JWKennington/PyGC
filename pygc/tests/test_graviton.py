"""Test module for testing graviton
"""
import pytest

from pygc import graviton


def test_square_spin_completion():
    """Test square_spin: completion only"""
    res = graviton.square_spin(spin=0.5)
    assert isinstance(res, float)


def test_square_spin_correctness():
    """Test square_spin: correctness"""
    res = graviton.square_spin(spin=0.5)
    assert res == 0.25


@pytest.mark.parametrize("spin,expected", [(2.0, 4.0), (3.0, 9.0), (4.0, 16.0)])
def test_square_spin_parametric(spin: float, expected: float):
    """Test square_spin multiple arguments"""
    res = graviton.square_spin(spin=spin)
    assert res == expected


@pytest.fixture
def simple_fixture():
    """Sample fixture, can be requested by inclusion in function signature"""
    return 2


def test_simple_fixture(simple_fixture):
    """Test demonstrating sample fixture"""
    assert simple_fixture == 2


class TestGraviton:
    """Sample Test-Group-class for Graviton class"""

    def test_name_without_fixture(self):
        """Test name, notice the 'g' argument in the signature"""
        g = graviton.Graviton()
        assert g.name == 'graviton'

    @pytest.fixture(scope='class')
    def g(self):
        """Sample fixture only available within a class"""
        return graviton.Graviton()

    def test_name_with_fixture(self, g):
        """Test name, notice the 'g' argument in the signature"""
        assert g.name == 'graviton'
