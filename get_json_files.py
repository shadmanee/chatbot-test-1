import os
import json

root_folder   = "./messenger-data" # root/source folder name
output_folder = "./final_json_data" # destination folder name

os.makedirs(output_folder, exist_ok=True)

messages = []
i = 1

"""
This file extracts the JSON files from folders in different sublevels in the root folder with raw folder heirarchies and stores only the JSON files containing your messages to the destination folder.
"""

while True:
    target_name = f"message_{i}.json"
    found_any  = False

    for dirpath, dirnames, filenames in os.walk(root_folder):
        if target_name in filenames:
            found_any = True
            full_path   = os.path.join(dirpath, target_name)
            folder_name = os.path.basename(dirpath)

            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    messages.append(data)

                base_fname = f"{folder_name}_message_{i}.json"
                out_path   = os.path.join(output_folder, base_fname)

                if os.path.exists(out_path):
                    name, ext = os.path.splitext(base_fname)
                    suffix = 1
                    while True:
                        candidate = os.path.join(output_folder, f"{name}_{suffix}{ext}")
                        if not os.path.exists(candidate):
                            out_path = candidate
                            break
                        suffix += 1

                with open(out_path, "w", encoding="utf-8") as out_f:
                    json.dump(data, out_f, indent=2, ensure_ascii=False)

                print(f"Wrote {out_path}")

            except json.JSONDecodeError as e:
                print(f"JSON error in {full_path}: {e!r}")

    if not found_any:
        break

    i += 1

print(f"\nTotal loaded messages: {len(messages)}")
