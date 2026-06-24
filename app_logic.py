import os
import re

def update_suffix(folder,old_suffix,new_suffix,case_sensitive,include_subfolders,execute=False):
    results=[]
    
 # FR-P-09: Traverse subdirectories recursively using os.walk
    if include_subfolders:
        for root, _, files in os.walk(folder):
            for file in files:
                old_path = os.path.join(root, file)
                _process_file(
                    old_path,
                    old_suffix,
                    new_suffix,
                    case_sensitive,
                    results,
           
                    execute
                )
    
    # FR-P-10: Process only top-level files when disabled
    else:
        for file in os.listdir(folder):
            old_path = os.path.join(folder, file)
            if os.path.isfile(old_path):
                _process_file(
                    old_path,
                    old_suffix,
                    new_suffix,
                    case_sensitive,
                    results,
                    execute
                )
    return results

def _process_file(old_path, old_suffix, new_suffix, case_sensitive, results, execute):
    # FR-S-05: Separate filename into base and extension
    folder, filename = os.path.split(old_path)
    name, ext = os.path.splitext(filename)



    #FR-S-06:APPLY SUFFIX ONLY ON BASE NAME
    if case_sensitive:
           # FR-S-08: Case-sensitive suffix match
        suffix_match = name.endswith(old_suffix)
    else:
              # FR-S-09: Case-insensitive suffix match
          suffix_match = name.lower().endswith(old_suffix.lower())
    if not suffix_match:
        return
        #FRS-09:Remove the old suffix and replacing with new suffix
    base_name= name [:-len(old_suffix)] if suffix_match else name
    new_name = base_name + new_suffix + ext



    new_path = os.path.join(folder, new_name)

    if execute:
        try:
            # FR-P-15: Rename file using os.rename
            os.rename(old_path, new_path)
            results.append((old_path, new_path, True, None))
        except OSError as e:
            results.append((old_path, new_path, False, str(e)))
    else:
        results.append((old_path, new_path, True, None))
