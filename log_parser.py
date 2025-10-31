from pathlib import Path
import re

log_file = Path("/var/log/nginx.log")
pattern = re.compile(r'(GET|PUT|POST|DELETE)\s.*"\s(\d{3})')
methods_found = {}
try:
    with open(log_file) as file_obj:
         for line_number,line in enumerate(file_obj, 1):
             line_result = pattern.findall(line.strip())
             for method, code in line_result:
                 if method not in methods_found:
                      methods_found[method] = {}
                 if code not in methods_found[method]:
                      methods_found[method][code] = 1
                 else:
                      methods_found[method][code] += 1                      
    print(methods_found)
except FileNotFoundError:
     print(f"Error: file {log_file} Not found")
except Exception as e:
     print(f"an Error Occured: {e}")