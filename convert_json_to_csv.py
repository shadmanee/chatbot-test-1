import os, json, time, uuid
import pandas as pd

DIR_NAME = "./final_json_data"
COLUMNS = ["Self", "Others", "ID", "Timestamp", "Title", "Sender", "Content", "Image", "Emoji", "Link", "Unsent", "Active"]

# These are the names of the columns I think can be in the df (before text-based preprocessing)
"""
Self -> Shadmanee Tasneem (str)
Others -> Other participants (list of str)
ID -> Unique ID for each message
Timestamp -> Time that the message was sent
Title -> Title of the conversation/chat
Sender -> Sender of each message
Content -> Content of each message
Boolean values:
Image -> Is the message just an image?
Emoji -> Is the message an emoji or does it contain any emojis?
Link -> Is the message a link or does it contain any links?
Unsent -> Has the message been unsent by the sender?
"""


def time_for_action(action, start, end):
    print(f"TIME => {action}: {int((end - start) / 60)} minutes and {int((end - start) % 60)} seconds.")

def get_column_names():
    fixed_keys = []

    find_columns_start = time.time()

    for dirpath, _, filenames in os.walk(DIR_NAME):
        for fn in filenames:
            json_file_path = os.path.join(dirpath, fn)
            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)               
                    new_keys = [key for key in data.keys() if key not in fixed_keys]
                    if len(new_keys) != 0:
                        # print(fn, "new: ", new_keys)
                        fixed_keys = fixed_keys + new_keys
            except Exception as e:
                print(e)

    if len(fixed_keys) != 0:
        find_columns_end = time.time()
        time_for_action(action="Finding column names", start=find_columns_start, end=find_columns_end)
        return fixed_keys
    
    raise Exception("No columns found")

def process_dictionary():
    """
    This function converts the dictionaries in the JSON files to df-convertible format. It is not completed yet. This docstring will be much more specific once I have an idea of what I am going to do in this function.
    """
    for dirpath, _, filenames in os.walk(DIR_NAME):
        for fn in filenames:
            json_file_path = os.path.join(dirpath, fn)
            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    participants = data.get("participants", None)
                    messages = data.get("messages", None)
                    
                    if participants is not None:
                        self = ["Shadmanee Tasneem"]
                        others = []
                        if len(participants) > 1:
                            others = [participant["name"] for participant in participants if participant["name"] not in self]

                        j = 1
                        
                        for i, other in enumerate(others):
                            if other == "":
                                others[i] = f"Unknown_{j}"
                                j += 1

                        others_n = len(others)
                    
                    if messages is not None:
                        all_message_in_conversation = []
                        if len(messages) != 0:
                            for message in messages:
                                sender = message.get("sender_name", "Unknown")
                                timestamp_ms = message.get("timestamp_ms", None)
                                content = message.get("content", None)
                                unsent = message.get("is_unsent_by_messenger_kid_parent", None)

                                if content is None:
                                    continue





                            
                            

                    # for key, value in data.items():
                    #     print(key, value)
                break
            except Exception as e:
                print(e)

if __name__ == "__main__":
    # df_cols = get_column_names()
    # print(df_cols)
    process_dictionary()

    