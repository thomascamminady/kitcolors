import matplotlib.pyplot as plt
from kitcolors import kitcolors

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1, figsize=(20, 15))
    mm = 19
    for i, (name, color) in enumerate(kitcolors.items()):
        ax.text(
            -0.8,
            mm - 2 * i,
            r"{}".format(name),
            horizontalalignment="right",
            fontsize=25,
            verticalalignment="center",
        )
        ax.text(
            8,
            mm - 2 * i,
            r"{}, {}, {}".format(*color.RGB),
            fontsize=25,
            verticalalignment="center",
        )
        ax.text(
            10,
            mm - 2 * i,
            color.hex,
            fontsize=25,
            verticalalignment="center",
        )

        for j, alpha in enumerate(
            [
                1.0,
                0.9,
                0.8,
                0.7,
                0.6,
                0.5,
                0.4,
                0.3,
                0.2,
                0.1,
            ]
        ):
            ax.scatter(
                0.8 * j,
                mm - 2 * i,
                s=6200,
                color=color.rgba(alpha=alpha, transparent=False),
                alpha=alpha,
            )
            if i == 0:
                ax.text(
                    0.8 * j,
                    mm + 2,
                    r"$\alpha={:.1f}$".format(alpha),
                    horizontalalignment="center",
                    fontsize=25,
                    verticalalignment="center",
                    rotation=60,
                    fontweight="bold",
                )
    ax.text(
        8,
        mm + 1.6,
        r"(R, G, B)${}_{256}$",
        fontsize=25,
        verticalalignment="center",
        fontweight="bold",
    )
    ax.text(
        10,
        mm + 1.6,
        r"HEX",
        fontsize=25,
        verticalalignment="center",
        fontweight="bold",
    )
    ax.text(
        -0.8,
        mm + 1.6,
        r"Name",
        fontsize=25,
        verticalalignment="center",
        horizontalalignment="right",
        fontweight="bold",
    )

    ax.set_xlim(-1, 9.6)
    ax.set_ylim(-2, 22)
    plt.tight_layout()
    plt.axis("off")
    plt.savefig("scripts/example.png")
