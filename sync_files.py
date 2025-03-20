import os
import shutil

def sync_public_to_docs_recursive():
    """
    Deletes the entire /docs directory and then recursively copies all
    files and folders from the /public directory to the /docs directory.
    """
    docs_dir = 'docs'
    public_dir = 'public'

    # --- Delete the entire /docs directory recursively ---
    print(f"Deleting the entire directory: {docs_dir}")
    if os.path.exists(docs_dir):
        try:
            shutil.rmtree(docs_dir)
            print(f"Deleted: {docs_dir}")
        except Exception as e:
            print(f"Error deleting {docs_dir}: {e}")
            return

    # --- Copy all files and folders from /public to /docs recursively ---
    print(f"\nCopying all content from: {public_dir} to {docs_dir}")
    if os.path.exists(public_dir):
        try:
            shutil.copytree(public_dir, docs_dir)
            print(f"Copied all content from {public_dir} to {docs_dir}")
        except FileNotFoundError:
            print(f"Error: Directory not found: {public_dir}")
        except Exception as e:
            print(f"Error copying from {public_dir} to {docs_dir}: {e}")
    else:
        print(f"Directory not found: {public_dir}")

if __name__ == "__main__":
    sync_public_to_docs_recursive()