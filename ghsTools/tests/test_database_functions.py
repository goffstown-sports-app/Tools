import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pytest
import sys

sys.path.append("..")
from main import ghsTools

@pytest.fixture(autouse=True, scope="session")
def run_around_tests():
    sys.path.append("..")
    cred = credentials.Certificate("firestore_creds.json")
    firebase_admin.initialize_app(
        cred, {
            "databaseURL": "https://ghs-app-5a0ba.firebaseio.com/",
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    assert True == True
    
def test_update_pulse():
    """Tests for the update pulse function
    """
    instance = ghsTools().update_pulse(0, "toolsPkgCI")
    ref = db.reference("db-info/pulses/toolsPkgCI")
    ref_data = ref.get()
    ref.set({})
    assert instance == ref_data
    
def test_set_monitoring_info():
    """Tests for the set monitoring info function
    """
    instance = ghsTools().set_monitoring_info(False, 0, "toolsPkgCI")
    ref = db.reference("db-info/monitoring/toolsPkgCI")
    ref_data = ref.get()
    ref.set({})
    assert ref_data == instance
    
def test_game_of_field():
    """Test for the game on field function
    """
    football_field_instance = ghsTools().game_on_field("football-field")
    gym_instance = ghsTools().game_on_field("gym")
    softball_field_instance = ghsTools().game_on_field("softball-field")
    assert type(football_field_instance) == type(True)
    assert type(gym_instance) == type(True)
    assert type(softball_field_instance) == type(True)
