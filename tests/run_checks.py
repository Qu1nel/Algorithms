"""Run Python and C algorithm checks from a fresh checkout."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALGORITHMS = ROOT / "algorithms"
CFLAGS = ("-std=c17", "-Wall", "-Wextra", "-Werror", "-Wpedantic", "-Wconversion", "-Wshadow", "-Wstrict-prototypes", "-O2")


def run_checks() -> None:
    for tests in sorted(ALGORITHMS.glob("*/*/python/test_*.py")):
        print(f"Python: {tests.parents[1].name}", flush=True)
        subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(tests.parent), "-p", tests.name],
            cwd=ROOT,
            check=True,
        )

    compiler = os.environ.get("CC", "gcc")
    with tempfile.TemporaryDirectory(prefix="algorithms-tests-") as build_dir:
        for tests in sorted(ALGORITHMS.glob("*/*/c/tests/test_*.c")):
            c_dir = tests.parents[1]
            print(f"C: {c_dir.parent.name}", flush=True)
            executable = Path(build_dir) / f"{tests.stem}.exe"
            sources = sorted((c_dir / "src").glob("*.c"))
            subprocess.run(
                [compiler, *CFLAGS, "-I", str(c_dir / "include"), *map(str, sources), str(tests), "-o", str(executable)],
                cwd=ROOT,
                check=True,
            )
            subprocess.run([executable], cwd=ROOT, check=True)


if __name__ == "__main__":
    run_checks()
