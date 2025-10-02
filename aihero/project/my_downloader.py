import io
import zipfile
import requests
import frontmatter

# --- Paste the same read_repo_data function here ---
def read_repo_data(repo_owner, repo_name):
    """
    Download and parse all markdown files from a GitHub repository.
    
    Args:
        repo_owner: GitHub username or organization
        repo_name: Repository name
    
    Returns:
        List of dictionaries containing file content and metadata
    """
    prefix = 'https://codeload.github.com'
    url = f'{prefix}/{repo_owner}/{repo_name}/zip/refs/heads/master'
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise Exception(f"Failed to download repository: {resp.status_code}")

    repository_data = []
    zf = zipfile.ZipFile(io.BytesIO(resp.content))
    
    for file_info in zf.infolist():
        filename = file_info.filename
        filename_lower = filename.lower()

        if not (filename_lower.endswith('.md') or filename_lower.endswith('.mdx')):
            continue
    
        try:
            with zf.open(file_info) as f_in:
                content = f_in.read().decode('utf-8', errors='ignore')
                post = frontmatter.loads(content)
                data = post.to_dict()
                data['filename'] = filename
                repository_data.append(data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    zf.close()
    return repository_data

# --- Call the function for your chosen repository ---
print("Downloading and processing FastAPI documentation...")

# Note: The FastAPI repo is large, so this might take a moment!
fastapi_docs = read_repo_data('tiangolo', 'fastapi')

print(f"Found {len(fastapi_docs)} markdown documents in the FastAPI repository.")

if fastapi_docs:
    print("\n--- Example FastAPI Document ---")
    # Print the first document found
    print(fastapi_docs[0])