import numpy as np
from pathlib import Path

out_dir = Path("output")

out_dir.mkdir(exist_ok=True)


def main():
    build_dir = out_dir / "_build"
    build_dir.mkdir(exist_ok=True)
    outf = build_dir / "res.txt"
    if outf.is_file():
        x = np.loadtxt(outf)
        print("A loaded x:\n", x)

    x = np.random.rand(4, 4)
    print("A new x to file:\n", x)
    np.savetxt(outf, x)


if __name__ == "__main__":
    main()
