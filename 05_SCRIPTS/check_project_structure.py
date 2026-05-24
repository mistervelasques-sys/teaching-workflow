from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "00_brief.md",
    "01_sources_consultees.md",
    "02_design_brief.md",
    "03_sequence.md",
    "90_audit.md",
    "91_revision_plan.md",
]

REQUIRED_DIRS = [
    "04_lessons",
    "05_worksheets",
    "06_assessment",
    "07_slides",
    "exports",
]


def format_items(items: list[str]) -> str:
    return ", ".join(items) if items else "None"


def check_project(project_dir: Path) -> str:
    present_files = [name for name in REQUIRED_FILES if (project_dir / name).is_file()]
    missing_files = [name for name in REQUIRED_FILES if name not in present_files]
    present_dirs = [name + "/" for name in REQUIRED_DIRS if (project_dir / name).is_dir()]
    missing_dirs = [name + "/" for name in REQUIRED_DIRS if name + "/" not in present_dirs]
    status = "OK" if not missing_files and not missing_dirs else "INCOMPLETE"

    lines = [
        f"Project: {project_dir.name}",
        f"Files present: {format_items(present_files)}",
        f"Files missing: {format_items(missing_files)}",
        f"Directories present: {format_items(present_dirs)}",
        f"Directories missing: {format_items(missing_dirs)}",
        f"Global status: {status}",
    ]
    return "\n".join(lines)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    projects_root = repo_root / "03_PROJECTS"

    if not projects_root.is_dir():
        print(f"Projects root not found: {projects_root}")
        return 1

    project_dirs = sorted(path for path in projects_root.iterdir() if path.is_dir())
    if not project_dirs:
        print(f"No project directories found in: {projects_root}")
        return 0

    reports = [check_project(project_dir) for project_dir in project_dirs]
    print("\n\n".join(reports))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
