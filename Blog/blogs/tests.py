from django.test import TestCase
import sys
import os

print("当前工作目录:", os.getcwd())
print("\nPython 路径:")
for path in sys.path:
    print(f"  {path}")

print(f"\nblogs 路径是否存在: {os.path.exists('blogs')}")
print(f"blogs/__init__.py 是否存在: {os.path.exists('blogs/__init__.py')}")
