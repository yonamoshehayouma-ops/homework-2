# import os
# from pathlib import Path
# current_dir = os.getcwd()
# print(current_dir)
#
# files_dir = os.path.join(current_dir, "files")
# file_path = os.path.join(files_dir, "text.data")
#
# print(file_path)
#
# home_dir = str(Path.home())
# print(home_dir)

# from pathlib import Path
# file_path = Path("txt.notes")
# if file_path.exists():
#     print("exists")
# else:
#     file_path.write_text("new file")
#     print("new file")
# content = file_path.read_text(encoding="utf-8")
# print("תוכן הקובץ:")
# print(content)

# from pathlib import Path
#
# # הנתיב הנתון
# path = Path('documents/reports/annual_report.pdf')
#
# # שם הקובץ כולל סיומת
# print("שם הקובץ (כולל סיומת):", path.name)
#
# # שם הקובץ ללא סיומת
# print("שם הקובץ (ללא סיומת):", path.stem)
#
# # סיומת הקובץ
# print("סיומת הקובץ:", path.suffix)
#
# # תיקיית האב
# print("תיקיית האב (parent):", path.parent)
#
# # כל התיקיות בנתיב (parents)
# print("כל התיקיות בנתיב (parents):", list(Path.parents))
import os

import os

# קבלת התיקיה הנוכחית
current_dir = os.getcwd()
print("תוכן התיקיה הנוכחית:", current_dir)


folder_count = 0
file_count = 0


for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    if os.path.isdir(item_path):
        print(" תיקיה:", item)
        folder_count += 1
    elif os.path.isfile(item_path):
        print(" קובץ:", item)
        file_count += 1


print("\nסיכום:")
print("מספר תיקיות:", folder_count)
print("מספר קבצים:", file_count)



