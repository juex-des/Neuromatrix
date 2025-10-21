import time, os, json

def errorHandling(e):
  print("Logging error...")
  with open('errorReports.txt', 'a+') as f:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}] Error: {e}\n")
  print("Error reported.")
  time.sleep(2)

def load_file(file_path):
  if os.path.exists(file_path):
    try:
      with open(file_path, 'r') as file:
        return json.load(file)
    except Exception as e:
      print(f"\033[31mError: Could not read file {file_path}.\033[0m")
      errorHandling(e)
      return {}
  else:
    return {}
  
def save_file(file_path, data):
  try:
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=2)
  except Exception as e:
    print(f"\033[31mError: Could not save file {file_path}.\033[0m")
    errorHandling(e)
