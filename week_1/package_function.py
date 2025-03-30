import os
import subprocess

# Define base images
BASE_IMAGES = {
    "python": "lambda_python",
    "javascript": "lambda_node"
}

# Function to package a user-defined function
def package_function(lang, function_name):
    # Validate language
    if lang not in BASE_IMAGES:
        print(f"Error: Unsupported language '{lang}'. Choose 'python' or 'javascript'.")
        return
    
    # Define paths
    function_dir = f"functions/{lang}/{function_name}"
    dockerfile_path = f"{function_dir}/Dockerfile"

    # Create function directory if not exists
    os.makedirs(function_dir, exist_ok=True)

    # Generate a function-specific Dockerfile
    with open(dockerfile_path, "w") as dockerfile:
        dockerfile.write(f"""
        FROM {BASE_IMAGES[lang]}
        WORKDIR /app
        COPY {function_name}.{lang if lang == 'python' else 'js'} .
        CMD ["python3", "{function_name}.py"] if lang == "python" else CMD ["node", "{function_name}.js"]
        """)

    # Build the Docker image
    image_name = f"{function_name}_{lang}"
    print(f"📦 Building Docker image: {image_name} ...")
    subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile_path, function_dir])

    print(f"✅ Function '{function_name}' is packaged as {image_name}.")

# Example usage (Replace 'example_function' with actual function name)
package_function("python", "example_function")
package_function("javascript", "example_function")
