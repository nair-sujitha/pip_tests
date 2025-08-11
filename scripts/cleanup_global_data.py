# scripts/cleanup_global_data.py
import sys


def main():
    print("[Global Teardown] Cleaning up global test data...")


    print("[Global Teardown] Done.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Global Teardown Error] {e}")
        sys.exit(1)
