import os
import subprocess
import shlex

def convert_to_mp3(directory, delete_original=False, recursive=False):
    supported_formats = ('.wav', '.flac', '.m4a')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_formats):
                input_path = os.path.join(root, file)
                output_path = os.path.splitext(input_path)[0] + '.mp3'

                # Convert the file using FFmpeg
                try:
                    command = f'ffmpeg -i "{input_path}" -acodec libmp3lame -b:a 320k "{output_path}"'
                    print(f"Executing command: {command}")

                    result = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, text=True)
                    print(f"Converted: {input_path} to {output_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {input_path}: {e}")
                    print(f"FFmpeg error output: {e.stderr}")
                    continue

                # Delete original if specified
                if delete_original:
                    try:
                        os.remove(input_path)
                        print(f"Deleted original: {input_path}")
                    except Exception as e:
                        print(f"Error deleting {input_path}: {e}")

                print("")

        if not recursive:
            break
