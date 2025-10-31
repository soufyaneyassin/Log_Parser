from pathlib import Path
import re
import csv

#defining files paths
log_file = Path("/var/log/nginx.log")
results_file = Path("logs_results.csv")

#extracting the methods (GET,POST...), codes(404,200,304...) from the log file using regex
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
# after walking through the log file, we will write the results into the csv file
try:
     with open(results_file, mode="w", newline='') as csv_file:
          writer = csv.writer(csv_file)
          writer.writerow(["Method", "Code", "Count"])
          for method, codes in methods_found.items():
              for code, value in methods_found[method].items():
                   writer.writerow([method, code, value])
     print(f"CSV file '{results_file}' created successfully.")
except Exception as e:
      print(f"an Error Occured: {e}")