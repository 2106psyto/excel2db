#!/usr/bin/env python3
"""
Wrapper script to build both the wheel/sdist and standalone executable.
Usage: python build_all.py [--clean]
"""

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n{'='*60}")
    print(f"{description}...")
    print('='*60)
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[FAILED] {description} failed!")
        sys.exit(1)
    print(f"[OK] {description} completed.")


def main():
    parser = argparse.ArgumentParser(description="Build wheel, sdist, and standalone executable")
    parser.add_argument("--clean", action="store_true", help="Clean previous builds")
    args = parser.parse_args()

    print("Building Python package and standalone Windows executable...\n")

    if args.clean:
        print("Cleaning previous builds...")
        import time
        for path in ["dist", "build"]:
            if Path(path).exists():
                try:
                    shutil.rmtree(path)
                except PermissionError:
                    print(f"  Warning: Could not remove {path}. Waiting and retrying...")
                    time.sleep(1)
                    try:
                        shutil.rmtree(path)
                    except:
                        print(f"  Could not remove {path} - it may be in use by another process")
        print("[OK] Cleaned.\n")

    # Step 1: Build wheel and sdist using uv
    run_command("uv build", "Building wheel and source distribution with uv")

    # Step 2: Build standalone executable
    run_command(
        f"{sys.executable} build_exe.py --standalone",
        "Building standalone executable with PyInstaller"
    )

    print("\n" + "="*60)
    print("[OK] All builds completed successfully!")
    print("="*60)
    print("\nGenerated files:")
    print("  dist/excel2sqlite_cli-0.1.0.whl          (Python wheel)")
    print("  dist/excel2sqlite_cli-0.1.0.tar.gz       (Source distribution)")
    print("  dist/excel2sqlite_cli.exe                (Standalone executable)")


if __name__ == "__main__":
    main()
