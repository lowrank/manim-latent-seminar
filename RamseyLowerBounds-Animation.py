"""
An Exponential Improvement for Ramsey Lower Bounds
Jie Ma, Wujie Shen, and Shengjie Xie (2025)

The first exponential improvement over Erdos's 1947 lower bound on Ramsey numbers,
using random sphere graphs and geometric dependencies.

arXiv:2507.12926v1
"""

from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService
from latent_utils import (
    LatentPrelude,
    make_content_group,
    make_theorem_card,
    center_mathtex,
    clear_screen,
    SEMINAR_BLUE,
)
import numpy as np


# ═══════════════════════════════════════════════════════════════════════════
# Main Scene
# ═══════════════════════════════════════════════════════════════════════════

class RamseyLowerBoundsScene(LatentPrelude, VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))
        self.play_prelude()

        # ═══════════════════════════════════════════════════════════════════
        # Scene 1: Title Card
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{An Exponential Improvement}",
            font_size=44,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        subtitle = Tex(
            r"\textbf{for Ramsey Lower Bounds}",
            font_size=40,
            color=BLUE,
        )
        subtitle.next_to(title, DOWN, buff=0.25)

        authors = Tex(
            r"Jie Ma \quad Wujie Shen \quad Shengjie Xie",
            font_size=30,
            color=GREY_B,
        )

        affiliations = Tex(
            r"USTC \& Tsinghua University",
            font_size=26,
            color=GREY_B,
        )

        journal = Tex(
            r"\textit{arXiv:2507.12926}, July 2025",
            font_size=28,
            color=GOLD,
        )

        tagline = Tex(
            r"The First Exponential Improvement in 78 Years",
            font_size=32,
            color=TEAL,
        )

        authors.next_to(subtitle, DOWN, buff=0.6)
        affiliations.next_to(authors, DOWN, buff=0.2)
        journal.next_to(affiliations, DOWN, buff=0.4)
        tagline.next_to(journal, DOWN, buff=0.5)

        with self.voiceover(
            text="An exponential improvement for Ramsey lower bounds. "
                 "By Jay Ma, Wu-Jay Shen, and Sheng-Jay Shay."
        ):
            self.play(Write(title))
            self.wait(1)
            self.play(Write(subtitle))
            self.wait(1.5)
            self.play(FadeIn(authors))
            self.wait(1)
            self.play(FadeIn(affiliations))
        self.wait(0.8)


        with self.voiceover(
            text="This paper, posted in July twenty twenty-five, provides the first exponential improvement "
                 "over Erdos's lower bound on Ramsey numbers in ninteen forty-seven. "
                 "A 78-year-old barrier, broken."
        ):
            self.play(FadeIn(journal))
            self.wait(1.5)
            self.play(FadeIn(tagline))
            self.wait(2)
            self.play(Indicate(tagline, color=TEAL))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 1b: Preliminaries — Complete Graphs
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Preliminaries: Complete Graphs}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        defn = Tex(
            r"A \textbf{complete graph} $K_n$ has $n$ vertices, "
            r"with an edge between every pair of vertices.",
            font_size=28,
        )

        example_label = Tex(
            r"$K_4$: 4 vertices, 6 edges",
            font_size=26,
            color=GREY_B,
        )

        # Draw K4 on the left
        k4_radius = 1.0
        k4_center = LEFT * 3 + DOWN * 0.8
        k4_verts = []
        k4_dots = VGroup()
        for i in range(4):
            angle = PI / 2 + i * TAU / 4
            pos = k4_center + k4_radius * np.array([np.cos(angle), np.sin(angle), 0])
            k4_verts.append(pos)
            k4_dots.add(Dot(pos, radius=0.08, color=WHITE))

        k4_edges = VGroup()
        for i in range(4):
            for j in range(i + 1, 4):
                k4_edges.add(Line(k4_verts[i], k4_verts[j], stroke_width=2, color=GREY_B))

        k4_label = Tex(r"$K_4$", font_size=30, color=TEAL).next_to(
            VGroup(k4_dots), DOWN, buff=0.4
        )

        # Draw K5 on the right
        k5_radius = 1.2
        k5_center = RIGHT * 3 + DOWN * 0.8
        k5_verts = []
        k5_dots = VGroup()
        for i in range(5):
            angle = PI / 2 + i * TAU / 5
            pos = k5_center + k5_radius * np.array([np.cos(angle), np.sin(angle), 0])
            k5_verts.append(pos)
            k5_dots.add(Dot(pos, radius=0.08, color=WHITE))

        k5_edges = VGroup()
        for i in range(5):
            for j in range(i + 1, 5):
                k5_edges.add(Line(k5_verts[i], k5_verts[j], stroke_width=2, color=GREY_B))

        k5_label = Tex(r"$K_5$", font_size=30, color=TEAL).next_to(
            VGroup(k5_dots), DOWN, buff=0.4
        )

        # Clique definition
        clique_def = Tex(
            r"A \textbf{clique} is a subset of vertices that form a complete subgraph.",
            font_size=28,
            color=TEAL,
        )

        defn.next_to(title, DOWN, buff=0.6)
        example_label.next_to(defn, DOWN, buff=0.4)

        clique_def.next_to(VGroup(k4_label, k5_label), DOWN, buff=0.6)

        with self.voiceover(
            text="Before diving in, let's review some basic definitions. "
                 "A complete graph K n has n vertices, "
                 "with an edge connecting every pair."
        ):
            self.play(FadeIn(defn))
        self.wait(1)


        with self.voiceover(
            text="Here is K 4, the complete graph on 4 vertices. "
                 "It has 6 edges. "
                 "And here is K 5, with 5 vertices and 10 edges."
        ):
            self.play(FadeIn(k4_dots), Create(k4_edges), FadeIn(k4_label))
            self.wait(2)
            self.play(FadeIn(k5_dots), Create(k5_edges), FadeIn(k5_label))
        self.wait(0.8)


        with self.voiceover(
            text="A clique is a subset of vertices that form a complete subgraph. "
                 "For example, any three mutually connected vertices in K 5 "
                 "form a triangle, which is a clique of size 3."
        ):
            self.play(FadeIn(clique_def))
            self.wait(1)
            # Highlight a triangle in K5
            tri = Polygon(
                k5_verts[0], k5_verts[1], k5_verts[2],
                stroke_color=YELLOW,
                stroke_width=3,
                fill_opacity=0.12,
                fill_color=YELLOW,
            )
            self.play(Create(tri))
        self.wait(3)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 2: What Are Ramsey Numbers?
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{What Are Ramsey Numbers?}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        setup = Tex(
            r"Color every edge of the complete graph $K_n$ either "
            r"red or blue.",
            font_size=28,
        )

        question = Tex(
            r"\textbf{Question:} How large must $n$ be to guarantee a \\",
            r"monochromatic complete subgraph?",
            font_size=28,
            color=TEAL,
            tex_environment="flushleft",
        )

        definition = Tex(
            r"$\bullet$ $r(\ell, k)$ = smallest $n$ such that \textit{every} red-blue coloring of $K_n$ \\",
            r"contains a red $K_\ell$ or a blue $K_k$.",
            font_size=28,
            tex_environment="flushleft",
        )

        example = Tex(
            r"\textbf{Example:} $r(3,3) = 6$ --- among any 6 people, \\",
            r"3 are mutual friends or 3 are mutual strangers.",
            font_size=28,
            color=YELLOW,
            tex_environment="flushleft",
        )

        content = make_content_group(
            setup, question, definition, example,
            reference=title,
            buff_between=0.4,
            buff_below=0.5,
        )

        with self.voiceover(
            text="Now, onto Ramsey numbers. "
                 "Take the complete graph on n vertices. "
                 "Color every edge either red or blue."
        ):
            self.play(FadeIn(setup))
        self.wait(1)


        with self.voiceover(
            text="The Ramsey number, r of l and k, is the smallest n such that "
                 "every red-blue coloring of K n must contain "
                 "either a red complete subgraph on l vertices, "
                 "or a blue complete subgraph on k vertices."
        ):
            self.play(FadeIn(question))
            self.wait(1.5)
            self.play(FadeIn(definition))
        self.wait(1)


        with self.voiceover(
            text="A classic example: r of three and three equals 6. "
                 "Among any 6 people, you can always find "
                 "3 mutual friends or 3 mutual strangers."
        ):
            self.play(FadeIn(example))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ─────────────────────────────────────────────────────────────────
        # Scene 2b: Small Ramsey Example (K6 Diagram)
        # ─────────────────────────────────────────────────────────────────

        title = Tex(
            r"\textbf{A Taste of Ramsey Theory}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # Draw K6 vertices and uncolored edges
        n_verts = 6
        radius = 1.8
        graph_center = DOWN * 0.3
        verts = []
        dots = VGroup()
        labels = VGroup()
        for i in range(n_verts):
            angle = PI / 2 + i * TAU / n_verts
            pos = graph_center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            verts.append(pos)
            dot = Dot(pos, radius=0.09, color=WHITE)
            direction = pos - graph_center
            direction = direction / np.linalg.norm(direction)
            label = Tex(str(i + 1), font_size=24).next_to(
                pos, direction, buff=0.2
            )
            dots.add(dot)
            labels.add(label)

        # Build edge list and create uncolored lines
        edge_list = []
        edge_lines = VGroup()
        for i in range(n_verts):
            for j in range(i + 1, n_verts):
                edge_list.append((i, j))
                line = Line(verts[i], verts[j], stroke_width=1.8, color=GREY)
                edge_lines.add(line)

        note = Tex(
            r"In $K_6$: every 2-coloring contains a monochromatic triangle.",
            font_size=26,
            color=GREY_B,
        )
        note.next_to(dots, DOWN, buff=0.8)

        with self.voiceover(
            text="Here is K 6, the complete graph on 6 vertices, "
                 "with 15 edges."
        ):
            self.play(FadeIn(dots), FadeIn(labels))
            self.wait(1)
            self.play(Create(edge_lines), run_time=2)
        self.wait(0.8)


        # Helper: find a monochromatic triangle in a coloring
        def find_mono_triangle(coloring):
            """coloring: dict (i,j) -> 'red' or 'blue'. Returns (a,b,c, color)."""
            for a in range(n_verts):
                for b in range(a + 1, n_verts):
                    for c_idx in range(b + 1, n_verts):
                        if coloring[(a, b)] == coloring[(a, c_idx)] == coloring[(b, c_idx)]:
                            return (a, b, c_idx, coloring[(a, b)])
            return None

        def random_coloring(seed):
            rng = np.random.RandomState(seed)
            col = {}
            while True:
                col = {}
                for e in edge_list:
                    col[e] = 'red' if rng.rand() < 0.5 else 'blue'
                tri = find_mono_triangle(col)
                if tri is not None:
                    return col, tri

        def recolor_edges(coloring):
            anims = []
            for k_idx, e in enumerate(edge_list):
                target_color = RED if coloring[e] == 'red' else BLUE_D
                anims.append(edge_lines[k_idx].animate.set_color(target_color))
            self.play(*anims, run_time=1)

        def make_triangle(tri):
            a, b, c_v, mono_color = tri
            col = RED if mono_color == 'red' else BLUE
            return Polygon(
                verts[a], verts[b], verts[c_v],
                stroke_color=col, stroke_width=4,
                fill_opacity=0.15, fill_color=col,
            )

        # ── Trial 1 (seed=1 → red triangle on vertices 1,2,4) ──
        col1, tri1 = random_coloring(1)

        with self.voiceover(
            text="No matter how you color the edges, "
                 "a monochromatic triangle always appears. "
        ):
            pass

        with self.voiceover(
            text= "Let's try a random coloring."
        ):
            recolor_edges(col1)
        self.wait(0.8)


        tri_highlight_1 = make_triangle(tri1)
        with self.voiceover(
            text="There it is. Vertices 1, 2, and 4 form a red triangle."
        ):
            self.play(Create(tri_highlight_1))
        self.wait(0.8)


        # ── Trial 2 (seed=0 → blue triangle on vertices 1,2,3) ──
        col2, tri2 = random_coloring(0)

        with self.voiceover(
            text="Let's shuffle the colors and try again."
        ):
            self.play(FadeOut(tri_highlight_1))
            recolor_edges(col2)
        self.wait(0.8)


        tri_highlight_2 = make_triangle(tri2)
        with self.voiceover(
            text="Vertices 1, 2, and 3 now form a blue triangle."
        ):
            self.play(Create(tri_highlight_2))
        self.wait(0.8)


        # ── Trial 3 (seed=5 → red triangle on vertices 1,2,6) ──
        col3, tri3 = random_coloring(5)

        with self.voiceover(
            text="One more random coloring."
        ):
            self.play(FadeOut(tri_highlight_2))
            recolor_edges(col3)
        self.wait(0.8)


        tri_highlight_3 = make_triangle(tri3)
        with self.voiceover(
            text="Vertices 1, 2, and 6, a red triangle again."
        ):
            self.play(Create(tri_highlight_3))
        self.wait(0.8)


        # ── Conclusion ──
        with self.voiceover(
            text="Every coloring we try, a monochromatic triangle appears. "
                 "This is guaranteed by Ramsey's theorem. "
        ):
            self.play(FadeIn(note))
            self.wait(1)
            self.play(Indicate(tri_highlight_3, color=YELLOW))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 3: The Upper and Lower Bound History
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{History: Upper and Lower Bounds}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        upper_header = Tex(
            r"\textbf{Upper Bounds} (how big $r(\ell,k)$ can be):",
            font_size=28,
            color=TEAL,
        )

        upper1 = Tex(
            r"$\bullet$ \textbf{1935} Erd\H{o}s--Szekeres: "
            r"$r(\ell, k) \le \binom{k+\ell-2}{\ell-1}$, "
            r"giving $r(\ell,\ell) \le 4^\ell$",
            font_size=26,
        )

        upper2 = Tex(
            r"$\bullet$ \textbf{2023} Campos--Griffiths--Morris--Sahasrabudhe: "
            r"$r(\ell,\ell) \le (4 - \varepsilon)^\ell$ \;\; (Breakthrough!)",
            font_size=26,
        )

        content = make_content_group(
            upper_header, upper1, upper2,
            reference=title,
            buff_between=0.35,
            buff_below=0.5,
        )

        with self.voiceover(
            text="Let's set the historical stage. "
                 "On the upper bound side, Erdos and Szekeres showed in nineteen thirty-five that "
                 "r of l and l is at most 4 to the l."
        ):
            self.play(FadeIn(upper_header))
            self.wait(1.5)
            self.play(FadeIn(upper1))
        self.wait(1)


        with self.voiceover(
            text="In twenty twenty-three, Campos, Griffiths, Morris, and Sahasrabudhe achieved a landmark breakthrough: "
                 "the first exponential improvement on the upper bound."
        ):
            self.play(FadeIn(upper2))
            self.wait(1.5)
            self.play(Indicate(upper2, color=GREEN))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ─────────────────────────────────────────────────────────────────
        # Scene 3b: Lower Bound History
        # ─────────────────────────────────────────────────────────────────

        title = Tex(
            r"\textbf{Lower Bounds: The 78-Year Gap}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        lower_header = Tex(
            r"\textbf{Lower Bounds} (showing $r(\ell,k)$ must be large):",
            font_size=28,
            color=TEAL,
        )

        lower1 = Tex(
            r"$\bullet$ \textbf{1947} Erd\H{o}s: "
            r"Color edges of $K_n$ randomly with probability $p$. \\",
            r"$\phantom{\bullet}$\; First moment method $\Rightarrow$ "
            r"$r(\ell, C\ell) \ge \Omega\!\bigl(\ell \cdot M_C^\ell\bigr)$ "
            r"where $M_C = p_C^{-1/2}$",
            font_size=26,
            tex_environment="flushleft",
        )

        asymptotic_note = Tex(
            r"$\phantom{\bullet}$\; Here $C > 1$ is a fixed constant and $\ell \to \infty$; "
            r"$p_C \in (0, \tfrac{1}{2})$ is a constant depending on $C$.",
            font_size=24,
            color=GREY_B,
        ).shift(RIGHT * 0.2)

        lower2 = Tex(
            r"$\bullet$ \textbf{1975} Spencer: Lov\'asz Local Lemma $\Rightarrow$ "
            r"constant-factor improvement only",
            font_size=26,
        )

        gap = Tex(
            r"\textbf{For 78 years: no exponential improvement on the lower bound!}",
            font_size=28,
            color=RED,
        )

        content = make_content_group(
            lower_header, lower1, asymptotic_note, lower2, gap,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Now the lower bound side. In nineteen forty-seven, Erdos invented the probabilistic method. "
                 "Color each edge of K n red with probability p, blue otherwise. "
                 "A simple first moment argument gives "
                 "r of l and C l is at least on the order of l times M C to the l, "
                 "where M C equals p C to the minus one half."
        ):
            self.play(FadeIn(lower_header))
            self.wait(1.5)
            self.play(FadeIn(lower1))
        self.wait(1)


        with self.voiceover(
            text="Here, C is a fixed constant greater than 1, "
                 "and l goes to infinity. This is an asymptotic result. "
                 "The quantity p C is a constant that depends only on C. "
                 "We will see its precise definition shortly."
        ):
            self.play(FadeIn(asymptotic_note))
        self.wait(1)


        with self.voiceover(
            text="In nineteen seventy-five, Spencer used the Lovasz Local Lemma to improve Erdos's bound, "
                 "but only by a constant factor. "
                 "For 78 years, no one could find an exponential improvement on the lower bound."
        ):
            self.play(FadeIn(lower2))
            self.wait(2)
            self.play(FadeIn(gap))
            self.wait(1.5)
            self.play(Indicate(gap, color=RED))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 4: Erdos's Probabilistic Method
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Erd\H{o}s's Probabilistic Method (1947)}",
            font_size=40,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        step1 = Tex(
            r"$\bullet$ Color each edge of $K_n$ red with probability $p$, "
            r"blue with probability $1-p$.",
            font_size=28,
        )

        step2_label = Tex(
            r"$\bullet$ Compute probabilities of monochromatic cliques:",
            font_size=28,
        )

        step2_eq = MathTex(
            r"\Pr[\text{red } K_\ell] = p^{\binom{\ell}{2}}, \qquad "
            r"\Pr[\text{blue } K_k] = (1-p)^{\binom{k}{2}}",
            font_size=32,
            color=TEAL,
        )

        step3 = Tex(
            r"$\bullet$ \textbf{Union bound:} if $\binom{n}{\ell} p^{\binom{\ell}{2}} "
            r"+ \binom{n}{k} (1-p)^{\binom{k}{2}} < 1$, a good coloring exists $\Rightarrow$ $r(\ell, k) > n$.",
            font_size=28,
            tex_environment="flushleft",
        )

        key_word = Tex(
            r"\textbf{Key assumption:} edges are colored \textit{independently}.",
            font_size=28,
            color=YELLOW,
        )

        content = make_content_group(
            step1, step2_label, step2_eq, step3, key_word,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Here is Erdos's argument. Color each edge independently: "
                 "red with probability p, blue with probability 1 minus p."
        ):
            self.play(FadeIn(step1))
        self.wait(1)


        with self.voiceover(
            text="Because edges are independent, the probability that l specific vertices "
                 "form a red clique is p to the l choose 2. "
                 "Similarly for blue cliques."
        ):
            self.play(FadeIn(step2_label))
            self.wait(1)
            self.play(Write(step2_eq))
        self.wait(1)


        with self.voiceover(
            text="By the union bound, if the expected number of monochromatic cliques "
                 "is less than 1, then a good coloring exists. "
                 "This gives us Erdos's lower bound on the Ramsey number."
        ):
            self.play(FadeIn(step3))
        self.wait(1)

        with self.voiceover(
            text="The critical assumption here is independence. "
                 "Every edge is colored independently of all others. "
                 "This is where the new paper finds room for improvement."
        ):
            self.play(FadeIn(key_word))
            self.wait(2)
            self.play(Indicate(key_word, color=YELLOW))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 5: The Main Result
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{The Main Result}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        setup_tex = Tex(
            r"Let $C > 1$ be a constant. Define $p_C \in (0, 1/2)$ as the unique solution to",
            font_size=28,
        )

        pc_eq = MathTex(
            r"C = \frac{\log p_C}{\log(1 - p_C)}",
            font_size=34,
            color=TEAL,
        )

        erdos_label = Tex(
            r"Erd\H{o}s's bound: $r(\ell, C\ell) \ge \Omega\!\bigl(\ell \cdot p_C^{-\ell/2}\bigr)$",
            font_size=28,
            color=GREY_B,
        )

        thm_label = Tex(
            r"\textbf{Theorem 1.1} (Ma--Shen--Xie, 2025):",
            font_size=28,
            color=GOLD,
        )

        thm_eq = MathTex(
            r"r(\ell,\, C\ell) \;\ge\; \left(p_C^{-1/2} + \varepsilon\right)^{\ell}",
            font_size=40,
            color=GREEN,
        )

        thm_note = Tex(
            r"for some $\varepsilon = \varepsilon(C) > 0$ and all $\ell$ sufficiently large.",
            font_size=26,
            color=GREY_B,
        )

        card, rect, card_content = make_theorem_card(
            thm_eq, thm_note,
            color=GREEN,
            buff=0.3,
        )

        all_items = VGroup(setup_tex, pc_eq, erdos_label, thm_label, card)
        all_items.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        all_items.next_to(title, DOWN, buff=0.5)
        all_items.set_x(0)
        center_mathtex(all_items)
        card.set_x(0)

        with self.voiceover(
            text="Here is the main result. Fix a constant C greater than 1. "
                 "Define p C as the unique value in the interval 0 to one half "
                 "satisfying C equals log p C over log of 1 minus p C. "
                 "This p C is a specific constant determined entirely by C."
        ):
            self.play(FadeIn(setup_tex))
            self.wait(1.5)
            self.play(Write(pc_eq))
        self.wait(1)


        with self.voiceover(
            text="Erdos's bound says r of l and C l is at least on the order of l times "
                 "p C to the minus l over 2. "
                 "Jay Ma, Wu-Jay Shen, and Sheng-Jay Shay prove that the base of the exponential "
                 "can be strictly increased."
        ):
            self.play(FadeIn(erdos_label))
            self.wait(3)
            self.play(FadeIn(thm_label))
        self.wait(0.8)


        with self.voiceover(
            text="Their theorem: r of l and C l is at least p C to the minus one half, "
                 "plus epsilon, all raised to the power l. "
                 "This epsilon is strictly positive, depending only on C. "
                 "For all l sufficiently large, this beats Erdos's bound exponentially!"
        ):
            self.play(FadeIn(card_content), Create(rect))
            self.wait(2)
            self.play(Circumscribe(card, color=GREEN, time_width=2))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 6: The Key Idea — Random Sphere Graphs
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{The Key Idea: Replace Independence}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        idea_erdos = Tex(
            r"$\bullet$ \textbf{Erd\H{o}s:} Color edges independently at random (Erd\H{o}s--R\'enyi model).",
            font_size=28,
        )

        idea_new = Tex(
            r"$\bullet$ \textbf{Ma--Shen--Xie:} Color edges using \textit{geometry} "
            r"--- the \textbf{random sphere graph}.",
            font_size=28,
            color=TEAL,
        )

        comparison = Tex(
            r"Each edge is still red with probability $p$. \\",
            r"But edge colors are now \textit{subtly correlated}!",
            font_size=28,
            color=YELLOW,
            tex_environment="flushleft",
        )

        content = make_content_group(
            idea_erdos, idea_new, comparison,
            reference=title,
            buff_between=0.5,
            buff_below=0.6,
        )

        with self.voiceover(
            text="Here is the crucial idea."
        ):
            pass
        self.wait(0.5)


        with self.voiceover(
            text="Erdos colored edges independently at random, "
                 "using what we now call the Erdos-Renyi random graph model."
        ):
            self.play(FadeIn(idea_erdos))
        self.wait(1)


        with self.voiceover(
            text="Ma, Shen, and Shay replace this with a geometric construction: "
                 "the random sphere graph. "
                 "Instead of flipping independent coins for each edge, "
                 "they place vertices as random points on a high-dimensional sphere "
                 "and let geometry determine the colors."
        ):
            self.play(FadeIn(idea_new))
        self.wait(1.2)


        with self.voiceover(
            text="Each individual edge is still red with probability p, "
                 "exactly the same marginal probability as in Erdos's model. "
                 "But the edge colors are no longer independent. "
                 "They have subtle geometric correlations. "
                 "And surprisingly, these correlations make monochromatic cliques rarer!"
        ):
            self.play(FadeIn(comparison))
            self.wait(2)
            self.play(Indicate(comparison, color=YELLOW))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 7: Proof Roadmap
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Proof Roadmap}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        step_colors = [BLUE, TEAL, GOLD, GREEN]
        step_labels = [
            r"\textbf{Step 1: Sphere Graph}",
            r"\textbf{Step 2: Geometric Deps.}",
            r"\textbf{Step 3: Perfect Sequences}",
            r"\textbf{Step 4: Asymmetry Trick}",
        ]
        step_descs = [
            r"Place $n$ random points on \\ $S^k$ and threshold inner products",
            r"Red cliques rarer, blue \\ cliques less common than ER",
            r"Nearly orthogonal sequences \\ capture essential behavior",
            r"Choose $p$ slightly above $p_C$ \\ to beat both bounds simultaneously",
        ]

        cards = VGroup()
        for i, (color, label, desc) in enumerate(
            zip(step_colors, step_labels, step_descs)
        ):
            box = RoundedRectangle(
                width=5.0,
                height=1.6,
                corner_radius=0.15,
                color=color,
                stroke_width=2.5,
                fill_color=color,
                fill_opacity=0.08,
            )
            label_tex = Tex(label, font_size=26, color=color)
            desc_tex = Tex(
                desc, font_size=24, color=GREY_B, tex_environment="flushleft"
            )
            inner = VGroup(label_tex, desc_tex).arrange(
                DOWN, buff=0.15, aligned_edge=LEFT
            )
            inner.move_to(box.get_center())
            card_group = VGroup(box, inner)
            cards.add(card_group)

        # Arrange as 2x2 grid
        top_row = VGroup(cards[0], cards[1]).arrange(RIGHT, buff=0.5)
        bot_row = VGroup(cards[2], cards[3]).arrange(RIGHT, buff=0.5)
        grid = VGroup(top_row, bot_row).arrange(DOWN, buff=0.4)
        grid.next_to(title, DOWN, buff=0.6)
        grid.set_x(0)

        with self.voiceover(
            text="Here's the roadmap of the proof in four steps. "
                 "Step one: construct the random sphere graph by placing points "
                 "on a high-dimensional sphere."
        ):
            self.play(FadeIn(cards[0], shift=RIGHT * 0.3))
        self.wait(1)


        with self.voiceover(
            text="Step two: analyze the geometric dependencies between edge colors."
        ):
            self.play(FadeIn(cards[1], shift=RIGHT * 0.3))
        self.wait(1)


        with self.voiceover(
            text="Step three: introduce perfect sequences, where vectors are nearly orthogonal, "
                 "and show they capture the essential behavior."
        ):
            self.play(FadeIn(cards[2], shift=RIGHT * 0.3))
        self.wait(1)


        with self.voiceover(
            text="Step four: use a clever asymmetry trick, choosing p slightly above p C "
                 "to beat both the red and blue clique bounds simultaneously."
        ):
            self.play(FadeIn(cards[3], shift=RIGHT * 0.3))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 8: The Random Sphere Graph — Definition
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Step 1: The Random Sphere Graph $G_{k,p}(n)$}",
            font_size=40,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        defn1 = Tex(
            r"$\bullet$ Let $S^k$ be the $k$-dimensional unit sphere in $\mathbb{R}^{k+1}$.",
            font_size=28,
        )

        defn2 = Tex(
            r"$\bullet$ Sample $n$ points $x_1, \ldots, x_n$ uniformly at random on $S^k$.",
            font_size=28,
        )

        defn3 = Tex(
            r"$\bullet$ Fix a reference direction $e \in S^k$ (e.g.\ the north pole).",
            font_size=28,
        )

        defn3b = Tex(
            r"$\bullet$ Choose $c_{k,p} \ge 0$ so that "
            r"$\Pr[\langle x, e \rangle \le -c_{k,p}/\!\sqrt{k}\,] = p$.",
            font_size=28,
        )

        defn4 = Tex(
            r"$\bullet$ Color edge $x_i x_j$: ",
            font_size=28,
        )

        color_rule = MathTex(
            r"\text{red} \;\text{if}\; "
            r"\langle x_i, x_j \rangle \le -\frac{c_{k,p}}{\sqrt{k}}, "
            r"\qquad "
            r"\text{blue} \;\text{otherwise}",
            font_size=30,
        )

        content = make_content_group(
            defn1, defn2, defn3, defn3b, defn4, color_rule,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Let's define the random sphere graph. "
                 "Take the k-dimensional unit sphere."
        ):
            self.play(FadeIn(defn1))
        self.wait(0.8)


        with self.voiceover(
            text="Sample n points uniformly at random on it."
        ):
            self.play(FadeIn(defn2))
        self.wait(0.8)


        with self.voiceover(
            text="Pick a fixed reference direction e on the sphere, "
                 "you can think of it as the north pole. "
                 "By the symmetry of the sphere, the choice doesn't matter."
        ):
            self.play(FadeIn(defn3))
        self.wait(1)


        with self.voiceover(
            text="Now choose a threshold c k p so that "
                 "the probability a random point has inner product below "
                 "minus c k p over root k with the north pole equals exactly p."
        ):
            self.play(FadeIn(defn3b))
        self.wait(1)


        with self.voiceover(
            text="Now color each edge."
        ):
            self.play(FadeIn(defn4))
        self.wait(0.8)


        with self.voiceover(
            text="If the inner product of x i and x j "
                 "is below the threshold, color it red. Otherwise, color it blue."
        ):
            self.play(Write(color_rule))
        self.wait(1)


        with self.voiceover(
            text="So red edges connect points that are nearly antipodal, "
                 "meaning they point in roughly opposite directions."
        ):
            pass
        self.wait(0.8)


        # Show the limiting value of c_{k,p}
        ckp_limit = MathTex(
            r"c_{k,p} \;\xrightarrow{k \to \infty}\; \Phi^{-1}(1-p)",
            font_size=30,
            color=GREY_B,
        ).next_to(color_rule, DOWN, buff=0.4)

        with self.voiceover(
            text="What is this constant c k p concretely? "
                 "As the dimension k grows, c k p converges to "
                 "the quantile of the standard normal distribution "
                 "at one minus p. "
                 "So for large k, this threshold is a fixed bounded constant."
        ):
            self.play(FadeIn(ckp_limit))
        self.wait(1.2)


        with self.voiceover(
            text="Why this convention? Because nearly antipodal points are "
                 "geometrically constrained. If two points are both nearly "
                 "opposite to a third point, they must be close to each other, "
                 "so they cannot also be opposite to each other. "
                 "This makes it hard to form large red cliques, "
                 "which is exactly what we want for the Ramsey bound."
        ):
            pass
        self.wait(1.5)


        self.wait(2)
        clear_screen(self)

        # ─────────────────────────────────────────────────────────────────
        # Scene 8b: Sphere Diagram (Intuition) — Redesigned
        # ─────────────────────────────────────────────────────────────────

        title = Tex(
            r"\textbf{Intuition: Red = Far Apart on the Sphere}",
            font_size=40,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        # ── Left side: sphere diagram ──
        sphere_center = LEFT * 3.2 + DOWN * 0.5

        # Transparent hemisphere shading to make sphere look solid
        # Upper half (blue neighbors live here) — blue tint
        upper_half = Arc(
            radius=2.0,
            start_angle=0,
            angle=PI,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.08,
            stroke_width=0,
        ).shift(sphere_center)

        # Lower half (red/antipodal neighbors live here) — red tint
        lower_half = Arc(
            radius=2.0,
            start_angle=PI,
            angle=PI,
            color=RED,
            fill_color=RED,
            fill_opacity=0.08,
            stroke_width=0,
        ).shift(sphere_center)

        # Draw a 3D-looking sphere: circle + equator ellipse
        sphere_outline = Circle(
            radius=2.0,
            color=WHITE,
            stroke_width=2,
        ).move_to(sphere_center)

        # Equator as an ellipse
        equator = Ellipse(
            width=4.0,
            height=0.8,
            color=GREY,
            stroke_width=1.2,
            stroke_opacity=0.5,
        ).move_to(sphere_center)

        # North pole label
        north_label = Tex(
            r"North", font_size=20, color=GREY_B
        ).next_to(sphere_outline, UP, buff=0.15)

        # South pole label
        south_label = Tex(
            r"South", font_size=20, color=GREY_B
        ).next_to(sphere_outline, DOWN, buff=0.15)

        # Point x near the top (north hemisphere)
        x_pos = sphere_center + UP * 1.6 + LEFT * 0.3
        x_dot = Dot(x_pos, color=YELLOW, radius=0.1)
        x_label = Tex(r"$x$", font_size=28, color=YELLOW).next_to(x_dot, LEFT, buff=0.12)

        # Red neighbors: points near the south (antipodal to x)
        np.random.seed(42)
        red_positions = [
            sphere_center + DOWN * 1.5 + LEFT * 0.5,
            sphere_center + DOWN * 1.3 + RIGHT * 0.4,
            sphere_center + DOWN * 1.7 + RIGHT * 0.1,
        ]
        red_neighbor_dots = VGroup(*[
            Dot(pos, color=RED, radius=0.09) for pos in red_positions
        ])

        # Blue neighbors: points near x (same hemisphere)
        blue_positions = [
            sphere_center + UP * 1.1 + RIGHT * 0.8,
            sphere_center + UP * 0.6 + LEFT * 1.0,
            sphere_center + UP * 0.3 + RIGHT * 1.3,
            sphere_center + RIGHT * 0.5 + UP * 1.4,
        ]
        blue_neighbor_dots = VGroup(*[
            Dot(pos, color=BLUE, radius=0.09) for pos in blue_positions
        ])

        # Red edges from x to red neighbors
        red_edge_lines = VGroup(*[
            Line(x_pos, pos, color=RED, stroke_width=1.8) for pos in red_positions
        ])

        # Blue edges from x to blue neighbors
        blue_edge_lines = VGroup(*[
            DashedLine(x_pos, pos, color=BLUE_D, stroke_width=1.2) for pos in blue_positions
        ])

        # ── Right side: explanation text ──
        right_x = RIGHT * 3.5

        explain1 = Tex(
            r"\textbf{Coloring Rule:}",
            font_size=26,
            color=GOLD,
        ).move_to(right_x + UP * 2.2)

        explain2 = Tex(
            r"Red edge: points are \\",
            r"nearly \textit{antipodal}",
            font_size=24,
            color=RED,
            tex_environment="flushleft",
        ).next_to(explain1, DOWN, buff=0.4)

        explain3 = Tex(
            r"Blue edge: points are \\",
            r"\textit{not} far apart",
            font_size=24,
            color=BLUE,
            tex_environment="flushleft",
        ).next_to(explain2, DOWN, buff=0.4)

        explain4 = Tex(
            r"Each edge is red with \\",
            r"probability $p$, same as \\",
            r"Erd\H{o}s's model.",
            font_size=24,
            color=GREY_B,
            tex_environment="flushleft",
        ).next_to(explain3, DOWN, buff=0.4)

        explain5 = Tex(
            r"\textbf{But edges are} \\",
            r"\textbf{not independent!}",
            font_size=26,
            color=YELLOW,
            tex_environment="flushleft",
        ).next_to(explain4, DOWN, buff=0.5)

        with self.voiceover(
            text="Here is the geometric picture. "
                 "Imagine a sphere. "
                 "Place a point x near the north pole."
        ):
            self.play(
                Create(sphere_outline), Create(equator),
                FadeIn(upper_half), FadeIn(lower_half),
            )
            self.wait(0.5)
            self.play(FadeIn(north_label), FadeIn(south_label))
            self.wait(1)
            self.play(FadeIn(x_dot), FadeIn(x_label))
        self.wait(0.8)


        with self.voiceover(
            text="The red neighbors of x are the points near the south pole, "
                 "the antipodal region. "
                 "These are the points that are farthest from x."
        ):
            self.play(FadeIn(red_neighbor_dots), Create(red_edge_lines))
            self.wait(1)
            self.play(FadeIn(explain1), FadeIn(explain2))
        self.wait(1)


        with self.voiceover(
            text="The blue neighbors are all the other points, "
                 "those that are not far enough away to trigger the red threshold."
        ):
            self.play(FadeIn(blue_neighbor_dots), Create(blue_edge_lines))
            self.wait(1)
            self.play(FadeIn(explain3))
        self.wait(1)


        with self.voiceover(
            text="Each individual edge is red with probability p, "
                 "exactly as in Erdos's model. "
                 "But because all points live on the same sphere, "
                 "the edge colors are not independent. "
                 "They share geometric constraints."
        ):
            self.play(FadeIn(explain4))
            self.wait(2)
            self.play(FadeIn(explain5))
            self.wait(1)
            self.play(Indicate(explain5, color=YELLOW))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 9: ER vs Sphere — Geometric Dependencies
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Step 2: Geometric Dependencies}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        er_header = Tex(
            r"\textbf{Erd\H{o}s--R\'enyi (independent edges):}",
            font_size=28,
            color=GREY_B,
        )

        er_red = MathTex(
            r"\Pr[\text{red } K_r] = p^{\binom{r}{2}}",
            font_size=30,
        )

        er_blue = MathTex(
            r"\Pr[\text{blue } K_r] = (1-p)^{\binom{r}{2}}",
            font_size=30,
        )

        sphere_header = Tex(
            r"\textbf{Random Sphere Graph (dependent edges):}",
            font_size=28,
            color=TEAL,
        )

        sphere_red = MathTex(
            r"\Pr[\text{red } K_r] \;<\; p^{\binom{r}{2}}",
            font_size=30,
            color=RED,
        )

        sphere_blue = MathTex(
            r"\Pr[\text{blue } K_r] \;>\; (1-p)^{\binom{r}{2}}",
            font_size=30,
            color=BLUE,
        )

        content = make_content_group(
            er_header, er_red, er_blue,
            sphere_header, sphere_red, sphere_blue,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Here is the key comparison. In the Erdos-Renyi model with independent edges, "
                 "the probability that r specific vertices form a red clique "
                 "is p to the r choose 2. "
                 "And for a blue clique it is 1 minus p to the r choose 2."
        ):
            self.play(FadeIn(er_header))
            self.wait(1)
            self.play(FadeIn(er_red))
            self.wait(1.5)
            self.play(FadeIn(er_blue))
        self.wait(1)


        with self.voiceover(
            text="In the random sphere graph, something remarkable happens. "
                 "Red cliques become strictly less likely than in Erdos-Renyi! "
                 "Blue cliques become more likely, but this turns out to be manageable. "
                 "The red suppression is the source of the exponential improvement."
        ):
            self.play(FadeIn(sphere_header))
            self.wait(1)
            self.play(FadeIn(sphere_red))
            self.wait(2)
            self.play(FadeIn(sphere_blue))
            self.wait(2)
            self.play(Indicate(sphere_red, color=RED))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ─────────────────────────────────────────────────────────────────
        # Scene 9b: Why Red Cliques Are Suppressed — Intuition
        # ─────────────────────────────────────────────────────────────────

        title = Tex(
            r"\textbf{Why Are Red Cliques Suppressed?}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        intuition1 = Tex(
            r"$\bullet$ For $x_1, x_2$ to both be red neighbors of $x_3$: \\",
            r"$\phantom{\bullet}$\; both must lie near the \textit{antipode} of $x_3$.",
            font_size=28,
            tex_environment="flushleft",
        )

        intuition2 = Tex(
            r"$\bullet$ But if $x_1$ and $x_2$ are both near the antipode of $x_3$, \\",
            r"$\phantom{\bullet}$\; they are \textit{close to each other}!",
            font_size=28,
            color=TEAL,
            tex_environment="flushleft",
        )

        intuition3 = Tex(
            r"$\bullet$ Close points have \textit{positive} inner product $\Rightarrow$ "
            r"less likely to be a red edge.",
            font_size=28,
            color=RED,
        )

        conclusion = Tex(
            r"\textbf{Red clique condition forces points to cluster,} \\",
            r"\textbf{making additional red edges harder to form!}",
            font_size=28,
            color=YELLOW,
            tex_environment="flushleft",
        )

        content = make_content_group(
            intuition1, intuition2, intuition3, conclusion,
            reference=title,
            buff_between=0.45,
            buff_below=0.5,
        )

        with self.voiceover(
            text="Here is the geometric intuition. "
                 "For x 1 and x 2 to both be red neighbors of x 3, "
                 "they must both lie near the antipode of x 3 on the sphere."
        ):
            self.play(FadeIn(intuition1))
        self.wait(1)


        with self.voiceover(
            text="But if x 1 and x 2 are both near the antipode of x 3, "
                 "then x 1 and x 2 must be close to each other."
        ):
            self.play(FadeIn(intuition2))
        self.wait(1)


        with self.voiceover(
            text="And close points have positive inner product, "
                 "which means they are less likely to be connected by a red edge. "
                 "Remember, red edges require a very negative inner product."
        ):
            self.play(FadeIn(intuition3))
        self.wait(1)


        with self.voiceover(
            text="So the red clique condition creates a geometric tension. "
                 "Forcing points to cluster near an antipode "
                 "makes additional red edges harder to form. "
                 "This is why red cliques are suppressed in the sphere graph!"
        ):
            self.play(FadeIn(conclusion))
            self.wait(2)
            self.play(Indicate(conclusion, color=YELLOW))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 9c: High-Dimensional Sphere Intuition (NEW)
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{High Dimensions: Concentration of Measure}",
            font_size=40,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        low_d = Tex(
            r"$\bullet$ On a circle ($k = 1$): two points near the south pole \\",
            r"$\phantom{\bullet}$\; can easily be close \textit{and} both far from the north pole.",
            font_size=28,
            tex_environment="flushleft",
        )

        high_d = Tex(
            r"$\bullet$ On a high-dimensional sphere ($k$ large): random vectors \\",
            r"$\phantom{\bullet}$\; are almost orthogonal with high probability.",
            font_size=28,
            color=TEAL,
            tex_environment="flushleft",
        )

        inner_prod = MathTex(
            r"|\langle x, y \rangle| = \Theta\!\left(\frac{1}{\sqrt{k}}\right)"
            r"\quad \text{for random } x, y \in S^k",
            font_size=30,
            color=GREY_B,
        )

        tension = Tex(
            r"$\bullet$ If $k$ is very large: vectors behave almost independently \\",
            r"$\phantom{\bullet}$\;$\Rightarrow$ sphere graph looks like Erd\H{o}s--R\'enyi (no improvement!).",
            font_size=28,
            tex_environment="flushleft",
        )

        key_insight = Tex(
            r"$\bullet$ If $k$ is moderate: there is enough geometric structure \\",
            r"$\phantom{\bullet}$\; to suppress red cliques, but not so much that blue cliques explode.",
            font_size=28,
            color=GREEN,
            tex_environment="flushleft",
        )

        content = make_content_group(
            low_d, high_d, inner_prod, tension, key_insight,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Before choosing the dimension, let's build some intuition. "
                 "On a low-dimensional sphere, like a circle, "
                 "two points near the south pole can easily be close to each other "
                 "and both far from the north pole."
        ):
            self.play(FadeIn(low_d))
        self.wait(1)


        with self.voiceover(
            text="But on a high-dimensional sphere, something surprising happens. "
                 "Random vectors are almost orthogonal, with inner product of order "
                 "1 over root k. "
                 "This is the concentration of measure phenomenon."
        ):
            self.play(FadeIn(high_d))
            self.wait(2)
            self.play(Write(inner_prod))
        self.wait(1)


        with self.voiceover(
            text="If k is too large, the inner products become tiny, "
                 "and the sphere graph degenerates into the Erdos-Renyi model. "
                 "All geometric structure is lost, and we gain nothing."
        ):
            self.play(FadeIn(tension))
        self.wait(1)


        with self.voiceover(
            text="But if k is chosen moderately, "
                 "there is enough geometric structure "
                 "to suppress red cliques, "
                 "while keeping blue cliques under control. "
                 "This is the sweet spot."
        ):
            self.play(FadeIn(key_insight))
            self.wait(2)
            self.play(Indicate(key_insight, color=GREEN))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 10: The Dimension Choice
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Choosing the Dimension $k$}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        choice = Tex(
            r"The paper sets $k = D^2 \ell^2$ for a large constant $D = D(C)$.",
            font_size=28,
        )

        too_big = Tex(
            r"$\bullet$ If $k$ is much larger than $\ell^2$: sphere is nearly flat locally, \\",
            r"$\phantom{\bullet}$\; points behave almost independently $\Rightarrow$ back to Erd\H{o}s.",
            font_size=28,
            tex_environment="flushleft",
        )

        too_small = Tex(
            r"$\bullet$ If $k$ is much smaller than $\ell^2$: dependencies are too strong, \\",
            r"$\phantom{\bullet}$\; blue clique prob.\ $\gtrsim (1{-}p)^{o(\ell^2)}$, too large for union bound; \\",
            r"$\phantom{\bullet}$\; multiplied by $\binom{n}{C\ell}$ subsets, it forces $n$ to be tiny.",
            font_size=28,
            tex_environment="flushleft",
        )

        just_right = Tex(
            r"$\bullet$ \textbf{Goldilocks:} $k \sim \ell^2$ gives just enough curvature \\",
            r"$\phantom{\bullet}$\; to suppress red cliques while controlling blue cliques.",
            font_size=28,
            color=GREEN,
            tex_environment="flushleft",
        )

        why_l2 = Tex(
            r"$\bullet$ Each ratio $\kappa_{r+1}/\kappa_r$ deviates from $p$ by $\sim r / \sqrt{k}$. \\",
            r"$\phantom{\bullet}$\; Averaging over $r = 1, \ldots, \ell$ gives base correction $\sim \ell / \sqrt{k}$. \\",
            r"$\phantom{\bullet}$\; For this to be $O(1)$, we need $\sqrt{k} \sim \ell$, i.e.\ $k \sim \ell^2$.",
            font_size=26,
            color=GREY_B,
            tex_environment="flushleft",
        )

        content = make_content_group(
            choice, too_big, too_small, just_right, why_l2,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="So what dimension should the sphere have? "
                 "The paper sets k equal to D squared times l squared, "
                 "where D is a large constant depending on C."
        ):
            self.play(FadeIn(choice))
        self.wait(1)


        with self.voiceover(
            text="If k is much larger than l squared, the sphere looks locally flat, "
                 "and points behave almost independently. We recover Erdos's bound and gain nothing."
        ):
            self.play(FadeIn(too_big))
        self.wait(1)


        with self.voiceover(
            text="If k is much smaller than l squared, the dependencies are too strong. "
                 "The blue clique probability is only one minus p to the little o of l squared, "
                 "much larger than the one minus p to the C l choose two you need. "
                 "When multiplied by n choose C l in the union bound, "
                 "this forces n to be too small."
        ):
            self.play(FadeIn(too_small))
        self.wait(1)


        with self.voiceover(
            text="The sweet spot is k proportional to l squared. "
                 "This gives just enough curvature to suppress red cliques, "
                 "while keeping blue cliques under control."
        ):
            self.play(FadeIn(just_right))
            self.wait(2)
            self.play(Indicate(just_right, color=GREEN))
        self.wait(1)


        with self.voiceover(
            text="Here is the quantitative reason. "
                 "Each clique-extension ratio deviates from p by roughly r over root k. "
                 "Averaging these corrections over r from 1 to l, "
                 "the effective base correction is on the order of l over root k. "
                 "For this to be a bounded constant, "
                 "we need root k proportional to l, that is, k proportional to l squared."
        ):
            self.play(FadeIn(why_l2))
        self.wait(1.2)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 11: Perfect Sequences
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Step 3: Perfect Sequences}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        intro_text = Tex(
            r"To analyze clique probabilities, the authors decompose \\",
            r"the probability into a telescoping product:",
            font_size=28,
            tex_environment="flushleft",
        )

        telescope = MathTex(
            r"P_{\mathrm{red},\ell} = \kappa_1 \cdot \kappa_2 \cdots \kappa_{\ell-1}",
            font_size=34,
            color=TEAL,
        )

        kappa_def = Tex(
            r"where $\kappa_r = \frac{P_{\mathrm{red},r+1}}{P_{\mathrm{red},r}}$ "
            r"= conditional probability that the next \\",
            r"point extends the red clique.",
            font_size=26,
            tex_environment="flushleft",
        )

        perfect_def_label = Tex(
            r"\textbf{Definition.} A sequence $(x_1, \ldots, x_r)$ on $S^k$ is "
            r"\textbf{perfect} if:",
            font_size=28,
            color=GOLD,
        )

        perfect_def_eq = MathTex(
            r"|\pi_{[i]}(x_{i+1})| \;\le\; \alpha_C \cdot \frac{\sqrt{\ell}}{\sqrt{k}}"
            r"\quad \text{for all } i = 1, \ldots, r-1",
            font_size=30,
        )

        perfect_meaning = Tex(
            r"$\Rightarrow$ Each new vector is \textit{nearly perpendicular} "
            r"to the span of the previous ones!",
            font_size=28,
            color=TEAL,
        )

        content = make_content_group(
            intro_text, telescope, kappa_def,
            perfect_def_label, perfect_def_eq, perfect_meaning,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="To bound clique probabilities, the authors write "
                 "the red clique probability as a telescoping product of conditional factors. "
                 "Each factor kappa r is the conditional probability "
                 "that the next point extends an existing red clique of size r."
        ):
            self.play(FadeIn(intro_text))
            self.wait(2)
            self.play(Write(telescope))
            self.wait(2)
            self.play(FadeIn(kappa_def))
        self.wait(1)


        with self.voiceover(
            text="To analyze these factors, they introduce perfect sequences. "
                 "A sequence of points on the sphere is called perfect "
                 "if each new vector is nearly perpendicular "
                 "to the subspace spanned by the previous vectors."
        ):
            self.play(FadeIn(perfect_def_label))
            self.wait(2)
            self.play(Write(perfect_def_eq))
            self.wait(2)
            self.play(FadeIn(perfect_meaning))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ─────────────────────────────────────────────────────────────────
        # Scene 11b: Why Perfect Sequences Suffice
        # ─────────────────────────────────────────────────────────────────

        title = Tex(
            r"\textbf{Why Perfect Sequences Suffice}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        thm71 = Tex(
            r"\textbf{Theorem 7.1:}",
            font_size=28,
            color=GOLD,
        )

        thm71_eq = MathTex(
            r"P_{\mathrm{red},r} \;\le\; (1 + 2^{-C\ell}) \cdot P_{\mathrm{red},r}^{\mathrm{per}}",
            font_size=32,
            color=GREEN,
        )

        thm71_note = Tex(
            r"The non-perfect contribution is exponentially negligible! \\",
            r"So we only need to analyze perfect sequences.",
            font_size=28,
            color=GREY_B,
            tex_environment="flushleft",
        )

        analogy = Tex(
            r"\textbf{Analogy:} In high dimensions, random vectors are almost \\",
            r"orthogonal with overwhelming probability (concentration of measure).",
            font_size=28,
            color=TEAL,
            tex_environment="flushleft",
        )

        content = make_content_group(
            thm71, thm71_eq, thm71_note, analogy,
            reference=title,
            buff_between=0.4,
            buff_below=0.5,
        )

        with self.voiceover(
            text="A key theorem shows that perfect sequences capture essentially all the behavior. "
                 "The total clique probability is at most the perfect-sequence contribution "
                 "times 1 plus an exponentially small error."
        ):
            self.play(FadeIn(thm71))
            self.wait(1)
            self.play(Write(thm71_eq))
            self.wait(2)
            self.play(FadeIn(thm71_note))
        self.wait(1)


        with self.voiceover(
            text="This makes sense intuitively. In high dimensions, random vectors are "
                 "almost orthogonal with overwhelming probability. "
                 "The non-perfect sequences, where vectors deviate significantly "
                 "from orthogonality, contribute negligibly."
        ):
            self.play(FadeIn(analogy))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 12: The Key Estimates — Redesigned layout
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{The Key Ratio Estimates}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        intro = Tex(
            r"For perfect sequences, the successive ratios of conditional factors satisfy:",
            font_size=28,
        )
        intro.next_to(title, DOWN, buff=0.5)

        # ── Left column: the two kappa formulas ──
        left_x = LEFT * 3.5

        red_label = Tex(
            r"\textbf{Red ratio of ratios:}", font_size=26, color=RED
        )
        red_ratio = MathTex(
            r"\frac{\kappa_{r+1}}{\kappa_r} \;\lesssim\; "
            r"p \;-\; \frac{a_{k,p}}{p^2} \cdot \frac{r}{\sqrt{k}}",
            font_size=30,
            color=RED,
        )

        blue_label = Tex(
            r"\textbf{Blue ratio of ratios:}", font_size=26, color=BLUE
        )
        blue_ratio = MathTex(
            r"\frac{\bar{\kappa}_{r+1}}{\bar{\kappa}_r} \;\lesssim\; "
            r"(1-p) \;+\; \frac{a_{k,p}}{(1-p)^2} \cdot \frac{r}{\sqrt{k}}",
            font_size=30,
            color=BLUE,
        )

        left_group = VGroup(red_label, red_ratio, blue_label, blue_ratio).arrange(
            DOWN, buff=0.4, aligned_edge=LEFT
        )
        left_group.next_to(intro, DOWN, buff=0.6)
        left_group.set_x(-3.0)

        # ── Right column: interpretation arrows ──
        right_x_pos = RIGHT * 3.0

        red_arrow_start = red_ratio.get_right() + RIGHT * 0.4
        red_interp = Tex(
            r"Each successive ratio is \\",
            r"strictly \textit{below} $p$",
            font_size=24,
            color=RED,
            tex_environment="flushleft",
        )
        red_interp.next_to(red_ratio, RIGHT, buff=1.5)

        red_arrow = Arrow(
            red_ratio.get_right() + RIGHT * 0.2,
            red_interp.get_left() + LEFT * 0.1,
            buff=0.1,
            color=RED,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.15,
        )

        blue_interp = Tex(
            r"Each successive ratio is \\",
            r"strictly \textit{above} $1 - p$",
            font_size=24,
            color=BLUE,
            tex_environment="flushleft",
        )
        blue_interp.next_to(blue_ratio, RIGHT, buff=1.5)

        blue_arrow = Arrow(
            blue_ratio.get_right() + RIGHT * 0.2,
            blue_interp.get_left() + LEFT * 0.1,
            buff=0.1,
            color=BLUE,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.15,
        )

        # Bottom note
        akp = Tex(
            r"where $a_{k,p} = \left(\frac{e^{-c^2}}{2\pi}\right)^{3/2}$ "
            r"is a small positive constant.",
            font_size=24,
            color=GREY_B,
        )
        akp.next_to(left_group, DOWN, buff=0.6)
        akp.set_x(0)

        with self.voiceover(
            text="Here are the key estimates. For perfect sequences, "
                 "the ratio of successive red kappas is at most "
                 "p minus a small correction proportional to r over root k."
        ):
            self.play(FadeIn(intro))
            self.wait(1.5)
            self.play(FadeIn(red_label))
            self.wait(0.5)
            self.play(Write(red_ratio))
        self.wait(1)


        with self.voiceover(
            text="This correction makes each successive factor strictly smaller. "
                 "So red cliques are suppressed."
        ):
            self.play(Create(red_arrow), FadeIn(red_interp))
        self.wait(1)


        with self.voiceover(
            text="For blue cliques, the successive ratio is at most "
                 "1 minus p plus a similar correction. "
                 "So blue cliques are slightly more likely than in Erdos-Renyi."
        ):
            self.play(FadeIn(blue_label))
            self.wait(0.5)
            self.play(Write(blue_ratio))
            self.wait(2)
            self.play(Create(blue_arrow), FadeIn(blue_interp))
        self.wait(1)


        with self.voiceover(
            text="The question is: can we handle both simultaneously? "
                 "The red suppression helps us, but the blue inflation hurts. "
                 "The next step addresses exactly this."
        ):
            self.play(FadeIn(akp))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 13: The Asymmetry Trick
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Step 4: The Asymmetry Trick}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        problem = Tex(
            r"\textbf{Problem:} Red cliques are suppressed (good!), \\",
            r"but blue cliques are inflated (bad!). Can we win both?",
            font_size=28,
            color=YELLOW,
            tex_environment="flushleft",
        )

        trick_label = Tex(
            r"\textbf{The trick:} Choose $p$ slightly above $p_C$!",
            font_size=28,
            color=TEAL,
        )

        trick_explain = Tex(
            r"$\bullet$ Increasing $p$ reduces blue clique probability "
            r"(more red means fewer blue cliques).",
            font_size=26,
        )

        trick_explain2 = Tex(
            r"$\bullet$ The geometric red-suppression is strong enough to \\",
            r"$\phantom{\bullet}$\; compensate for the slight increase in $p$.",
            font_size=26,
        )

        key_ineq_label = Tex(
            r"\textbf{Key inequality} that makes this work:",
            font_size=28,
            color=GOLD,
        )

        key_ineq = MathTex(
            r"\frac{C \cdot p_C^2}{(1-p_C)^2} "
            r"= \frac{p_C^2 \cdot \log p_C}{(1-p_C)^2 \cdot \log(1-p_C)} < 1"
            r"\quad \text{for all } p_C \in (0, 1/2)",
            font_size=28,
            color=GREEN,
        )

        content = make_content_group(
            problem, trick_label, trick_explain, trick_explain2,
            key_ineq_label, key_ineq,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Here is the key challenge. The geometric structure suppresses red cliques, "
                 "which is good. But it inflates blue cliques, which is bad. "
                 "Can we beat both bounds simultaneously?"
        ):
            self.play(FadeIn(problem))
        self.wait(1)


        with self.voiceover(
            text="The trick is to choose p slightly above p C. "
                 "Increasing p directly reduces blue clique probabilities, "
                 "because more edges are red, leaving fewer opportunities for blue cliques."
        ):
            self.play(FadeIn(trick_label))
            self.wait(2)
            self.play(FadeIn(trick_explain))
        self.wait(1)


        with self.voiceover(
            text="Meanwhile, the geometric red-suppression is strong enough "
                 "to compensate for the slight increase in p. "
                 "Even though p is slightly higher, "
                 "the sphere geometry still keeps red cliques rare enough."
        ):
            self.play(FadeIn(trick_explain2))
        self.wait(1)


        with self.voiceover(
            text="This works because of a key algebraic inequality. "
                 "The ratio C times p C squared over 1 minus p C squared "
                 "is strictly less than 1. "
                 "This asymmetry between the red correction and the blue correction "
                 "is what allows both bounds to be beaten at once."
        ):
            self.play(FadeIn(key_ineq_label))
            self.wait(1.5)
            self.play(Write(key_ineq))
            self.wait(2)
            self.play(Circumscribe(key_ineq, color=GREEN, time_width=2))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 14: Putting It All Together
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Putting It All Together}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        eps0_note = Tex(
            r"$\bullet$ Define $\varepsilon_0 = \varepsilon_0(C) > 0$: "
            r"a small constant capturing the geometric \\",
            r"$\phantom{\bullet}$\; advantage of the sphere graph over Erd\H{o}s--R\'enyi.",
            font_size=26,
            tex_environment="flushleft",
        )

        step1_text = Tex(
            r"$\bullet$ \textbf{Theorem 2} (key technical result): \\",
            r"$\phantom{\bullet}$\;$P_{\mathrm{red},\ell} \le (p_C - \varepsilon_0 \cdot \ell/\!\sqrt{k}\,)^{\binom{\ell}{2}}$ \\",
            r"$\phantom{\bullet}$\;$\bar{P}_{\mathrm{blue},C\ell} \le (1 - p_C - \varepsilon_0 \cdot \ell/\!\sqrt{k}\,)^{\binom{C\ell}{2}}$",
            font_size=26,
            tex_environment="flushleft",
        )

        step2_text = Tex(
            r"$\bullet$ Set $n = (M_C + \varepsilon)^\ell$ with "
            r"$M_C = p_C^{-1/2}$ and appropriate $\varepsilon > 0$.",
            font_size=26,
        )

        step3_text = Tex(
            r"$\bullet$ \textbf{Union bound:}",
            font_size=26,
        )

        union_eq = MathTex(
            r"\binom{n}{\ell} \cdot P_{\mathrm{red},\ell} "
            r"+ \binom{n}{C\ell} \cdot \bar{P}_{\mathrm{blue},C\ell} "
            r"\;<\; 1",
            font_size=30,
            color=TEAL,
        )

        conclusion_tex = Tex(
            r"$\Rightarrow$ A good coloring exists $\Rightarrow$ "
            r"$r(\ell, C\ell) \ge (p_C^{-1/2} + \varepsilon)^\ell$ \quad $\blacksquare$",
            font_size=28,
            color=GREEN,
        )

        content = make_content_group(
            eps0_note, step1_text, step2_text, step3_text, union_eq, conclusion_tex,
            reference=title,
            buff_between=0.4,
            buff_below=0.45,
        )

        with self.voiceover(
            text="Let's assemble the proof. "
                 "First, define epsilon-zero as a small positive constant "
                 "that depends only on C. "
                 "It captures the precise geometric advantage "
                 "the sphere graph has over independent coloring."
        ):
            self.play(FadeIn(eps0_note))
        self.wait(1)


        with self.voiceover(
            text="The key technical theorem shows that "
                 "both the red and blue clique probabilities in the sphere graph "
                 "have bases strictly below their Erdos-Renyi values. "
                 "The correction is epsilon-zero times l over root k."
        ):
            self.play(FadeIn(step1_text))
        self.wait(1.2)


        with self.voiceover(
            text="Set n equal to M C plus epsilon, all raised to the power l, "
                 "where M C is p C to the minus one half."
        ):
            self.play(FadeIn(step2_text))
        self.wait(1)


        with self.voiceover(
            text="By the union bound, the expected number of monochromatic cliques "
                 "is less than 1."
        ):
            self.play(FadeIn(step3_text))
            self.wait(1)
            self.play(Write(union_eq))
        self.wait(1)


        with self.voiceover(
            text="Therefore, a good coloring exists. "
                 "The Ramsey number r of l and C l is at least "
                 "p C to the minus one half, plus epsilon, raised to the l. "
                 "This completes the proof."
        ):
            self.play(FadeIn(conclusion_tex))
            self.wait(2)
            self.play(Circumscribe(conclusion_tex, color=GREEN, time_width=2))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 15: Context and Significance
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Why This Matters}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        point1 = Tex(
            r"$\bullet$ \textbf{78-year barrier broken:} First exponential improvement \\",
            r"$\phantom{\bullet}$\; over Erd\H{o}s's 1947 probabilistic method for lower bounds.",
            font_size=28,
            tex_environment="flushleft",
        )

        point2 = Tex(
            r"$\bullet$ \textbf{New technique:} Random sphere graphs introduce \\",
            r"$\phantom{\bullet}$\; geometry into Ramsey theory in a fundamentally new way.",
            font_size=28,
            color=TEAL,
            tex_environment="flushleft",
        )

        point3 = Tex(
            r"$\bullet$ \textbf{Complements 2023 breakthrough:} Upper bound improved \\",
            r"$\phantom{\bullet}$\; by Campos et al.; now lower bound improved by Ma--Shen--Xie.",
            font_size=28,
            tex_environment="flushleft",
        )

        point4 = Tex(
            r"$\bullet$ \textbf{Open:} Does this extend to the diagonal case $r(\ell, \ell)$? \\",
            r"$\phantom{\bullet}$\; The method requires $C > 1$; the case $C = 1$ remains wide open.",
            font_size=28,
            color=GOLD,
            tex_environment="flushleft",
        )

        content = make_content_group(
            point1, point2, point3, point4,
            reference=title,
            buff_between=0.4,
            buff_below=0.5,
        )

        with self.voiceover(
            text="Why does this matter? First, it breaks a 78-year barrier. "
                 "This is the first exponential improvement on the Ramsey lower bound "
                 "since Erdos's original 1947 result."
        ):
            self.play(FadeIn(point1))
        self.wait(1)


        with self.voiceover(
            text="Second, the technique is entirely new. "
                 "Random sphere graphs bring high-dimensional geometry "
                 "into Ramsey theory in a way that has never been done before."
        ):
            self.play(FadeIn(point2))
        self.wait(1)


        with self.voiceover(
            text="Third, this complements the 2023 breakthrough of Campos and collaborators "
                 "on the upper bound. Both sides of the Ramsey problem "
                 "have now seen exponential improvements."
        ):
            self.play(FadeIn(point3))
        self.wait(1)


        with self.voiceover(
            text="A major open question remains. "
                 "Does this extend to the diagonal case, r of l and l? "
                 "The current method requires C strictly greater than 1. "
                 "The diagonal case, where C equals 1, remains wide open."
        ):
            self.play(FadeIn(point4))
            self.wait(2)
            self.play(Indicate(point4, color=GOLD))
        self.wait(1)


        self.wait(2)
        clear_screen(self)

        # ═══════════════════════════════════════════════════════════════════
        # Scene 16: Summary
        # ═══════════════════════════════════════════════════════════════════

        title = Tex(
            r"\textbf{Summary}",
            font_size=42,
            color=BLUE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title))

        summary_header = Tex(
            r"\textbf{Ma--Shen--Xie's proof uses four key ingredients:}",
            font_size=30,
            color=TEAL,
        )

        ingredient1 = Tex(
            r"$\bullet$ \textbf{Random sphere graphs} "
            r"--- replace independent edge coloring with geometry",
            font_size=28,
        )

        ingredient2 = Tex(
            r"$\bullet$ \textbf{Geometric dependencies} "
            r"--- red cliques suppressed, blue cliques inflated",
            font_size=28,
        )

        ingredient3 = Tex(
            r"$\bullet$ \textbf{Perfect sequences} "
            r"--- near-orthogonal vectors capture essential behavior",
            font_size=28,
        )

        ingredient4 = Tex(
            r"$\bullet$ \textbf{Asymmetry trick} "
            r"--- choosing $p > p_C$ beats both bounds",
            font_size=28,
        )

        final_eq_label = Tex(
            r"\textbf{Result:}",
            font_size=30,
            color=GOLD,
        )

        final_eq = MathTex(
            r"r(\ell,\, C\ell) \;\ge\; \left(p_C^{-1/2} + \varepsilon\right)^{\ell}",
            font_size=42,
            color=GREEN,
        )

        final_card, final_rect, _ = make_theorem_card(
            final_eq,
            color=GREEN,
            buff=0.3,
        )

        impact = Tex(
            r"A landmark in Ramsey theory: geometry conquers randomness!",
            font_size=28,
            color=GOLD,
        )

        all_items = VGroup(
            summary_header, ingredient1, ingredient2, ingredient3, ingredient4,
            final_eq_label, final_card, impact,
        )
        all_items.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        all_items.next_to(title, DOWN, buff=0.45)
        all_items.set_x(0)
        center_mathtex(all_items)
        final_card.set_x(0)

        with self.voiceover(
            text="To summarize. "
                 "Jay Ma, Wu-Jay Shen, and Sheng-Jay Shay's proof "
                 "rests on four ingredients."
        ):
            self.play(FadeIn(summary_header))
        self.wait(1)


        with self.voiceover(
            text="First, random sphere graphs that replace independent coloring with geometry."
        ):
            self.play(FadeIn(ingredient1))
        self.wait(1)


        with self.voiceover(
            text="Second, geometric dependencies that suppress red cliques."
        ):
            self.play(FadeIn(ingredient2))
        self.wait(1)


        with self.voiceover(
            text="Third, perfect sequences that simplify the analysis."
        ):
            self.play(FadeIn(ingredient3))
        self.wait(1)


        with self.voiceover(
            text="And fourth, a clever asymmetry trick that beats both bounds simultaneously."
        ):
            self.play(FadeIn(ingredient4))
        self.wait(1)


        with self.voiceover(
            text="The result: r of l and C l is at least p C to the minus one half "
                 "plus epsilon, raised to the power l. "
                 "A landmark in Ramsey theory. Geometry conquers randomness!"
        ):
            self.play(FadeIn(final_eq_label))
            self.wait(1)
            self.play(FadeIn(final_eq), Create(final_rect))
            self.wait(2)
            self.play(Circumscribe(final_card, color=GREEN, time_width=2))
            self.wait(2)
            self.play(FadeIn(impact))
        self.wait(1.2)


        self.wait(3)
        clear_screen(self)
