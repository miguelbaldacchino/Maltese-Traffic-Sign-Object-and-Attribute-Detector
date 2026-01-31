import json
import urllib.parse
from pathlib import Path

# --- CONFIGURATION ---# Change this line:
input_json_path = "C:/GitHub/Advanced-CV---Group-Assignment/ARI3129 - Assignment Materials/reissueswithmembermerger_ipynb/Merger/merged_input.json"
output_json_path = "merged_inputs_clean.json" # The new file we will create
# ---------------------

print(f"Reading {input_json_path}...")
with open(input_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def clean_path(path_str):
    """Decodes URL characters and extracts just the filename."""
    if not path_str or not isinstance(path_str, str):
        return path_str
    # 1. Decode URL (converts %5C back to \)
    decoded = urllib.parse.unquote(path_str)
    # 2. Extract just the filename (e.g., 20251112_123441.jpg)
    filename = Path(decoded).name
    # 3. Strip any leftover query parameters (like ?d=...) if Path didn't catch them
    if "?" in filename:
        filename = filename.split("?")[-1]
    return filename

# Handle Label Studio JSON format (List of tasks)
if isinstance(data, list):
    count = 0
    for task in data:
        # Check standard LS keys
        task_data = task.get("data", {})
        
        # Clean 'image' key
        if "image" in task_data:
            original = task_data["image"]
            task_data["image"] = clean_path(original)
            if original != task_data["image"]:
                count += 1
                
        # Clean 'file_upload' key (often used as ID)
        if "file_upload" in task:
            task["file_upload"] = clean_path(task["file_upload"])

    print(f"[OK] Cleaned {count} paths in Label Studio list format.")

# Handle COCO format (Dictionary with 'images' key)
elif isinstance(data, dict) and "images" in data:
    count = 0
    for img in data["images"]:
        if "file_name" in img:
            original = img["file_name"]
            img["file_name"] = clean_path(original)
            if original != img["file_name"]:
                count += 1
    print(f"[OK] Cleaned {count} paths in COCO dictionary format.")

else:
    print("[WARN] Unknown JSON structure. Could not sanitize.")

# Save the result
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved clean JSON to: {output_json_path}")
print("Use this file as your input for LS2COCO!")