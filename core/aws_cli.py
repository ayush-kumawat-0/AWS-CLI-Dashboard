import subprocess


def run_aws_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return {
            "success": True,
            "output": result.stdout,
            "error": None,
            "returncode": result.returncode #(returncode will tell) This tells us whether the external command succeeded.
        }

    return {
        "success": False,
        "output": result.stdout,
        "error": result.stderr,
        "returncode": result.returncode
    }
