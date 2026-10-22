import  unittest

from src.validate_incident import validate_incidents

class TestIncidentValidation(unittest.TestCase):

    def test_valid_incident(self):
        incidents = [
            {
                "id": "INC001",
                "description": "High CPU usage"
            }
        ]
        self.assertTrue(validate_incidents(incidents))

    def test_empty_list(self):
        with self.assertRaisesRegex(ValueError, "Incident list cannot be empty."):
            validate_incidents([])

    def test_missing_description(self):
        incidents = [
            {
                "id": "INC002"
            }
        ]
        with self.assertRaisesRegex(ValueError, "missing fields"):
            validate_incidents(incidents)

    def test_duplicate_ids(self):
        incidents = [
            {id: "INC003", "description": "First incident"},
            {id: "INC003", "description": "second incident"}
        ]
        with self.assertRaisesRegex(ValueError, "Incident at index 0 is missing fields: id"):
            validate_incidents(incidents)

    def test_empty_description(self):
        incidents = [
            {
                "id": "INC004",
                "description": ""
            }
        ]
        with self.assertRaisesRegex(ValueError, "empty or invalid description"):
            validate_incidents(incidents)

if __name__ == "__main__":
    unittest.main()



