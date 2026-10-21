import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "incidents.json"
OUTPUT_FILE = PROJECT_ROOT / "reports" / "triage_report.json"

def classify_incident(incident):
    title = incident.get("title", "").lower()
    description = incident.get("description", "").lower()
    text = f"{title} {description}"

    if any(word in text for word in [
        "outage", "unavailable", "service down"
    ]):
        severity = "Critical"
    elif any(word in text for word in [
        "failed", "failure", "timeout", "error"
    ]):
        severity = "High"
    elif any(word in text for word in [
        "CPU", "memory", "latency", "slow"
    ]):
        severity = "Medium"
    else:
        severity = "Low"

    if any(word in text for word in [
        "CPU", "memory", "latency", "slow"
    ]):
        category = "Performance"
    elif any(word in text for word in [
        "network", "connection", "firewall", "dns"
    ]):
        category = "Networking"
    elif any(word in text for word in [
        "deploy", "deploymenyt", "container", "image pull"
    ]):
        category = "Deployment"
    else:
        category = "general"

    return {
        **incident,
        "severity": severity,
        "category": category,
        "status": "Needs investigation"
    }

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Incident input file not found: {INPUT_FILE}"
        )
    
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        incidents = json.load(file)
        
    if not isinstance(incidents, list):
        raise ValueError("Input must contain a json list of incidents,")
    
    results = []
    for incident in incidents:
        if not isinstance(incident, dict):
            raise ValueError("Every incident must be a JSON object.")
        if not incident.get("id") or not incident.get("title"):
            raise ValueError("Every incident need an id and title.")
        
        results.append(classify_incident(incident))
        
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)

    print(f"Processed {len(results)} incidents.")
    print(f"Report saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()