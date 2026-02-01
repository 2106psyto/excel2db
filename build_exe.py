#!/usr/bin/env python3
"""
Build script to create a standalone Windows executable using PyInstaller.
Usage: python build_exe.py [--clean]

Can also be called as a post-build hook by the build system.
"""

import argparse
import subprocess
import sys
import shutil
from pathlib import Path


def clean_builds():
    """Remove previous build artifacts."""
    print("Cleaning previous builds...")
    import time
    for path in ["dist", "build"]:
        if Path(path).exists():
            try:
                shutil.rmtree(path)
            except PermissionError:
                print(f"  Warning: Could not remove {path} (file may be in use). Retrying...")
                time.sleep(1)
                shutil.rmtree(path)
    for spec in Path(".").glob("*.spec"):
        try:
            spec.unlink()
        except PermissionError:
            pass
    print("[OK] Cleaned.")


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n{description}...")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[FAILED] {description} failed!")
        sys.exit(1)
    print(f"[OK] {description} completed.")


def build_executable():
    """Build the standalone executable."""
    print("\nBuilding executable...")
    
    # Use a temporary dist directory to avoid file locking issues
    import uuid
    import os
    temp_dist = f"dist_build_{str(uuid.uuid4())[:8]}"
    
    cmd = (
        f"{sys.executable} -m PyInstaller "
        '--name="excel2sqlite_cli" '
        "--onefile "
        "--console "
        "--specpath=build "
        f"--distpath={temp_dist} "
        "-p src "
        "src/excel2sqlite_cli/main.py"
    )

    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("[FAILED] Build failed!")
        sys.exit(1)

    # Move exe to final location with proper error handling
    import time
    Path("dist").mkdir(exist_ok=True)
    exe_src = Path(temp_dist) / "excel2sqlite_cli.exe"
    exe_dst = Path("dist") / "excel2sqlite_cli.exe"
    
    if exe_src.exists():
        # Try to remove old exe if it exists (might be locked)
        if exe_dst.exists():
            try:
                exe_dst.unlink()
            except PermissionError:
                # File is locked, try to replace it anyway
                print("  Warning: Old exe file is locked. Attempting copy over...")
                time.sleep(0.5)
        
        # Try to move, with fallback to copy
        try:
            shutil.move(str(exe_src), str(exe_dst))
        except (PermissionError, OSError) as e:
            print(f"  Warning: Could not move exe ({e}). Trying copy...")
            shutil.copy2(str(exe_src), str(exe_dst))
        
        # Clean up temp directory
        shutil.rmtree(temp_dist, ignore_errors=True)

    print("\n" + "="*60)
    print("[OK] Build successful!")
    print(f"Executable: dist/excel2sqlite_cli.exe")
    print("="*60)
    print("\nUsage example:")
    print("  .\\dist\\excel2sqlite_cli.exe --config config.yaml --excel data.xlsx --output database.db")


def main():
    parser = argparse.ArgumentParser(description="Build standalone executable")
    parser.add_argument("--clean", action="store_true", help="Clean previous builds")
    parser.add_argument("--standalone", action="store_true", help="Build standalone executable only")
    args = parser.parse_args()

    if args.clean:
        clean_builds()

    print("Building standalone Windows executable for excel2sqlite_cli...\n")

    # Install PyInstaller
    run_command(
        f"{sys.executable} -m pip install -q pyinstaller",
        "Installing PyInstaller"
    )

    # Only install the project in dev mode if building standalone
    if args.standalone or not any(Path("dist").glob("excel2sqlite_cli-*.whl")):
        run_command(
            f"{sys.executable} -m pip install -e .",
            "Installing project in development mode"
        )

    build_executable()


if __name__ == "__main__":
    main()
