import pytest

@pytest.fixture
def sample_data():
    """Fixture qui fournit des donn´ees de test."""
    return {"name": "Alice", "age": 30}

@pytest.fixture(scope="class")
def setup_class_level():
    """Fixture ex´ecut´ee une fois par classe de test."""
    return {"message": "Hello from class-level setup"}
# Classe de test
class TestExample:
    def test_data_content(self, sample_data):
        """Test utilisant la fixture sample_data."""
        assert sample_data["name"] == "Alice"
        assert sample_data["age"] == 30
    def test_data_modification(self, sample_data):
        """Test qui modifie les donn´ees fournies par la fixture."""
        sample_data["name"] = "Bob"
        assert sample_data["name"] == "Bob"
        assert sample_data["age"] == 30
    def test_class_fixture(self, setup_class_level):
        """Test utilisant une fixture avec une port´ee de classe."""
        assert setup_class_level["message"] == "Hello from class-level setup"