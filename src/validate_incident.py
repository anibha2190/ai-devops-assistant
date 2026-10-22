import json
from pathlib import Path

REQUIRED_FIELDS = {"id", "description"}

def validate_incidents(incidents):

    if not isinstance(incidents, list):
        raise ValueError("Incident data must be a JSON list.")

    if not incidents:
        raise ValueError("Incident list cannot be empty.")

    seen_ids = set()

    for index, incident in enumerate(incidents):
        if not isinstance(incident, dict):
            raise ValueError(f"Incident at index {index} must be a JSON object.")

        missing = REQUIRED_FIELDS - incident.keys()
        if missing:
            raise ValueError(f"Incident at index {index} is missing fields: "
                             f"{', '.join(sorted(missing))}"
            )

        incident_id = incident["id"]
        if not isinstance(incident_id, (str,int)) or isinstance(incident_id, bool):
            raise ValueError(f"Incident ID at index {index} has an invalid id.")

        incident_id = str(incident_id).strip()
        if not incident_id:
            raise ValueError(f"Incident ID at index {index} has an empty id.")

        if incident_id in seen_ids:
            raise ValueError(f"duplicate incident id: {incident_id}")

        seen_ids.add(incident_id)

        description = incident["description"]
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"Incident {incident_id} has an empty or invalid description.")

    return True

def load_and_validate_incidents(file_path):
    
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            incidents = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    
    validate_incidents(incidents)
    return incidents


        





        



        
    
        


    