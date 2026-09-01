import os
import re
import shutil
import urllib.request
import json

# Define the primary categories (including the fallback)
CATEGORIES = [
    "Arrays", "Strings", "Hashing", "Two_Pointers", "Sliding_Window",
    "Binary_Search", "Linked_List", "Stack", "Queue", "Trees", "Heap",
    "Graph", "Greedy", "Backtracking", "Dynamic_Programming", "Uncategorized"
]

# Priority mapping from LeetCode official tags to our folder names.
# The script checks this list in order. The first matching tag wins.
PRIORITY_MAPPING = [
    ("Dynamic Programming", "Dynamic_Programming"),
    ("Backtracking", "Backtracking"),
    ("Graph", "Graph"),
    ("Tree", "Trees"),
    ("Binary Tree", "Trees"),
    ("Binary Search Tree", "Trees"),
    ("Heap (Priority Queue)", "Heap"),
    ("Queue", "Queue"),
    ("Stack", "Stack"),
    ("Linked List", "Linked_List"),
    ("Binary Search", "Binary_Search"),
    ("Sliding Window", "Sliding_Window"),
    ("Two Pointers", "Two_Pointers"),
    ("Greedy", "Greedy"),
    ("Hash Table", "Hashing"),
    ("String", "Strings"),
    ("Array", "Arrays")
]

def get_tags(title_slug):
    """Fetch topic tags for a given problem slug using LeetCode GraphQL API."""
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        topicTags {
          name
        }
      }
    }
    """
    req = urllib.request.Request(
        'https://leetcode.com/graphql/',
        data=json.dumps({'query': query, 'variables': {'titleSlug': title_slug}}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            # Safely navigate the JSON response
            question = data.get('data', {}).get('question')
            if not question:
                return []
            tags = question.get('topicTags', [])
            return [tag['name'] for tag in tags] if tags else []
    except Exception as e:
        print(f"Error fetching tags for {title_slug}: {e}")
        return []

def get_target_category(tags):
    """Determine the primary category based on the priority mapping."""
    for mapping_tag, category in PRIORITY_MAPPING:
        if mapping_tag in tags:
            return category
    return "Uncategorized"

def find_existing_location(folder_name):
    """Check if the problem folder already exists in any of our primary categories."""
    for category in CATEGORIES:
        path = os.path.join(category, folder_name)
        if os.path.isdir(path):
            return path
    return None

def main():
    # Find all folders matching the LeetHub pattern: exactly 4 digits, a dash, and the slug
    pattern = re.compile(r'^\d{4}-.+$')
    
    root_items = os.listdir('.')
    for item in root_items:
        if os.path.isdir(item) and pattern.match(item):
            parts = item.split('-', 1)
            if len(parts) < 2:
                continue
            title_slug = parts[1]
            
            print(f"Processing newly synced problem: {item}")
            
            # 1. Check if it already exists in a category
            existing_path = find_existing_location(item)
            
            if existing_path:
                print(f"  -> Problem already exists at '{existing_path}'. Updating files.")
                target_dir = existing_path
            else:
                # 2. It's a new problem, determine category
                tags = get_tags(title_slug)
                category = get_target_category(tags)
                print(f"  -> Fetched tags: {tags}")
                print(f"  -> Assigned category: {category}")
                
                target_dir = os.path.join(category, item)
                os.makedirs(category, exist_ok=True)
            
            # 3. Move/Overwrite files from item/ to target_dir/
            os.makedirs(target_dir, exist_ok=True)
            for file_name in os.listdir(item):
                src = os.path.join(item, file_name)
                dst = os.path.join(target_dir, file_name)
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.move(src, dst)
                else:
                    shutil.move(src, dst)
            
            # 4. Remove the now-empty root folder
            try:
                os.rmdir(item)
                print(f"  -> Successfully organized into '{target_dir}' and cleaned up root.")
            except Exception as e:
                print(f"  -> Error removing root directory '{item}': {e}")

if __name__ == "__main__":
    main()
