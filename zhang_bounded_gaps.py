from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService
from latent_utils import (
    center_mathtex,
    make_content_group,
    make_theorem_card,
    LatentPrelude,
    clear_screen,
    SEMINAR_BLUE,
)


class ZhangBoundedGaps(LatentPrelude, VoiceoverScene):
    """
    Visualizes Yitang Zhang's 2014 proof on bounded gaps between primes.
    Uses Kokoro TTS for synchronized narration.
    """

    def construct(self):
        self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))
        self.play_prelude()

        # === Intro / Title Card ===
        self.intro()

        # === Prime Gaps Context ===
        self.prime_gaps_context()

        # === Twin Prime Conjecture ===
        self.twin_prime_conjecture()

        # === Sieve Theory Intuition ===
        self.sieve_intuition()

        # === Admissible Tuples ===
        self.admissible_tuples()

        # === GPY Sieve Method ===
        self.gpy_sieve_method()

        # === Level of Distribution ===
        self.level_of_distribution()

        # === GPY Sieve Barrier ===
        self.gpy_barrier()

        # === Zhang's Proof Roadmap ===
        self.zhang_roadmap()

        # === Smooth Moduli Restriction ===
        self.zhang_breakthrough()

        # === Type I and Type II Sums ===
        self.type_sums()

        # === Deligne's Bound ===
        self.deligne_bound()

        # === Putting It All Together ===
        self.putting_it_together()

        # === Main Theorem ===
        self.main_theorem()

        # === Conclusion ===
        self.conclusion()

    # ------------------------------------------------------------------
    # Scene 1: Intro
    # ------------------------------------------------------------------
    def intro(self):
        with self.voiceover(
            text="Welcome to Latent Seminar. "
                 "In 2014, Yitang Zhang published a landmark paper, "
                 "proving for the first time that the gaps between prime numbers are bounded."
        ):
            title = Tex(
                r"\textbf{Bounded Gaps Between Primes}",
                font_size=44,
                color=SEMINAR_BLUE,
            ).to_edge(UP, buff=0.5)
            author = Tex(
                r"Y. Zhang, Ann. Math. 179(3) (2014)",
                font_size=30,
                color=GRAY,
            )
            author.next_to(title, DOWN, buff=0.5)

            self.play(Write(title), run_time=1.5)
            self.play(FadeIn(author))

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 2: Prime Gaps Context
    # ------------------------------------------------------------------
    def prime_gaps_context(self):
        pnt_label = MathTex(
            r"p_n \sim n \log n",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        avg_gap = MathTex(
            r"\text{Average gap: } p_{n+1} - p_n \sim \log p_n",
            font_size=28,
        )
        avg_gap.next_to(pnt_label, DOWN, buff=0.4).set_x(0)

        number_line = NumberLine(
            x_range=[0, 32, 1],
            length=10,
            include_numbers=False,
            include_ticks=True,
        ).shift(DOWN * 0.5)

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dots = VGroup()
        prime_labels = VGroup()
        gap_labels = VGroup()

        for p in primes:
            pos = number_line.n2p(p)
            dot = Dot(pos, radius=0.09, color=YELLOW)
            dots.add(dot)

            lbl = MathTex(str(p), font_size=22)
            lbl.next_to(pos, UP, buff=0.15)
            prime_labels.add(lbl)

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            mid = (number_line.n2p(primes[i]) + number_line.n2p(primes[i + 1])) / 2
            gap_lbl = MathTex(str(gap), font_size=18, color=TEAL)
            gap_lbl.next_to(mid, UP, buff=0.45)
            gap_labels.add(gap_lbl)

        with self.voiceover(text="Let us start with the basics."):
            pass

        self.wait(0.5)

        with self.voiceover(
            text="The prime number theorem tells us "
                 "that the n-th prime is approximately n log n."
        ):
            self.play(Write(pnt_label), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="This means the average gap between consecutive primes "
                 "grows like the logarithm of n. "
                 "So on average, primes get farther apart as we go further out."
        ):
            self.play(FadeIn(avg_gap), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="But the average does not tell the whole story. "
                 "Some gaps are small, and some are very large."
        ):
            self.play(Create(number_line), run_time=1.5)
            self.play(FadeIn(dots), Write(prime_labels), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The question is whether the small gaps keep appearing forever."
        ):
            self.play(FadeIn(gap_labels), run_time=2.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 3: Twin Prime Conjecture
    # ------------------------------------------------------------------
    def twin_prime_conjecture(self):
        header = Tex(
            r"\textbf{The Twin Prime Conjecture}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        conj = MathTex(
            r"\liminf_{n \to \infty} (p_{n+1} - p_n) = 2",
            font_size=36,
        )
        card, rect, content = make_theorem_card(conj, color=YELLOW, buff=0.3)
        card.next_to(header, DOWN, buff=0.5)
        card.set_x(0)

        examples = Tex(
            r"Examples: $(3,5),\, (5,7),\, (11,13),\, (17,19),\, \dots$",
            font_size=26,
            color=TEAL,
        )
        examples.next_to(card, DOWN, buff=0.4)

        zhang_note = Tex(
            r"Zhang proved: $\liminf (p_{n+1} - p_n) < \infty$",
            font_size=28,
            color=GREEN,
        )
        zhang_note.next_to(examples, DOWN, buff=0.4)

        with self.voiceover(
            text="The most famous question about small gaps "
                 "is the Twin Prime Conjecture."
        ):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="It says that there are infinitely many pairs of primes "
                 "that differ by exactly two."
        ):
            self.play(FadeIn(content), Create(rect), run_time=2.0)

        self.wait(1.0)

        with self.voiceover(
            text="For example, three and five, five and seven, "
                 "eleven and thirteen. "
                 "These pairs appear to persist no matter how far you go, "
                 "but nobody has been able to prove this for over a century."
        ):
            self.play(FadeIn(examples), run_time=2.0)

        self.wait(1.0)

        with self.voiceover(
            text="Zhang's breakthrough was to prove a weaker version: "
                 "that the gaps are bounded by some finite number, "
                 "even if we do not know which one."
        ):
            self.play(FadeIn(zhang_note), run_time=2.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 4: Sieve Theory Intuition
    # ------------------------------------------------------------------
    def sieve_intuition(self):
        header = Tex(
            r"\textbf{Sieve Theory Intuition}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        erat_label = Tex(
            r"\textbf{Sieve of Eratosthenes:}",
            font_size=28,
        )
        step1 = Tex(
            r"$\bullet$ Cross out multiples of 2",
            font_size=26,
        )
        step2 = Tex(
            r"$\bullet$ Cross out multiples of 3",
            font_size=26,
        )
        step3 = Tex(
            r"$\bullet$ Cross out multiples of 5, \dots",
            font_size=26,
        )
        modern = Tex(
            r"\textbf{Modern sieves:} use weights $w(n)$",
            font_size=28,
            color=TEAL,
        )
        weight_note = Tex(
            r"$\phantom{\bullet}$\; Large on primes, small on composites",
            font_size=24,
            color=GRAY,
        )

        content = VGroup(erat_label, step1, step2, step3, modern, weight_note)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        # Sieve visualization: numbers 1-30 in a grid
        numbers_grid = VGroup()
        crossed_out = VGroup()
        primes_remaining = VGroup()
        for i in range(1, 31):
            sq = Square(side_length=0.35, fill_opacity=0.9, fill_color=WHITE, stroke_width=1, stroke_color=GRAY)
            num = MathTex(str(i), font_size=16)
            num.move_to(sq.get_center())
            cell = VGroup(sq, num)
            numbers_grid.add(cell)

        numbers_grid.arrange_in_grid(rows=3, cols=10, buff=0.08)
        numbers_grid.scale(0.8)
        numbers_grid.to_corner(DL, buff=0.5)

        # Pre-mark which get crossed out
        composites_2 = {4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
        composites_3 = {9, 15, 21, 27}
        composites_5 = {25}

        with self.voiceover(
            text="Before we get to Zhang's proof, "
                 "let us understand the main tool: sieve theory."
        ):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="The idea goes back to the sieve of Eratosthenes. "
                 "To find primes, you cross out multiples of two, "
                 "then multiples of three, then five, and so on. "
                 "What remains are the primes."
        ):
            self.play(FadeIn(erat_label), run_time=0.8)
            self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=0.8)

            # Animate crossing out multiples of 2
            self.play(FadeIn(numbers_grid), run_time=1.0)
            for idx in range(30):
                n = idx + 1
                if n in composites_2:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(RED, opacity=0.4),
                        run_time=0.08,
                    )

            self.wait(0.3)
            self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=0.8)

            # Cross out multiples of 3
            for idx in range(30):
                n = idx + 1
                if n in composites_3:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(RED, opacity=0.4),
                        run_time=0.08,
                    )

            self.wait(0.3)
            self.play(FadeIn(step3, shift=RIGHT * 0.3), run_time=0.8)

            # Cross out multiples of 5
            for idx in range(30):
                n = idx + 1
                if n in composites_5:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(RED, opacity=0.4),
                        run_time=0.08,
                    )

        self.wait(0.5)

        with self.voiceover(
            text="Modern sieve methods are more sophisticated. "
                 "Instead of crossing out numbers one by one, "
                 "we assign weights to integers that are designed "
                 "to be large on primes and small on composites."
        ):
            self.play(FadeIn(modern), run_time=1.0)
            self.play(FadeIn(weight_note, shift=RIGHT * 0.3), run_time=1.0)

            # Highlight remaining primes
            primes_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
            for idx in range(30):
                n = idx + 1
                if n in primes_set:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(GREEN, opacity=0.6),
                        run_time=0.08,
                    )

        self.wait(0.5)

        with self.voiceover(
            text="The goal is to count how many primes survive the sieve, "
                 "or in our case, how many pairs of integers "
                 "are simultaneously prime."
        ):
            pass

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 5: Admissible Tuples
    # ------------------------------------------------------------------
    def admissible_tuples(self):
        header = Tex(
            r"\textbf{Admissible Tuples}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        motivation = Tex(
            r"\textbf{Why?} Avoid local obstructions to primality",
            font_size=26,
            color=TEAL,
        )
        bad_example = Tex(
            r"Bad: $\{0, 1\}$ --- one is always even",
            font_size=24,
            color=RED,
        )
        def_text = MathTex(
            r"\mathcal{H} = \{h_1, \dots, h_k\} \text{ admissible}",
            font_size=28,
        )
        cond_text = MathTex(
            r"\forall p, \quad |\mathcal{H} \bmod p| < p",
            font_size=28,
        )
        example = Tex(
            r"Good: $\mathcal{H} = \{0, 2, 6\}$",
            font_size=28,
            color=GREEN,
        )
        mod2 = Tex(
            r"$\bmod\, 2$: $\{0, 0, 0\}$ --- 1 of 2 classes",
            font_size=24,
            color=TEAL,
        )
        mod3 = Tex(
            r"$\bmod\, 3$: $\{0, 2, 0\}$ --- 2 of 3 classes",
            font_size=24,
            color=TEAL,
        )
        mod5 = Tex(
            r"$\bmod\, 5$: $\{0, 2, 1\}$ --- 3 of 5 classes",
            font_size=24,
            color=TEAL,
        )

        content = VGroup(motivation, bad_example, def_text, cond_text, example, mod2, mod3, mod5)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        # Residue class visualization: circles for each class
        def make_residue_classes(p, hits, size=0.3):
            """Create visual residue classes with hits highlighted."""
            group = VGroup()
            for i in range(p):
                circle = Circle(radius=size, fill_opacity=0.3, stroke_width=2)
                if i in hits:
                    circle.set_fill(GREEN, opacity=0.7)
                    circle.set_stroke(GREEN, width=3)
                else:
                    circle.set_fill(GRAY, opacity=0.2)
                    circle.set_stroke(GRAY, width=1)
                label = MathTex(str(i), font_size=16)
                label.move_to(circle.get_center())
                group.add(VGroup(circle, label))
            group.arrange(RIGHT, buff=0.15)
            return group

        # Bad tuple {0,1} mod 2: hits all classes
        bad_mod2_label = Tex(r"$\{0,1\} \bmod 2$:", font_size=22)
        bad_mod2_circles = make_residue_classes(2, {0, 1}, size=0.25)
        bad_mod2_circles.next_to(bad_mod2_label, RIGHT, buff=0.3)
        bad_mod2_group = VGroup(bad_mod2_label, bad_mod2_circles)
        bad_mod2_group.set_x(0)

        with self.voiceover(
            text="Now we come to a central concept: admissible tuples. "
                 "Why do we need this notion? "
                 "If you want to find two primes at a fixed distance, "
                 "say distance two, "
                 "you need to make sure there is no obvious obstruction."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(motivation), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="For example, if you look at n and n plus one, "
                 "one of them is always even, "
                 "so they cannot both be prime except for the pair two and three."
        ):
            self.play(FadeIn(bad_example), run_time=1.5)
            self.play(FadeIn(bad_mod2_group), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="An admissible tuple is a set of shifts "
                 "that avoids this kind of obstruction for every prime. "
                 "Formally, a set H is admissible if for every prime p, "
                 "the elements of H do not cover all residue classes modulo p."
        ):
            self.play(FadeOut(bad_mod2_group), run_time=0.5)
            self.play(FadeIn(def_text), run_time=1.5)
            self.play(FadeIn(cond_text), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="For example, the tuple zero, two, six is admissible. "
                 "Modulo two, all three elements are zero, "
                 "so they only hit one residue class. "
                 "Modulo three, they hit zero and two, missing the class one. "
                 "So there is no local obstruction to all three "
                 "being prime simultaneously."
        ):
            self.play(FadeIn(example), run_time=0.8)

            # Show residue class visualizations
            good_mod2_label = Tex(r"$\{0,2,6\} \bmod 2$:", font_size=22)
            good_mod2_circles = make_residue_classes(2, {0}, size=0.25)
            good_mod2_circles.next_to(good_mod2_label, RIGHT, buff=0.3)
            good_mod2_group = VGroup(good_mod2_label, good_mod2_circles)
            good_mod2_group.set_x(0)

            good_mod3_label = Tex(r"$\{0,2,6\} \bmod 3$:", font_size=22)
            good_mod3_circles = make_residue_classes(3, {0, 2}, size=0.25)
            good_mod3_circles.next_to(good_mod3_label, RIGHT, buff=0.3)
            good_mod3_group = VGroup(good_mod3_label, good_mod3_circles)
            good_mod3_group.set_x(0)

            good_mod5_label = Tex(r"$\{0,2,6\} \bmod 5$:", font_size=22)
            good_mod5_circles = make_residue_classes(5, {0, 1, 2}, size=0.2)
            good_mod5_circles.next_to(good_mod5_label, RIGHT, buff=0.3)
            good_mod5_group = VGroup(good_mod5_label, good_mod5_circles)
            good_mod5_group.set_x(0)

            self.play(FadeIn(good_mod2_group), run_time=0.8)
            self.play(FadeIn(mod2), run_time=0.6)
            self.wait(0.3)
            self.play(FadeIn(good_mod3_group), run_time=0.8)
            self.play(FadeIn(mod3), run_time=0.6)
            self.wait(0.3)
            self.play(FadeIn(good_mod5_group), run_time=0.8)
            self.play(FadeIn(mod5), run_time=0.6)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 6: GPY Sieve Method
    # ------------------------------------------------------------------
    def gpy_sieve_method(self):
        header = Tex(
            r"\textbf{The GPY Sieve Method}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        idea = Tex(
            r"\textbf{Key idea:} Weight integers by how ``prime-rich'' they are",
            font_size=26,
            color=TEAL,
        )
        sum_label = Tex(
            r"\textbf{Weighted sum:}",
            font_size=28,
        )
        sum_eq = MathTex(
            r"S = \sum_{n \leq x} "
            r"\left( \sum_{i=1}^{k} \Lambda(n + h_i) - \rho \right) "
            r"w(n)^2",
            font_size=26,
        )
        lambda_def = MathTex(
            r"\Lambda(n) = \begin{cases} \log p & \text{if } n = p^m \\ 0 & \text{otherwise} \end{cases}",
            font_size=24,
        )
        weight_def = MathTex(
            r"w(n) = \sum_{d \mid P(n)} \lambda_d, \quad P(n) = \prod_{i=1}^k (n + h_i)",
            font_size=24,
        )
        conclusion = Tex(
            r"If $S > 0$, then $\exists\, n$ with $> \rho$ primes among $\{n+h_i\}$",
            font_size=26,
            color=GREEN,
        )

        content = VGroup(idea, sum_label, sum_eq, lambda_def, weight_def, conclusion)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        with self.voiceover(
            text="The G P Y method, named after Goldston, Pintz, and Yildirim, "
                 "is the starting point for Zhang's work. "
                 "Here is the key idea."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(idea), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="Instead of looking at individual primes, "
                 "we look at a weighted sum over integers n, "
                 "where the weight is designed to be large "
                 "when many of the shifted values n plus h sub i "
                 "are simultaneously prime."
        ):
            self.play(FadeIn(sum_label), run_time=0.8)
            self.play(FadeIn(sum_eq), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The inner sum counts primes among the shifts "
                 "using the von Mangoldt function. "
                 "Recall that the von Mangoldt function of n "
                 "is log p if n is a power of a prime p, "
                 "and zero otherwise. "
                 "So it essentially detects prime powers."
        ):
            self.play(FadeIn(lambda_def), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The weight w of n is a sieve weight, "
                 "a sum over divisors d of the product of all shifts. "
                 "The coefficients lambda sub d are chosen to optimize the sum. "
                 "The parameter rho is a threshold. "
                 "If the weighted sum is positive, "
                 "it means that for some n, more than rho of the shifts are prime. "
                 "By choosing rho carefully and making the sum positive, "
                 "one can guarantee that at least two shifts are prime simultaneously."
        ):
            self.play(FadeIn(weight_def), run_time=2.0)
            self.wait(0.5)
            self.play(FadeIn(conclusion), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 7: Level of Distribution
    # ------------------------------------------------------------------
    def level_of_distribution(self):
        header = Tex(
            r"\textbf{Level of Distribution}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        ap_label = Tex(
            r"\textbf{Arithmetic progressions:} $a, a+q, a+2q, \dots$",
            font_size=26,
        )
        dirichlet = MathTex(
            r"\pi(x;q,a) \approx \frac{\pi(x)}{\phi(q)}",
            font_size=28,
        )
        level_def = MathTex(
            r"\theta = \sup \left\{ \vartheta : \text{error is small for } q \leq x^\vartheta \right\}",
            font_size=26,
        )
        importance = Tex(
            r"$\bullet$ Larger $\theta$ $\Rightarrow$ more powerful sieve",
            font_size=26,
            color=TEAL,
        )
        importance2 = Tex(
            r"$\bullet$ $\theta > 1/2$ $\Rightarrow$ bounded prime gaps",
            font_size=26,
            color=GREEN,
        )

        content = VGroup(ap_label, dirichlet, level_def, importance, importance2)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        # Visual: arithmetic progression highlight on number line
        number_line = NumberLine(
            x_range=[0, 30, 1],
            length=10,
            include_numbers=False,
            include_ticks=True,
        ).shift(DOWN * 1.5)

        # Highlight progression 1 mod 4: 1, 5, 9, 13, 17, 21, 25, 29
        ap_dots = VGroup()
        for n in range(1, 30, 4):
            pos = number_line.n2p(n)
            dot = Dot(pos, radius=0.12, color=TEAL)
            ap_dots.add(dot)
            lbl = MathTex(str(n), font_size=16, color=TEAL)
            lbl.next_to(pos, UP, buff=0.15)
            ap_dots.add(lbl)

        with self.voiceover(
            text="To make the G P Y sum positive, "
                 "we need to understand how primes are distributed "
                 "in arithmetic progressions. "
                 "An arithmetic progression is a sequence like "
                 "a, a plus q, a plus two q, and so on, "
                 "where a and q are coprime."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(ap_label), run_time=1.0)
            self.play(Create(number_line), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="Dirichlet's theorem tells us that each such progression "
                 "contains infinitely many primes. "
                 "But we need a quantitative version: "
                 "how many primes are there up to x "
                 "in the progression a mod q? "
                 "The prime number theorem for arithmetic progressions says "
                 "this is approximately pi of x divided by phi of q, "
                 "where phi is Euler's totient function."
        ):
            self.play(FadeIn(ap_dots), run_time=1.5)
            self.play(FadeIn(dirichlet), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The level of distribution theta measures "
                 "how large q can be "
                 "while this approximation still holds on average "
                 "over all a coprime to q."
        ):
            self.play(FadeIn(level_def), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="If theta is larger, we can handle larger moduli, "
                 "and the sieve becomes more powerful."
        ):
            self.play(FadeIn(importance), run_time=1.0)
            self.play(FadeIn(importance2), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 8: GPY Sieve Barrier
    # ------------------------------------------------------------------
    def gpy_barrier(self):
        header = Tex(
            r"\textbf{The GPY Barrier}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        req_text = MathTex(
            r"\text{GPY needs } \theta > 1/2",
            font_size=30,
            color=RED,
        )
        bv_text = MathTex(
            r"\text{Bombieri--Vinogradov: } \theta = 1/2",
            font_size=28,
        )
        bv_formula = MathTex(
            r"\sum_{q \leq x^{1/2} / (\log x)^B} \max_{(a,q)=1} "
            r"\left| \pi(x;q,a) - \frac{\pi(x)}{\phi(q)} \right| "
            r"\ll_A \frac{x}{(\log x)^A}",
            font_size=22,
        )
        barrier = Tex(
            r"\textbf{Gap:} need $\theta = 1/2 + \delta$ for some $\delta > 0$",
            font_size=26,
            color=RED,
        )

        info_group = VGroup(req_text, bv_text, bv_formula, barrier)
        info_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        info_group.next_to(header, DOWN, buff=0.5)
        info_group.set_x(0)
        center_mathtex(info_group)

        # Visual: theta scale with barrier line
        theta_line = NumberLine(
            x_range=[0, 1, 0.1],
            length=6,
            include_numbers=True,
        ).shift(DOWN * 2)

        half_mark = Line(
            start=theta_line.n2p(0.5) + UP * 0.5,
            end=theta_line.n2p(0.5) + DOWN * 0.5,
            color=RED,
            stroke_width=4,
        )
        half_label = Tex(r"$\theta = 1/2$", font_size=20, color=RED)
        half_label.next_to(half_mark, UP, buff=0.1)

        bv_region = Line(
            start=theta_line.n2p(0) + DOWN * 0.3,
            end=theta_line.n2p(0.5) + DOWN * 0.3,
            color=BLUE,
            stroke_width=6,
        )
        bv_label = Tex(r"Bombieri--Vinogradov", font_size=18, color=BLUE)
        bv_label.next_to(bv_region, DOWN, buff=0.1)

        gpy_region = Line(
            start=theta_line.n2p(0.5) + UP * 0.7,
            end=theta_line.n2p(1.0) + UP * 0.7,
            color=GREEN,
            stroke_width=6,
        )
        gpy_label = Tex(r"GPY needs this", font_size=18, color=GREEN)
        gpy_label.next_to(gpy_region, UP, buff=0.1)

        gap_arrow = DoubleArrow(
            start=theta_line.n2p(0.5) + UP * 0.15,
            end=theta_line.n2p(0.52) + UP * 0.15,
            color=YELLOW,
            stroke_width=3,
        )
        gap_label = Tex(r"$\delta$", font_size=20, color=YELLOW)
        gap_label.next_to(gap_arrow, UP, buff=0.1)

        with self.voiceover(
            text="Here is the problem. "
                 "The G P Y method needs a level of distribution "
                 "strictly greater than one-half to prove bounded gaps."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(req_text), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="But the best known result is the Bombieri Vinogradov theorem, "
                 "which gives exactly one-half. "
                 "Let us understand what this theorem says. "
                 "It bounds the average error in the prime number theorem "
                 "for arithmetic progressions, "
                 "summed over all moduli q up to x to the theta."
        ):
            self.play(FadeIn(bv_text), run_time=1.0)
            self.play(FadeIn(bv_formula), run_time=2.0)
            self.play(Create(theta_line), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="The error term is small compared to x divided by any power of log x, "
                 "but only when theta is at most one-half. "
                 "This was the fundamental barrier that blocked progress for years. "
                 "The G P Y method was powerful enough to reduce bounded gaps "
                 "to this distribution problem, "
                 "but it could not break past the one-half threshold on its own."
        ):
            self.play(Create(half_mark), Write(half_label), run_time=1.0)
            self.play(Create(bv_region), FadeIn(bv_label), run_time=1.0)
            self.play(Create(gpy_region), FadeIn(gpy_label), run_time=1.0)
            self.play(Create(gap_arrow), FadeIn(gap_label), run_time=0.8)
            self.play(FadeIn(barrier), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 9: Zhang's Proof Roadmap
    # ------------------------------------------------------------------
    def zhang_roadmap(self):
        header = Tex(
            r"\textbf{Zhang's Proof Roadmap}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step1 = Tex(
            r"$\bullet$ \textbf{Step 1:} Restrict to smooth moduli",
            font_size=26,
        )
        step1_note = Tex(
            r"$\phantom{\bullet}$\; Only $q$ with all prime factors $\leq x^\delta$",
            font_size=24,
            color=GRAY,
        )
        step2 = Tex(
            r"$\bullet$ \textbf{Step 2:} Type I / Type II decomposition",
            font_size=26,
        )
        step2_note = Tex(
            r"$\phantom{\bullet}$\; Split error terms by convolution structure",
            font_size=24,
            color=GRAY,
        )
        step3 = Tex(
            r"$\bullet$ \textbf{Step 3:} Deligne's bound on Kloosterman sums",
            font_size=26,
        )
        step3_note = Tex(
            r"$\phantom{\bullet}$\; Deep result from algebraic geometry",
            font_size=24,
            color=GRAY,
        )
        step4 = Tex(
            r"$\bullet$ \textbf{Step 4:} Distribution level $\theta = 1/2 + \delta$",
            font_size=26,
            color=GREEN,
        )
        step4_note = Tex(
            r"$\phantom{\bullet}$\; $\delta \approx 1/584$",
            font_size=24,
            color=GRAY,
        )

        steps = VGroup(step1, step1_note, step2, step2_note, step3, step3_note, step4, step4_note)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        steps.next_to(header, DOWN, buff=0.5)
        steps.set_x(0)
        center_mathtex(steps)

        with self.voiceover(
            text="Zhang's proof follows a clear four-step roadmap. "
                 "Step one: instead of summing over all moduli q, "
                 "he restricts to smooth moduli, "
                 "meaning q whose prime factors are all small. "
                 "This restriction is mild but crucial."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(step1_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text="Step two: he decomposes the error terms "
                 "into Type one and Type two sums. "
                 "Type one sums have a simple convolution structure, "
                 "while Type two sums are bilinear forms."
        ):
            self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(step2_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text="Step three: for the Type two sums, "
                 "he applies Deligne's bound on Kloosterman sums, "
                 "a deep result from algebraic geometry "
                 "proved as part of the Weil conjectures."
        ):
            self.play(FadeIn(step3, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(step3_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text="Step four: combining all estimates, "
                 "he shows the distribution level exceeds one-half "
                 "by a tiny amount, "
                 "approximately one over five hundred eighty-four."
        ):
            self.play(FadeIn(step4, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(step4_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 10: Smooth Moduli Restriction
    # ------------------------------------------------------------------
    def zhang_breakthrough(self):
        header = Tex(
            r"\textbf{Step 1: Smooth Moduli}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        smooth_def = MathTex(
            r"q \text{ is } y\text{-smooth if } p \mid q \implies p \leq y",
            font_size=26,
        )
        example = Tex(
            r"Example: $12 = 2^2 \cdot 3$ is 3-smooth",
            font_size=26,
            color=TEAL,
        )
        zhang_choice = MathTex(
            r"y = x^\delta, \quad \delta \approx \frac{1}{584}",
            font_size=28,
        )
        why_label = Tex(
            r"\textbf{Why this helps:}",
            font_size=28,
            color=TEAL,
        )
        benefit1 = Tex(
            r"$\bullet$ CRT factorization: $\mathbb{Z}/q\mathbb{Z} \cong \prod \mathbb{Z}/p_i^{e_i}\mathbb{Z}$",
            font_size=24,
        )
        benefit2 = Tex(
            r"$\bullet$ Kloosterman structure becomes visible",
            font_size=24,
        )
        benefit3 = Tex(
            r"$\bullet$ Error terms become tractable",
            font_size=24,
        )

        content = VGroup(smooth_def, example, zhang_choice, why_label, benefit1, benefit2, benefit3)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        with self.voiceover(
            text="Let us look at each step in more detail, "
                 "starting with smooth moduli. "
                 "A number q is called y-smooth "
                 "if all of its prime factors are at most y. "
                 "For example, twelve is three-smooth "
                 "because twelve equals two squared times three."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(smooth_def), run_time=1.5)
            self.play(FadeIn(example), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="Zhang restricts his sieve sum "
                 "to only include smooth moduli q. "
                 "He chooses y to be x to the power delta, "
                 "where delta is about one over five hundred eighty-four. "
                 "This is a very small exponent, but it is enough."
        ):
            self.play(FadeIn(zhang_choice), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="Why does this help? "
                 "When q has only small prime factors, "
                 "the arithmetic structure of q is very special. "
                 "The Chinese Remainder Theorem lets us factor "
                 "problems modulo q "
                 "into problems modulo each prime power dividing q. "
                 "This factorization is the key "
                 "that unlocks the deeper analysis."
        ):
            self.play(FadeIn(why_label), run_time=0.8)

            # Visual: CRT factorization
            crt_demo = MathTex(
                r"\mathbb{Z}/12\mathbb{Z} \cong \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}",
                font_size=24,
                color=TEAL,
            )
            crt_demo.next_to(why_label, DOWN, buff=0.4)
            crt_demo.set_x(0)

            self.play(FadeIn(crt_demo), run_time=1.5)
            self.play(FadeIn(benefit1, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(benefit2, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(benefit3, shift=RIGHT * 0.3), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 11: Type I and Type II Sums
    # ------------------------------------------------------------------
    def type_sums(self):
        header = Tex(
            r"\textbf{Step 2: Type I and Type II Sums}",
            font_size=30,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        type1_label = Tex(
            r"\textbf{Type I:} one long variable",
            font_size=28,
            color=TEAL,
        )
        type1_eq = MathTex(
            r"\sum_{m \sim M} \alpha_m \sum_{n \sim N} \psi(mn)",
            font_size=26,
        )
        type1_cond = MathTex(
            r"M \leq x^{1/2 + \delta}, \quad N = x / M \text{ is long}",
            font_size=24,
            color=GRAY,
        )
        type1_note = Tex(
            r"$\phantom{\bullet}$\; Easier: long range gives cancellation",
            font_size=24,
            color=GRAY,
        )
        type2_label = Tex(
            r"\textbf{Type II:} bilinear form",
            font_size=28,
            color=GOLD,
        )
        type2_eq = MathTex(
            r"\sum_{m \sim M} \sum_{n \sim N} \alpha_m \beta_n \, \psi(mn)",
            font_size=26,
        )
        type2_cond = MathTex(
            r"x^\delta \leq M, N \leq x^{1/2 + \delta}",
            font_size=24,
            color=GRAY,
        )
        type2_note = Tex(
            r"$\phantom{\bullet}$\; Harder: needs Cauchy-Schwarz + Kloosterman",
            font_size=24,
            color=GRAY,
        )

        content = VGroup(type1_label, type1_eq, type1_cond, type1_note, type2_label, type2_eq, type2_cond, type2_note)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)
        center_mathtex(content)

        with self.voiceover(
            text="After restricting to smooth moduli, "
                 "Zhang needs to estimate the error terms. "
                 "The error terms come from the difference "
                 "between the actual count of primes "
                 "in arithmetic progressions and the expected count. "
                 "Zhang decomposes these error terms into two types."
        ):
            self.play(Write(header), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="Type one sums have the form of a single sum over m, "
                 "where the coefficients alpha sub m are arbitrary "
                 "but the other variable n is long. "
                 "Think of it as a weighted average "
                 "of a sequence psi over a long range. "
                 "These are easier to handle "
                 "because the long variable gives cancellation."
        ):
            self.play(FadeIn(type1_label), run_time=0.8)
            self.play(FadeIn(type1_eq), run_time=1.5)
            self.play(FadeIn(type1_cond), run_time=1.0)

            # Visual: show long vs short
            short_bar = Rectangle(height=0.3, width=1.5, fill_color=TEAL, fill_opacity=0.6, stroke_width=1)
            long_bar = Rectangle(height=0.3, width=5, fill_color=TEAL, fill_opacity=0.3, stroke_width=1)
            short_label = Tex(r"short $M$", font_size=18)
            long_label = Tex(r"long $N = x/M$", font_size=18)
            short_label.move_to(short_bar)
            long_label.move_to(long_bar)
            type1_vis = VGroup(
                VGroup(short_bar, short_label),
                VGroup(long_bar, long_label),
            )
            type1_vis.arrange(RIGHT, buff=0.3)
            type1_vis.next_to(type1_eq, DOWN, buff=0.3)
            type1_vis.set_x(0)

            self.play(FadeIn(type1_vis), run_time=1.0)
            self.play(FadeIn(type1_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text="Type two sums are bilinear. "
                 "Both variables m and n are of moderate size, "
                 "and both have arbitrary coefficients alpha and beta. "
                 "These are harder because neither variable "
                 "is long enough to give easy cancellation. "
                 "But the bilinear structure is precisely what allows us "
                 "to use Cauchy-Schwarz "
                 "and reduce to estimating Kloosterman sums."
        ):
            self.play(FadeIn(type2_label), run_time=0.8)
            self.play(FadeIn(type2_eq), run_time=1.5)
            self.play(FadeIn(type2_cond), run_time=1.0)

            # Visual: show both moderate
            mod_bar1 = Rectangle(height=0.3, width=2.5, fill_color=GOLD, fill_opacity=0.5, stroke_width=1)
            mod_bar2 = Rectangle(height=0.3, width=2.5, fill_color=GOLD, fill_opacity=0.5, stroke_width=1)
            mod_label1 = Tex(r"moderate $M$", font_size=18)
            mod_label2 = Tex(r"moderate $N$", font_size=18)
            mod_label1.move_to(mod_bar1)
            mod_label2.move_to(mod_bar2)
            type2_vis = VGroup(
                VGroup(mod_bar1, mod_label1),
                VGroup(mod_bar2, mod_label2),
            )
            type2_vis.arrange(RIGHT, buff=0.3)
            type2_vis.next_to(type2_eq, DOWN, buff=0.3)
            type2_vis.set_x(0)

            self.play(FadeIn(type2_vis), run_time=1.0)
            self.play(FadeIn(type2_note, shift=RIGHT * 0.3), run_time=0.8)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 12: Deligne's Bound
    # ------------------------------------------------------------------
    def deligne_bound(self):
        header = Tex(
            r"\textbf{Step 3: Deligne's Bound on Kloosterman Sums}",
            font_size=28,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        kl_label = Tex(
            r"\textbf{Kloosterman sum:}",
            font_size=28,
        )
        kl_def = MathTex(
            r"K(a, b; p) = \sum_{x \in \mathbb{F}_p^\times} "
            r"e\!\left(\frac{ax + b\overline{x}}{p}\right)",
            font_size=26,
        )
        trivial = MathTex(
            r"\text{Trivial bound: } |K| \leq p - 1",
            font_size=24,
            color=GRAY,
        )

        kl_group = VGroup(kl_label, kl_def, trivial)
        kl_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        kl_group.next_to(header, DOWN, buff=0.6)
        kl_group.set_x(0)

        deligne = MathTex(
            r"|K(a, b; p)| \leq 2\sqrt{p}",
            font_size=36,
            color=GREEN,
        )
        card, rect, content = make_theorem_card(deligne, color=GREEN, buff=0.3)
        card.next_to(kl_group, DOWN, buff=0.5)
        card.set_x(0)

        remark = Tex(
            r"Deligne (1974) --- Weil conjectures, algebraic geometry",
            font_size=24,
            color=GRAY,
        )
        remark.next_to(card, DOWN, buff=0.4)

        connection = Tex(
            r"Algebraic geometry $\rightarrow$ analytic number theory $\rightarrow$ prime gaps",
            font_size=24,
            color=TEAL,
        )
        connection.next_to(remark, DOWN, buff=0.3)

        with self.voiceover(
            text="Now we reach the deepest ingredient of Zhang's proof. "
                 "When estimating Type two sums, after applying Cauchy-Schwarz, "
                 "one encounters exponential sums called Kloosterman sums. "
                 "A Kloosterman sum is a sum over the multiplicative group "
                 "of a finite field. "
                 "It involves the exponential of a linear term plus its inverse, "
                 "divided by the prime p."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(kl_label), run_time=0.8)
            self.play(FadeIn(kl_def), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The trivial bound would give p minus one, "
                 "since there are p minus one terms each of size one."
        ):
            self.play(FadeIn(trivial), run_time=1.0)

            # Visual: bar chart comparison
            p_val = 101  # example prime
            trivial_height = 3.0
            deligne_height = 3.0 / (p_val ** 0.5) * 2

            trivial_bar = Rectangle(
                height=trivial_height, width=0.8,
                fill_color=RED, fill_opacity=0.5, stroke_width=1,
            )
            trivial_bar_label = Tex(r"$p$", font_size=18)
            trivial_bar_label.next_to(trivial_bar, UP, buff=0.1)

            deligne_bar = Rectangle(
                height=deligne_height, width=0.8,
                fill_color=GREEN, fill_opacity=0.5, stroke_width=1,
            )
            deligne_bar_label = Tex(r"$2\sqrt{p}$", font_size=18)
            deligne_bar_label.next_to(deligne_bar, UP, buff=0.1)

            bound_vis = VGroup(trivial_bar, trivial_bar_label, deligne_bar, deligne_bar_label)
            bound_vis.arrange(RIGHT, buff=0.5)
            bound_vis.next_to(trivial, DOWN, buff=0.5)
            bound_vis.set_x(0)

            self.play(FadeIn(bound_vis), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text="But Deligne proved, as part of his Fields Medal work "
                 "on the Weil conjectures, "
                 "that these sums exhibit square-root cancellation. "
                 "The absolute value is at most two times the square root of p. "
                 "This is dramatically smaller than p."
        ):
            self.play(FadeIn(content), Create(rect), run_time=2.0)

        self.wait(1.0)

        with self.voiceover(
            text="Without this bound, the error terms in Zhang's estimates "
                 "would be too large, and the proof would fail. "
                 "It is remarkable that a result from algebraic geometry, "
                 "proved using etale cohomology and schemes, "
                 "is the key to a problem about prime numbers."
        ):
            self.play(FadeIn(remark), run_time=1.0)
            self.play(FadeIn(connection), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 13: Putting It All Together
    # ------------------------------------------------------------------
    def putting_it_together(self):
        header = Tex(
            r"\textbf{Putting It All Together}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step_labels = VGroup(
            Tex(r"\textbf{(1) Start with the GPY weighted sum}", font_size=26),
            MathTex(r"S = \sum_{n \leq x} \left(\sum_{i=1}^k \Lambda(n+h_i) - \rho\right) w(n)^2", font_size=24),
            Tex(r"$\bullet$ Goal: show $S > 0$ for some admissible $\mathcal{H}$", font_size=24, color=TEAL),
        )
        step_labels.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_labels.next_to(header, DOWN, buff=0.5)
        step_labels.set_x(0)

        step_analysis = VGroup(
            Tex(r"\textbf{(2) Decompose the error}", font_size=26),
            Tex(r"$\bullet$ Restrict to smooth moduli $q$", font_size=24),
            Tex(r"$\bullet$ Split into Type I sums (one long variable)", font_size=24),
            Tex(r"$\bullet$ Split into Type II sums (bilinear form)", font_size=24),
        )
        step_analysis.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_analysis.next_to(step_labels, DOWN, buff=0.4)
        step_analysis.set_x(0)

        step_estimate = VGroup(
            Tex(r"\textbf{(3) Estimate each type}", font_size=26),
            Tex(r"$\bullet$ Type I: use smooth modulus factorization", font_size=24),
            Tex(r"$\bullet$ Type II: Cauchy-Schwarz $\rightarrow$ Kloosterman sums", font_size=24),
            Tex(r"$\bullet$ Apply Deligne: $|K| \leq 2\sqrt{p}$", font_size=24, color=GREEN),
        )
        step_estimate.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_estimate.next_to(step_analysis, DOWN, buff=0.4)
        step_estimate.set_x(0)

        step_conclude = VGroup(
            Tex(r"\textbf{(4) Conclusion}", font_size=26),
            MathTex(r"\theta = 1/2 + \delta \quad (\delta \approx 1/584)", font_size=28, color=GREEN),
            Tex(r"$\Rightarrow S > 0$ for large enough $k$", font_size=26, color=GREEN),
            Tex(r"$\Rightarrow \exists$ infinitely many $n$ with 2+ primes in $\{n+h_i\}$", font_size=24, color=GREEN),
        )
        step_conclude.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_conclude.next_to(step_estimate, DOWN, buff=0.4)
        step_conclude.set_x(0)

        with self.voiceover(
            text="Now let us see how all the pieces fit together. "
                 "We start with the G P Y weighted sum. "
                 "The goal is to show this sum is positive "
                 "for some admissible tuple H. "
                 "If it is positive, then for some integer n, "
                 "at least two of the shifted values n plus h sub i are prime."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(step_labels), run_time=2.5)

            # Flow arrow animation
            arrow1 = Arrow(
                start=step_labels.get_bottom(),
                end=step_analysis.get_top(),
                color=TEAL,
                buff=0.1,
            )
            self.play(GrowArrow(arrow1), run_time=0.5)

        self.wait(0.5)

        with self.voiceover(
            text="Step two: decompose the error. "
                 "First, we restrict the sum to smooth moduli only. "
                 "This means we only consider q whose prime factors are small. "
                 "Then we split the remaining error terms "
                 "into Type one sums, where one variable is long, "
                 "and Type two sums, which have a bilinear structure."
        ):
            self.play(FadeIn(step_analysis), run_time=3.0)

            arrow2 = Arrow(
                start=step_analysis.get_bottom(),
                end=step_estimate.get_top(),
                color=TEAL,
                buff=0.1,
            )
            self.play(GrowArrow(arrow2), run_time=0.5)

        self.wait(0.5)

        with self.voiceover(
            text="Step three: estimate each type. "
                 "For Type one sums, the smooth modulus structure "
                 "lets us factor the problem using the Chinese Remainder Theorem, "
                 "and the long variable gives us cancellation. "
                 "For Type two sums, we apply Cauchy-Schwarz, "
                 "which reduces the problem to bounding Kloosterman sums. "
                 "And here we use Deligne's bound: "
                 "the absolute value is at most two times the square root of p."
        ):
            self.play(FadeIn(step_estimate), run_time=3.5)

            arrow3 = Arrow(
                start=step_estimate.get_bottom(),
                end=step_conclude.get_top(),
                color=GREEN,
                buff=0.1,
            )
            self.play(GrowArrow(arrow3), run_time=0.5)

        self.wait(0.5)

        with self.voiceover(
            text="Step four: putting the estimates together, "
                 "we find that the distribution level exceeds one-half "
                 "by a tiny amount delta, about one over five hundred eighty-four. "
                 "This is just enough to make the G P Y sum positive, "
                 "which guarantees that there are infinitely many integers n "
                 "such that at least two of the shifts n plus h sub i are prime. "
                 "Since the tuple is finite, the gap between these two primes "
                 "is bounded by the diameter of the tuple."
        ):
            self.play(FadeIn(step_conclude), run_time=4.0)

        self.wait(2.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 14: Main Theorem
    # ------------------------------------------------------------------
    def main_theorem(self):
        theorem_title = Tex(
            r"\textbf{Theorem (Zhang, 2014)}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        result = MathTex(
            r"\liminf_{n \to \infty} (p_{n+1} - p_n) \leq 70,\!000,\!000",
            font_size=36,
            color=GREEN,
        )
        card, rect, content = make_theorem_card(result, color=GREEN, buff=0.3)
        card.next_to(theorem_title, DOWN, buff=0.5)
        card.set_x(0)

        pieces = Tex(
            r"Smooth moduli + Type I/II + Deligne $\Rightarrow \theta > 1/2$",
            font_size=24,
            color=TEAL,
        )
        pieces.next_to(card, DOWN, buff=0.5)

        sub_note = Tex(
            r"First finite bound on prime gaps in history",
            font_size=26,
            color=GRAY,
        )
        sub_note.next_to(pieces, DOWN, buff=0.4)

        with self.voiceover(
            text="Putting all the pieces together, "
                 "Zhang proved his main theorem."
        ):
            self.play(Write(theorem_title), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="The smooth moduli restriction makes the error terms manageable. "
                 "The Type one and Type two decomposition organizes the analysis. "
                 "Deligne's bound provides the crucial square-root cancellation "
                 "for the hardest terms."
        ):
            # Dramatic reveal: build up to the theorem
            self.play(FadeIn(content), Create(rect), run_time=2.0)

        self.wait(1.0)

        with self.voiceover(
            text="And the result is that the distribution level exceeds one-half "
                 "by a tiny but positive amount. "
                 "This is enough to make the G P Y sum positive, "
                 "which guarantees that some pair of shifts "
                 "is prime infinitely often."
        ):
            self.play(FadeIn(pieces), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="The bound he obtained was seventy million. "
                 "This was the first time anyone proved "
                 "that prime gaps are bounded by any finite number."
        ):
            # Dramatic flash on the number
            self.play(
                rect.animate.set_stroke(YELLOW, width=6),
                run_time=0.5,
            )
            self.play(
                rect.animate.set_stroke(GREEN, width=4),
                run_time=0.5,
            )
            self.play(FadeIn(sub_note), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 15: Conclusion
    # ------------------------------------------------------------------
    def conclusion(self):
        header = Tex(
            r"\textbf{Aftermath}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        poly = MathTex(
            r"\text{Polymath8} \rightarrow \text{Bound } 4,\!680",
            font_size=28,
        )
        may = MathTex(
            r"\text{Maynard (2013)} \rightarrow \text{Bound } 246",
            font_size=28,
        )
        eh = MathTex(
            r"\text{Under GEH: Bound } 6",
            font_size=26,
            color=TEAL,
        )
        twin = MathTex(
            r"\text{Open: } \liminf (p_{n+1} - p_n) = 2",
            font_size=30,
            color=YELLOW,
        )

        items = VGroup(poly, may, eh, twin)
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        items.to_corner(UL, buff=0.8)

        # Timeline visualization: decreasing bounds
        timeline_header = Tex(r"\textbf{Bound over time:}", font_size=24, color=TEAL)
        timeline_header.to_corner(UR, buff=0.8)

        bounds = [
            (r"Zhang 2014", 70000000),
            (r"Polymath8", 4680),
            (r"Maynard", 246),
            (r"GEH", 6),
        ]
        timeline_bars = VGroup()
        for i, (label, bound) in enumerate(bounds):
            height = 0.3 + 2.5 * (1 - (bound ** (1/8)) / (70000000 ** (1/8)))
            bar = Rectangle(
                height=max(0.3, height), width=0.6,
                fill_color=BLUE, fill_opacity=0.6, stroke_width=1,
            )
            lbl = Tex(label, font_size=16)
            lbl.next_to(bar, DOWN, buff=0.1)
            val = Tex(str(bound), font_size=14)
            val.next_to(bar, UP, buff=0.1)
            timeline_bars.add(VGroup(bar, lbl, val))

        timeline_bars.arrange(RIGHT, buff=0.4, aligned_edge=DOWN)
        timeline_bars.next_to(timeline_header, DOWN, buff=0.3)

        with self.voiceover(
            text="Zhang's result sparked an explosion of activity. "
                 "The Polymath project, a collaborative online effort, "
                 "quickly improved the bound from seventy million "
                 "down to four thousand six hundred eighty."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(poly, shift=RIGHT * 0.3), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text="Then James Maynard, working independently, "
                 "introduced a new sieve method "
                 "that brought the bound down to six hundred, "
                 "and later to two hundred forty-six "
                 "when combined with Zhang's ideas."
        ):
            self.play(FadeIn(may, shift=RIGHT * 0.3), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text="The current record is two hundred forty-six. "
                 "Assuming the generalized Elliott Halberstam conjecture, "
                 "it can be reduced to six."
        ):
            self.play(FadeIn(eh, shift=RIGHT * 0.3), run_time=1.5)
            self.play(FadeIn(timeline_header), run_time=0.8)
            for bar_group in timeline_bars:
                self.play(FadeIn(bar_group), run_time=0.5)

        self.wait(0.5)

        with self.voiceover(
            text="But the original Twin Prime Conjecture, "
                 "which claims the bound is exactly two, "
                 "remains wide open."
        ):
            self.play(FadeIn(twin, shift=RIGHT * 0.3), run_time=1.5)

        self.wait(1.5)
        clear_screen(self)
