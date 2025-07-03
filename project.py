#!/usr/bin/env python3
#NET=~/jetson-inference/python/training/detection/ssd
#detectnet --model=$NET/models/friends/ssd-mobilenet.onnx --labels=$NET/models/friends/labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes /dev/video0 webrtc://@:8554/output



import subprocess
import os
import argparse

def run_jetson_detection():
    parser = argparse.ArgumentParser(description="Run Jetson Inference detectnet.")
    parser.add_argument("--model", type=str, default="~/final_project/models/friends/ssd-mobilenet.onnx")
    parser.add_argument("--labels", type=str, default="~/final_project/models/friends/labels.txt")
    parser.add_argument("--input-blob", type=str, default="input_0")
    parser.add_argument("--output-cvg", type=str, default="scores")
    parser.add_argument("--output-bbox", type=str, default="boxes")
    parser.add_argument("--input", type=str, default="/dev/video0")
    parser.add_argument("--output", type=str, default="webrtc://@:8554/output")
    opt = parser.parse_args()

    model_path = os.path.expanduser(opt.model)
    labels_path = os.path.expanduser(opt.labels)

    detectnet_command = [
        "detectnet",
        f"--model={model_path}",
        f"--labels={labels_path}",
        f"--input-blob={opt.input_blob}",
        f"--output-cvg={opt.output_cvg}",
        f"--output-bbox={opt.output_bbox}",
        opt.input,
        opt.output
    ]

    print("Now running") # Added print statement here

    try:
        subprocess.run(
            detectnet_command,
            check=True,
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print(f"Error: 'detectnet' command not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Return Code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_jetson_detection()
