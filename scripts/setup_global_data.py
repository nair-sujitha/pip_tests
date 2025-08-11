# scripts/setup_global_data.py
import sys


def main():
    print("[Global Setup] Preparing global test data...")

    print("[Global Setup] Done.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Global Setup Error] {e}")
        sys.exit(1)
