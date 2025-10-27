from pathlib import Path
import re

log_file = Path("var/log/nginx.log")
pattern = re.compile(r'(GET|PUT|POST|DELETE)\s.*"\s(\d{3})')
codes_found = {}
try:
    with open(log_file) as file_obj:
         for line_number,line in enumerate(file_obj, 1):
             print(f"Line  {line_number}, {line.strip()}")
except FileNotFoundError:
     print(f"Error: file {log_file} Not found")
except Exception as e:
     print(f"an Error Occured: {e}")