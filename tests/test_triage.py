import unittest

from src.triage import classify_incident

class testIncidentTriage(unittest.TestCase):

    def test_cpu_incident(self):
        incident = {
            "id": "TEST-001",
            "title": "High CPU usage",
            "description": "CPU usage is 95 percent."
        }

        result = classify_incident(incident)

        self.assertEqual(result["severity"], "Low")
        self.assertEqual(result["category"], "general")

    def test_deployment_failure(self):
        incident = {
            "id": "TEST-002",
            "title": "Deployment Failed",
            "description": "the release failed."
        }

        result = classify_incident(incident)

        self.assertEqual(result["severity"], "High")
        self.assertEqual(result["category"], "Deployment")

    def test_network_timeout(self):
        incident = {
            "id": "TEST-003",
            "title": "Connection timeout.",
            "description": "backend connection timed out."
        }

        result = classify_incident(incident)

        self.assertEqual(result["severity"], "High")
        self.assertEqual(result["category"], "Networking")

    def test_outage_is_critical(self):
        incident = {
            "id": "TEST-004",
            "title": "Service unavailable.",
            "description": "The service is down."
        }

        result = classify_incident(incident)

        self.assertEqual(result["severity"], "Critical")

if __name__ == "__main__":
    unittest.main()