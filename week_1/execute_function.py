import subprocess
import sys
import time

def execute_function(function_name, lang, timeout=5):  
    """Runs a function inside a Docker container with a timeout."""
    
    image_name = f"example_function_{lang}"  # Selects the correct image
    print(f"🚀 Running {function_name} in {lang} with a timeout of {timeout} seconds...")

    try:
        # Start the container
        process = subprocess.Popen(
            ["docker", "run", "--rm", image_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait for execution with timeout
        try:
            output, error = process.communicate(timeout=timeout)
            if output:
                print(f"✅ Output: {output.decode().strip()}")
            if error:
                print(f"⚠️ Error: {error.decode().strip()}")
        except subprocess.TimeoutExpired:
            print(f"⏳ Timeout exceeded! Stopping {function_name}...")
            process.terminate()  # Graceful stop
            time.sleep(1)  # Give time to terminate
            process.kill()  # Force kill if still running
            print(f"❌ Function {function_name} exceeded {timeout} seconds and was terminated.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python execute_function.py <function_name> <language> [timeout]")
        sys.exit(1)

    function_name = sys.argv[1]
    lang = sys.argv[2]
    timeout = int(sys.argv[3]) if len(sys.argv) > 3 else 5  # Default timeout: 5 seconds

    execute_function(function_name, lang, timeout)
