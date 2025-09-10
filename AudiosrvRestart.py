import subprocess
import sys

def kill_audio_service():
    try:
        result = subprocess.run(
            ["sc", "queryex", "audiosrv"], capture_output=True, text=True)

        # Check Audiosrv service status
        if result.returncode != 0:
            print("Failed to retrieve service status")
            return

        # Find PID
        for line in result.stdout.splitlines():
            if "PID" in line:
                pid_line = line.strip()
                pid = pid_line.split(":")[1].strip()
                print(f"Audio Service PID: {pid}")
                break
        else:
            print("Audio Service is not running.")
            return

        # Kill
        kill_command = ["taskkill", "/F", "/PID", pid]
        kill_result = subprocess.run(kill_command)

        if kill_result.returncode == 0:
            print("Successfully killed the Windows Audio service")
        else:
            print("Failed to kill the Windows Audio service")
            return

        # Start Windows Audio service again
        start_command = ["net", "start", "audiosrv"]
        start_result = subprocess.run(start_command)

        if start_result.returncode == 0:
            print("Successfully restarted the Windows Audio service")
        else:
            print("Failed to restart the Windows Audio service")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    kill_audio_service()