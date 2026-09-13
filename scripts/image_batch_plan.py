#!/usr/bin/env python3
"""Create deterministic image-generation batches from a storyboard CSV."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


SHOT_ID_FIELDS = ("shot_id", "shot id", "分镜编号", "镜头编号", "id")


def partition_shot_ids(shot_ids: list[str], size: int = 10) -> list[list[str]]:
    if size < 1:
        raise ValueError("batch size must be at least 1")
    if any(not shot_id.strip() for shot_id in shot_ids):
        raise ValueError("shot IDs must not be blank")
    if len(set(shot_ids)) != len(shot_ids):
        raise ValueError("shot IDs must be unique")
    return [shot_ids[index : index + size] for index in range(0, len(shot_ids), size)]


def load_shot_ids(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("storyboard CSV has no header")
        normalized = {name.strip().lower(): name for name in reader.fieldnames}
        field = next((normalized[name] for name in SHOT_ID_FIELDS if name in normalized), None)
        if field is None:
            raise ValueError("storyboard CSV must contain a shot_id column")
        shot_ids = [row.get(field, "").strip() for row in reader]
    if not shot_ids:
        raise ValueError("storyboard CSV has no shots")
    return shot_ids


def build_plan(shot_ids: list[str], size: int) -> dict:
    batches = partition_shot_ids(shot_ids, size)
    return {
        "total_shots": len(shot_ids),
        "batch_size": size,
        "batches": [
            {"batch_id": f"{index:02d}", "count": len(batch), "shot_ids": batch}
            for index, batch in enumerate(batches, start=1)
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("storyboard_csv", type=Path)
    parser.add_argument("--size", type=int, default=10)
    args = parser.parse_args()
    try:
        plan = build_plan(load_shot_ids(args.storyboard_csv), args.size)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
