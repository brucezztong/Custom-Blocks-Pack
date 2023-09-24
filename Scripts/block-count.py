#!/usr/bin/python3

import subprocess

# Custom Blocks Pack

blockCount = subprocess.check_output( "grep '<block' ~/7dData/Config/blocks.xml | wc -l", shell=True)
blockCount = int(blockCount.decode())
placeholderCount = subprocess.check_output( "grep '<placeholder' ~/7dData/Config/blockplaceholders.xml | wc -l", shell=True)
placeholderCount = int(placeholderCount.decode())
total = blockCount + placeholderCount

print("VANILLA")
print(f"Blocks       : {blockCount}")
print(f"Placeholders : {placeholderCount}")
print(f"TOTAL        : {total}")

# Vanilla

blockCount = subprocess.check_output( "grep '<block' ../Config/blocks.xml | wc -l", shell=True)
blockCount = int(blockCount.decode())
placeholderCount = subprocess.check_output( "grep '<placeholder' ../Config/blockplaceholders.xml | wc -l", shell=True)
placeholderCount = int(placeholderCount.decode())
total = blockCount + placeholderCount

print("\nCUSTOM BLOCKS PACK")
print(f"Blocks       : {blockCount}")
print(f"Placeholders : {placeholderCount}")
print(f"TOTAL        : {total}")

