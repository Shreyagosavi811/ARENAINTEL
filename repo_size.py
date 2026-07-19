import os
import pathspec

def get_repo_size(repo_path):
    # Load .gitignore if exists
    gitignore_path = os.path.join(repo_path, ".gitignore")
    ignore_spec = None
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            lines = f.readlines()
            # Explicitly add .git to the ignore patterns
            lines.append(".git/")
            ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, lines)
    else:
        ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, [".git/"])
        
    total_size = 0
    file_count = 0
    
    print(f"{'Size (KB)':<15} | File")
    print("-" * 50)
    
    for root, dirs, files in os.walk(repo_path):
        # Filter directories based on gitignore
        dirs[:] = [d for d in dirs if not ignore_spec.match_file(os.path.relpath(os.path.join(root, d), repo_path))]
        
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, repo_path)
            
            if not ignore_spec.match_file(rel_path):
                size = os.path.getsize(file_path)
                total_size += size
                file_count += 1
                if size > 500 * 1024:  # Print files larger than 500KB
                    print(f"{size / 1024:>10.2f} KB | {rel_path} (LARGE FILE)")
                    
    print("-" * 50)
    print(f"Total Files Analyzed: {file_count}")
    print(f"Total Source Code Size: {total_size / (1024 * 1024):.2f} MB")
    
    if total_size < 10 * 1024 * 1024:
        print("✅ PASSED: Project size is well under the 10 MB limit.")
    else:
        print("❌ FAILED: Project size exceeds 10 MB limit.")

if __name__ == "__main__":
    get_repo_size(os.path.abspath(r"d:\\Antigravity\\stadiumops-ai"))
