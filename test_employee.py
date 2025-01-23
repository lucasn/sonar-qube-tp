from Employee import Employee
import pytest

@pytest.fixture
def employee_instance():
    employee = Employee('Paul', 'Paul', 10)
    return employee

def test_should_retrieve_employee_fullname(employee_instance):
    assert employee_instance.fullname() == 'Paul Paul'

def test_should_retrieve_employee_str(employee_instance):
    assert employee_instance.__str__() == \
          "Paul Paul Paul.Paul@ec-nantes.fr, jours restants : 10"