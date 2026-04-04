import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        try:
            filled = template
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key)
                if value is None or value == "":
                    value = "N/A"
                filled = filled.replace("{" + key + "}", str(value))
            filename = f"output_{idx}.txt"
            with open(filename, "w") as f:
                f.write(filled)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error processing attendee {idx}: {e}")
