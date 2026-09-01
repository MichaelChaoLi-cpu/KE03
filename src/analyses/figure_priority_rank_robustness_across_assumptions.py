"""Generate the priority-rank robustness across assumptions figure.

Plan: Distinguish frequent scenario eligibility from stable top-priority
placement and show how ranks respond separately to structural scenarios,
population-allocation thresholds, alternative weighting schemes, and
sensitivity-only district vulnerability context.

Framework: AnaSOP Section 6.5 additive, leave-one-out, emphasized, random,
multiplicative, population-allocation, and structural-scenario robustness;
workflow step 9. Rank stability is interpreted jointly with family-specific
eligible denominators and rank intervals.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D


ROOT = Path(__file__).resolve().parents[2]
INPUT = (
    ROOT
    / "data"
    / "processed"
    / "decision"
    / "settlement_priority_robustness_preprocessed.parquet"
)
OUTPUT = (
    ROOT
    / "data"
    / "results"
    / "figures"
    / "Figure_priority_rank_robustness_across_assumptions.png"
)

METRICS = [
    "Intervention Priority",
    "Scenario Inclusion Frequency",
    "Structural-Scenario Top-10 Frequency",
    "Allocation-Threshold Top-10 Frequency",
    "Weight-Rule Top-10 Frequency",
    "Rank Stability",
]


def add_panel_heading(ax: plt.Axes, label: str, subtitle: str) -> None:
    ax.text(
        0.014,
        0.986,
        f"{label}: {subtitle}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontweight="bold",
        color="#20252b",
        bbox={
            "facecolor": "white",
            "edgecolor": "#d2d7dc",
            "linewidth": 0.5,
            "alpha": 0.94,
            "pad": 3.0,
        },
        zorder=50,
    )


def style_frame(ax: plt.Axes) -> None:
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_linewidth(1.25)
        spine.set_edgecolor("#535d66")


def display_name(row: pd.Series) -> str:
    name = str(row["Settlement Name (English Preferred)"])
    if name.startswith("OSM Settlement "):
        name = name.replace("OSM Settlement ", "OSM ")
    return f"{int(row['Priority Rank'])} · {name}"


def select_primary_top_twenty(frame: pd.DataFrame) -> pd.DataFrame:
    selected = (
        frame.loc[frame["Priority Rank"].notna()]
        .nsmallest(20, "Priority Rank")
        .sort_values("Priority Rank")
        .copy()
    )
    if len(selected) != 20:
        raise RuntimeError("Expected 20 primary-ranked settlements for the robustness figure")
    if selected[METRICS].isna().any().any():
        raise RuntimeError("Top-20 robustness metrics are incomplete")
    selected["Sensitivity Display Rank"] = selected["Sensitivity Priority Rank"].astype(float)
    selected["Display Name"] = selected.apply(display_name, axis=1)
    return selected


def plot_frequency_heatmap(ax: plt.Axes, selected: pd.DataFrame) -> None:
    values = selected[METRICS].to_numpy(dtype=float) * 100
    ax.imshow(values, cmap="YlGnBu", vmin=0, vmax=100, aspect="auto", zorder=1)

    for row in range(values.shape[0]):
        for col in range(values.shape[1]):
            value = values[row, col]
            ax.text(
                col,
                row,
                f"{value:.0f}",
                ha="center",
                va="center",
                fontsize=7.1,
                color="white" if value >= 57 else "#25313a",
                fontweight="bold" if row < 10 else "normal",
                zorder=5,
            )

    ax.set_xticks(
        np.arange(len(METRICS)),
        labels=[
            "Primary\npriority",
            "Scenario\ninclusion",
            "Structural\ntop-10",
            "Allocation\ntop-10",
            "Weight-rule\ntop-10",
            "Family-balanced\nstability",
        ],
    )
    ax.set_yticks(np.arange(len(selected)), labels=selected["Display Name"])
    for tick, rank in zip(ax.get_yticklabels(), selected["Priority Rank"], strict=True):
        tick.set_fontsize(7.4)
        if int(rank) <= 10:
            tick.set_fontweight("bold")
    ax.tick_params(axis="x", labelsize=8, length=0, pad=7)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.set_xticks(np.arange(-0.5, len(METRICS), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(selected), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1.1)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.axhline(9.5, color="#26323c", linewidth=1.25, zorder=8)
    ax.set_ylim(len(selected) - 0.5, -1.25)
    ax.set_xlim(-0.5, len(METRICS) - 0.5)
    style_frame(ax)
    add_panel_heading(ax, "a", "Eligibility and family-balanced stability (%)")


def plot_rank_intervals(ax: plt.Axes, selected: pd.DataFrame) -> None:
    y = np.arange(len(selected))

    for idx, row in selected.reset_index(drop=True).iterrows():
        ax.plot(
            [row["Priority Rank P05"], row["Priority Rank P95"]],
            [idx, idx],
            color="#b7bec4",
            linewidth=1.2,
            solid_capstyle="round",
            zorder=2,
        )
        ax.plot(
            [row["Priority Rank IQR Lower"], row["Priority Rank IQR Upper"]],
            [idx, idx],
            color="#3182bd",
            linewidth=4.3,
            solid_capstyle="round",
            zorder=3,
        )

    ax.scatter(
        selected["Median Priority Rank"],
        y,
        marker="o",
        s=22,
        color="#17324d",
        edgecolor="white",
        linewidth=0.35,
        zorder=5,
    )
    ax.scatter(
        selected["Priority Rank"].astype(float),
        y,
        marker="D",
        s=31,
        facecolor="white",
        edgecolor="#111820",
        linewidth=0.9,
        zorder=6,
    )
    ax.scatter(
        selected["Sensitivity Display Rank"],
        y,
        marker="^",
        s=35,
        color="#d95f02",
        edgecolor="white",
        linewidth=0.35,
        zorder=7,
    )

    ax.axvline(10.5, color="#6d757c", linestyle="--", linewidth=0.85, zorder=1)
    ax.text(
        10.9,
        -0.62,
        "Top-10 threshold",
        ha="left",
        va="center",
        fontsize=7,
        color="#59636b",
        zorder=10,
    )
    ax.axhline(9.5, color="#26323c", linewidth=1.25, zorder=8)
    ax.set_ylim(len(selected) - 0.5, -1.25)
    maximum_rank = float(np.ceil(selected["Priority Rank P95"].max() / 10) * 10)
    ax.set_xlim(0, maximum_rank + 2)
    ax.set_xlabel("Priority rank across retained specifications (lower is better)")
    ax.set_yticks(np.arange(len(selected)), labels=[])
    ax.grid(axis="x", color="#d7dde1", linewidth=0.55, alpha=0.78, zorder=0)
    ax.tick_params(axis="x", labelsize=8)
    ax.tick_params(axis="y", length=0)
    style_frame(ax)
    add_panel_heading(ax, "b", "Rank intervals and vulnerability sensitivity")

    ax.legend(
        handles=[
            Line2D([0], [0], color="#b7bec4", lw=1.4, label="P05–P95"),
            Line2D([0], [0], color="#3182bd", lw=4.0, label="IQR"),
            Line2D([0], [0], marker="o", color="none", markerfacecolor="#17324d", markeredgecolor="white", markersize=5.5, label="Median rank"),
            Line2D([0], [0], marker="D", color="none", markerfacecolor="white", markeredgecolor="#111820", markersize=5.5, label="Primary rank"),
            Line2D([0], [0], marker="^", color="none", markerfacecolor="#d95f02", markeredgecolor="white", markersize=6, label="Vulnerability sensitivity rank"),
        ],
        loc="upper right",
        bbox_to_anchor=(0.99, 0.965),
        fontsize=6.8,
        ncol=5,
        borderpad=0.4,
        columnspacing=0.75,
        handlelength=1.6,
    )


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    robustness = pd.read_parquet(INPUT)
    if int((robustness["Robustness Specification Count"] > 0).sum()) != 117:
        raise RuntimeError("Expected 117 settlements eligible in at least one structural scenario")
    primary_family_count = robustness.loc[
        robustness["Included in Priority Ranking"].fillna(False),
        "Robustness Family Count",
    ]
    if not primary_family_count.eq(3).all():
        raise RuntimeError("Every primary-ranked settlement must have three robustness families")
    selected = select_primary_top_twenty(robustness)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.5,
            "legend.frameon": True,
            "legend.framealpha": 0.94,
        }
    )
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(15.8, 9.4),
        constrained_layout=True,
        gridspec_kw={"width_ratios": [1.05, 1.32]},
    )
    ax_a, ax_b = axes
    plot_frequency_heatmap(ax_a, selected)
    plot_rank_intervals(ax_b, selected)

    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight", pad_inches=0.14, facecolor="white")
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
