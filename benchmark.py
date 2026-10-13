"""Benchmark with synthetic strings only. Never use real passwords."""
import csv, timeit
from pathlib import Path
from password_analyzer.app import analyze_password
LENGTHS = [8,16,32,64,128,256,512,1024]
REPEATS = 1000
def main():
    rows=[]
    for n in LENGTHS:
        sample=("aA7!"*((n+3)//4))[:n]
        elapsed=timeit.timeit(lambda: analyze_password(sample),number=REPEATS)
        per_run=elapsed*1_000_000/REPEATS
        rows.append({"input_length":n,"runs":REPEATS,"total_seconds":round(elapsed,6),
                     "microseconds_per_run":round(per_run,3)})
        print(f"n={n:4} | {per_run:9.3f} microseconds/run")
    with Path("benchmark_results.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print("Saved benchmark_results.csv. Times vary by device and system load.")
if __name__=="__main__": main()
