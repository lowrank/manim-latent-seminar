from manim import *
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService
from BoundedGapPrimeNumbers_Phoetics import get_phonetic_text
from latent_utils import (
    center_mathtex,
    make_content_group,
    make_theorem_card,
    LatentPrelude,
    clear_screen,
    SEMINAR_BLUE,
)


class BoundedGapsProof(LatentPrelude, VoiceoverScene):
    """
    Visualizes Yitang Zhang's 2014 proof on bounded gaps between primes.
    Uses Kokoro TTS for synchronized narration.
    """

    def construct(self):
        self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))
#        self.play_prelude()

        # === Intro / Title Card ===
        self.intro()

        # === Prime Gaps Context ===
        self.prime_gaps_context_part1()
        self.prime_gaps_context_part2()

        # === Twin Prime Conjecture ===
        self.twin_prime_conjecture()

        # === Sieve Theory Intuition ===
        self.sieve_intuition_part1()
        self.sieve_intuition_part2()

        # === Admissible Tuples ===
        self.admissible_tuples_part1()
        self.admissible_tuples_part2()

        # === GPY Sieve Method ===
        self.gpy_sieve_method_part1()
        self.gpy_sieve_method_part2()

        # === Level of Distribution ===
        self.level_of_distribution_part1()
        self.level_of_distribution_part2()

        # === GPY Sieve Barrier ===
        self.gpy_barrier_part1()
        self.gpy_barrier_part2()

        # === Zhang's Proof Roadmap ===
        self.zhang_roadmap()

        # === Smooth Moduli Restriction ===
        self.zhang_breakthrough_part1()
        self.zhang_breakthrough_part2()

        # === Type I and Type II Sums ===
        self.type_sums_part1()
        self.type_sums_part2()

        # === Deligne's Bound ===
        self.deligne_bound_part1()
        self.deligne_bound_part2()

        # === Putting It All Together ===
        self.putting_it_together_part1()
        self.putting_it_together_part2()
        self.putting_it_together_part3()

        # === Main Theorem ===
        self.main_theorem()

        # === Conclusion ===
        self.conclusion_part1()

    # ------------------------------------------------------------------
    # Scene 1: Intro
    # ------------------------------------------------------------------
    def intro(self):
        with self.voiceover(
            text=get_phonetic_text("Welcome to Latent Seminar. "
                 "In 2014, Yitang Zhang published a landmark paper, "
                 "proving for the first time that the gaps between prime numbers are bounded."),
            subcaption="Welcome to Latent Seminar. "
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
    # Scene 2a: Prime Gaps Context — PNT and average gap
    # ------------------------------------------------------------------
    def prime_gaps_context_part1(self):
        header = Tex(
            r"\textbf{Prime Gaps}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        pnt_label = MathTex(
            r"p_n \sim n \log n",
            font_size=32,
            color=BLUE,
        )
        pnt_label.next_to(header, DOWN, buff=0.5).set_x(0)

        avg_gap = MathTex(
            r"\text{Average gap: } p_{n+1} - p_n \sim \log p_n",
            font_size=28,
        )
        avg_gap.next_to(pnt_label, DOWN, buff=0.4).set_x(0)

        with self.voiceover(text=get_phonetic_text("Let us start with the basics."),
            subcaption="Let us start with the basics."):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The prime number theorem tells us "
                 "that the n-th prime is approximately n log n."),
            subcaption="The prime number theorem tells us "
                 "that the n-th prime is approximately n log n."
        ):
            self.play(Write(pnt_label), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("This means the average gap between consecutive primes "
                 "near p is about log p."),
            subcaption="This means the average gap between consecutive primes "
                 "near p is about log p."
        ):
            self.play(FadeIn(avg_gap), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 2b: Prime Gaps Context — What is known
    # ------------------------------------------------------------------
    def prime_gaps_context_part2(self):
        header = Tex(
            r"\textbf{Prime Gaps}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        small_gaps = MathTex(
            r"\liminf_{n \to \infty} \frac{p_{n+1} - p_n}{\log p_n} = 0",
            font_size=28,
        )
        small_gaps.next_to(header, DOWN, buff=0.5).set_x(0)

        note = Tex(
            r"Gaps can be arbitrarily small relative to average",
            font_size=24,
            color=GRAY,
        )
        note.next_to(small_gaps, DOWN, buff=0.4).set_x(0)

        with self.voiceover(
            text=get_phonetic_text("But what about the smallest gaps? "
                 "It was known that the lim inf of the gap divided by log p "
                 "is zero. So gaps can be arbitrarily small relative to the average."),
            subcaption="But what about the smallest gaps? "
                 "It was known that the lim inf of the gap divided by log p "
                 "is zero. So gaps can be arbitrarily small relative to the average."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(Write(small_gaps), run_time=2.0)
            self.play(FadeIn(note), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 3: Twin Prime Conjecture
    # ------------------------------------------------------------------
    def twin_prime_conjecture(self):
        header = Tex(
            r"\textbf{Twin Prime Conjecture}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        conjecture = MathTex(
            r"\liminf_{n \to \infty} (p_{n+1} - p_n) = 2",
            font_size=36,
            color=GREEN,
        )
        conjecture.next_to(header, DOWN, buff=0.6).set_x(0)

        note = Tex(
            r"Infinitely many pairs of primes at distance 2",
            font_size=26,
            color=GRAY,
        )
        note.next_to(conjecture, DOWN, buff=0.4).set_x(0)

        with self.voiceover(
            text=get_phonetic_text("The famous Twin Prime Conjecture goes further. "
                 "It claims that there are infinitely many pairs of primes "
                 "that differ by exactly two."),
            subcaption="The famous Twin Prime Conjecture goes further. "
                 "It claims that there are infinitely many pairs of primes "
                 "that differ by exactly two."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(Write(conjecture), run_time=2.0)
            self.play(FadeIn(note), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 4a: Sieve Theory Intuition — Eratosthenes
    # ------------------------------------------------------------------
    def sieve_intuition_part1(self):
        header = Tex(
            r"\textbf{Sieve Theory Intuition}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        erat_label = Tex(
            r"\textbf{Sieve of Eratosthenes:}",
            font_size=30,
        )
        step1 = Tex(
            r"$\bullet$ Cross out multiples of 2",
            font_size=28,
        )
        step2 = Tex(
            r"$\bullet$ Cross out multiples of 3",
            font_size=28,
        )
        step3 = Tex(
            r"$\bullet$ Cross out multiples of 5, \dots",
            font_size=28,
        )

        erat_content = VGroup(erat_label, step1, step2, step3)
        erat_content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        erat_content.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Sieve visualization: numbers 1-30 in a grid
        numbers_grid = VGroup()
        for i in range(1, 31):
            sq = Square(side_length=0.4, fill_opacity=0.9, fill_color=WHITE, stroke_width=1, stroke_color=GRAY)
            num = MathTex(str(i), font_size=18)
            num.move_to(sq.get_center())
            cell = VGroup(sq, num)
            numbers_grid.add(cell)

        numbers_grid.arrange_in_grid(rows=3, cols=10, buff=0.1)
        numbers_grid.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.6)

        composites_2 = {4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
        composites_3 = {9, 15, 21, 27}
        composites_5 = {25}
        primes_remaining = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

        with self.voiceover(
            text=get_phonetic_text("Before we get to Zhang's proof, "
                 "let us understand the main tool: sieve theory."),
            subcaption="Before we get to Zhang's proof, "
                 "let us understand the main tool: sieve theory."
        ):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The idea goes back to the sieve of Eratosthenes. "
                 "To find primes, you cross out multiples of two, "
                 "then multiples of three, then five, and so on. "
                 "What remains are the primes."),
            subcaption="The idea goes back to the sieve of Eratosthenes. "
                 "To find primes, you cross out multiples of two, "
                 "then multiples of three, then five, and so on. "
                 "What remains are the primes."
        ):
            self.play(FadeIn(erat_label), run_time=0.8)
            self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=0.8)

            self.play(FadeIn(numbers_grid), run_time=1.0)
            for idx in range(30):
                n = idx + 1
                if n in composites_2:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(DARK_GRAY, opacity=0.7),
                        run_time=0.08,
                    )

            self.wait(0.3)
            self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=0.8)

            for idx in range(30):
                n = idx + 1
                if n in composites_3:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(DARK_GRAY, opacity=0.7),
                        run_time=0.08,
                    )

            self.wait(0.3)
            self.play(FadeIn(step3, shift=RIGHT * 0.3), run_time=0.8)

            for idx in range(30):
                n = idx + 1
                if n in composites_5:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    self.play(
                        sq.animate.set_fill(DARK_GRAY, opacity=0.7),
                        run_time=0.08,
                    )

            for idx in range(30):
                n = idx + 1
                if n in primes_remaining:
                    cell = numbers_grid[idx]
                    sq = cell[0]
                    num = cell[1]
                    self.play(
                        sq.animate.set_fill(YELLOW, opacity=1.0),
                        num.animate.set_color(BLACK),
                        run_time=0.08,
                    )

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 4b: Sieve Theory Intuition — Modern sieves
    # ------------------------------------------------------------------
    def sieve_intuition_part2(self):
        header = Tex(
            r"\textbf{Sieve Theory Intuition}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        modern = Tex(
            r"\textbf{Modern sieves:} use weights $w(n)$",
            font_size=30,
            color=TEAL,
        )
        weight_note = Tex(
            r"$\bullet$ Large on primes, small on composites",
            font_size=26,
            color=GRAY,
        )
        goal_note = Tex(
            r"$\bullet$ Count integers where multiple shifts are prime",
            font_size=26,
            color=GRAY,
        )

        modern_content = VGroup(modern, weight_note, goal_note)
        modern_content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        modern_content.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Sieve visualization: numbers 1-30 in a grid
        numbers_grid = VGroup()
        for i in range(1, 31):
            sq = Square(side_length=0.4, fill_opacity=0.9, fill_color=WHITE, stroke_width=1, stroke_color=GRAY)
            num = MathTex(str(i), font_size=18)
            num.move_to(sq.get_center())
            cell = VGroup(sq, num)
            numbers_grid.add(cell)

        numbers_grid.arrange_in_grid(rows=3, cols=10, buff=0.1)
        numbers_grid.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.6)

        with self.voiceover(
            text=get_phonetic_text("Modern sieve methods are more sophisticated. "
                 "Instead of crossing out numbers one by one, "
                 "we assign weights to integers that are designed "
                 "to be large on primes and small on composites."),
            subcaption="Modern sieve methods are more sophisticated. "
                 "Instead of crossing out numbers one by one, "
                 "we assign weights to integers that are designed "
                 "to be large on primes and small on composites."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(modern), run_time=1.0)
            self.play(FadeIn(weight_note, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(numbers_grid), run_time=1.0)

            primes_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
            for idx in range(30):
                n = idx + 1
                cell = numbers_grid[idx]
                sq = cell[0]
                num = cell[1]
                if n in primes_set:
                    self.play(
                        sq.animate.set_fill(YELLOW, opacity=1.0),
                        num.animate.set_color(BLACK),
                        run_time=0.08,
                    )
                else:
                    self.play(
                        sq.animate.set_fill(DARK_GRAY, opacity=0.7),
                        run_time=0.08,
                    )

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The goal is to count how many primes survive the sieve, "
                 "or in our case, how many pairs of integers "
                 "are simultaneously prime."),
            subcaption="The goal is to count how many primes survive the sieve, "
                 "or in our case, how many pairs of integers "
                 "are simultaneously prime."
        ):
            self.play(FadeIn(goal_note, shift=RIGHT * 0.3), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 5a: Admissible Tuples — Definition
    # ------------------------------------------------------------------
    def admissible_tuples_part1(self):
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

        content = VGroup(motivation, bad_example, def_text, cond_text)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        content.next_to(header, DOWN, buff=0.5).set_x(0)
        center_mathtex(content)

        # Bad tuple {0,1} mod 2: hits all classes - use VGroup for proper spacing
        bad_mod2_label = Tex(r"$\{0,1\} \bmod 2$:", font_size=22)

        def make_residue_classes(p, hits, size=0.3):
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

        bad_mod2_circles = make_residue_classes(2, {0, 1}, size=0.25)
        bad_mod2_group = VGroup(bad_mod2_label, bad_mod2_circles)
        bad_mod2_group.arrange(RIGHT, buff=0.3)
        bad_mod2_group.set_x(0).next_to(bad_example, DOWN, buff=0.4)

        with self.voiceover(
            text=get_phonetic_text("Now we come to a central concept: admissible tuples. "
                 "Why do we need this notion? "
                 "If you want to find two primes at a fixed distance, "
                 "say distance two, "
                 "you need to make sure there is no obvious obstruction."),
            subcaption="Now we come to a central concept: admissible tuples. "
                 "Why do we need this notion? "
                 "If you want to find two primes at a fixed distance, "
                 "say distance two, "
                 "you need to make sure there is no obvious obstruction."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(motivation), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("For example, if you look at n and n plus one, "
                 "modulo two they are zero and one. "
                 "They hit both residue classes, "
                 "so one of them is always even, "
                 "and they cannot both be prime except for the pair two and three."),
            subcaption="For example, if you look at n and n plus one, "
                 "modulo two they are zero and one. "
                 "They hit both residue classes, "
                 "so one of them is always even, "
                 "and they cannot both be prime except for the pair two and three."
        ):
            self.play(FadeIn(bad_example), run_time=1.5)
            self.play(FadeIn(bad_mod2_group), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("An admissible tuple is a set of shifts "
                 "that avoids this kind of obstruction for every prime. "
                 "Formally, a set H is admissible if for every prime p, "
                 "the elements of H do not cover all residue classes modulo p."),
            subcaption="An admissible tuple is a set of shifts "
                 "that avoids this kind of obstruction for every prime. "
                 "Formally, a set H is admissible if for every prime p, "
                 "the elements of H do not cover all residue classes modulo p."
        ):
            self.play(FadeOut(bad_mod2_group), run_time=0.5)
            self.play(FadeIn(def_text), run_time=1.5)
            self.play(FadeIn(cond_text), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 5b: Admissible Tuples — Example with residue classes
    # ------------------------------------------------------------------
    def admissible_tuples_part2(self):
        header = Tex(
            r"\textbf{Admissible Tuples}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        # Left column: text descriptions - use VGroup for proper arrangement
        left_items = VGroup(
            Tex(
                r"Good: $\mathcal{H} = \{0, 2, 6\}$",
                font_size=30,
                color=GREEN,
            ),
            Tex(
                r"$\bmod 2$: $\{0, 0, 0\}$ — 1 of 2 classes",
                font_size=22,
                color=TEAL,
            ),
            Tex(
                r"$\bmod 3$: $\{0, 2, 0\}$ — 2 of 3 classes",
                font_size=22,
                color=TEAL,
            ),
            Tex(
                r"$\bmod 5$: $\{0, 2, 1\}$ — 3 of 5 classes",
                font_size=22,
                color=TEAL,
            ),
        )
        left_items.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        left_items.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Right column: residue class visualizations (stacked vertically, centered on right half)
        def make_residue_classes(p, hits, size=0.3):
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
            group.arrange(RIGHT, buff=0.1)
            return group

        # Stack residue visuals vertically on the right half
        good_mod2_label = Tex(r"$\{0,2,6\} \bmod 2$:", font_size=18)
        good_mod2_circles = make_residue_classes(2, {0}, size=0.3)
        good_mod2_group = VGroup(good_mod2_label, good_mod2_circles)
        good_mod2_group.arrange(RIGHT, buff=0.2)

        good_mod3_label = Tex(r"$\{0,2,6\} \bmod 3$:", font_size=18)
        good_mod3_circles = make_residue_classes(3, {0, 2}, size=0.25)
        good_mod3_group = VGroup(good_mod3_label, good_mod3_circles)
        good_mod3_group.arrange(RIGHT, buff=0.2)

        good_mod5_label = Tex(r"$\{0,2,6\} \bmod 5$:", font_size=18)
        good_mod5_circles = make_residue_classes(5, {0, 1, 2}, size=0.2)
        good_mod5_group = VGroup(good_mod5_label, good_mod5_circles)
        good_mod5_group.arrange(RIGHT, buff=0.2)

        # Stack vertically on right side
        right_stack = VGroup(good_mod2_group, good_mod3_group, good_mod5_group)
        right_stack.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        right_stack.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.8)

        with self.voiceover(
            text=get_phonetic_text("For example, the tuple zero, two, six is admissible. "
                 "Modulo two, all three elements are zero, "
                 "so they only hit one residue class."),
            subcaption="For example, the tuple zero, two, six is admissible. "
                 "Modulo two, all three elements are zero, "
                 "so they only hit one residue class."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(left_items[0]), run_time=0.8)
            self.play(FadeIn(good_mod2_label), FadeIn(good_mod2_circles), run_time=1.0)
            self.play(FadeIn(left_items[1]), run_time=0.8)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Modulo three, they hit zero and two, missing the class one. "
                 "So there is no local obstruction to all three "
                 "being prime simultaneously."),
            subcaption="Modulo three, they hit zero and two, missing the class one. "
                 "So there is no local obstruction to all three "
                 "being prime simultaneously."
        ):
            self.play(FadeIn(good_mod3_label), FadeIn(good_mod3_circles), run_time=1.0)
            self.play(FadeIn(left_items[1]), run_time=0.8)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Modulo five, they hit zero, one, and two — three out of five classes. "
                 "Again, no obstruction."),
            subcaption="Modulo five, they hit zero, one, and two — three out of five classes. "
                 "Again, no obstruction."
        ):
            self.play(FadeIn(good_mod5_label), FadeIn(good_mod5_circles), run_time=1.0)
            self.play(FadeIn(left_items[2]), run_time=0.8)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 6a: GPY Sieve Method — Idea and weighted sum
    # ------------------------------------------------------------------
    def gpy_sieve_method_part1(self):
        header = Tex(
            r"\textbf{The GPY Sieve Method}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        idea = Tex(
            r"Weight integers by how ``prime-rich'' they are",
            font_size=26,
            color=TEAL,
        )
        idea.next_to(header, DOWN, buff=0.4)

        sum_label = Tex(r"Weighted sum:", font_size=24)
        sum_eq = MathTex(
            r"S = \sum_{n \leq x} \left( \sum_{i=1}^{k} \Lambda(n + h_i) - \rho \right) w(n)^2",
            font_size=22,
        )

        left_group = VGroup(sum_label, sum_eq)
        left_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        lambda_def = MathTex(r"\Lambda(n) = \begin{cases} \log p & n = p^m \\ 0 & \text{otherwise} \end{cases}", font_size=20)
        lambda_label = Tex(r"von Mangoldt", font_size=18, color=GRAY)

        weight_def = MathTex(r"w(n) = \sum_{d \mid P(n)} \lambda_d", font_size=20)
        weight_label = Tex(r"sieve weight", font_size=18, color=GRAY)

        rho_def = MathTex(r"\rho = \text{threshold}", font_size=20)
        rho_label = Tex(r"$S>0 \Rightarrow >\rho$ primes", font_size=18, color=GREEN)

        right_group = VGroup(
            VGroup(lambda_def, lambda_label),
            VGroup(weight_def, weight_label),
            VGroup(rho_def, rho_label),
        )
        for item in right_group:
            item.arrange(RIGHT, buff=0.2)
        right_group.arrange(DOWN, buff=0.4)

        main_content = VGroup(left_group, right_group)
        main_content.arrange(RIGHT, buff=1.8)
        main_content.next_to(idea, DOWN, buff=0.5)

        with self.voiceover(
            text=get_phonetic_text("The G P Y method, named after Goldston, Pintz, and Yildirim, "
                 "is the starting point for Zhang's work. "
                 "Here is the key idea."),
            subcaption="The G P Y method, named after Goldston, Pintz, and Yildirim, "
                 "is the starting point for Zhang's work. "
                 "Here is the key idea."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(idea), run_time=1.5)

        self.wait(1.0)

        with self.voiceover(
            text=get_phonetic_text("Instead of looking at individual primes, "
                 "we look at a weighted sum over integers n, "
                 "where the weight is designed to be large "
                 "when many of the shifted values n plus h i "
                 "are simultaneously prime."),
            subcaption="Instead of looking at individual primes, "
                 "we look at a weighted sum over integers n, "
                 "where the weight is designed to be large "
                 "when many of the shifted values n plus h i "
                 "are simultaneously prime."
        ):
            self.play(FadeIn(left_group), run_time=2.5)

        self.wait(1.0)

        with self.voiceover(
            text=get_phonetic_text("Let us break down each piece. "
                 "Lambda is the von Mangoldt function: "
                 "it equals log p when n is a prime power, and zero otherwise. "
                 "So it detects primes."),
            subcaption="Let us break down each piece. "
                 "Lambda is the von Mangoldt function: "
                 "it equals log p when n is a prime power, and zero otherwise. "
                 "So it detects primes."
        ):
            self.play(FadeIn(lambda_def), run_time=1.5)
            self.play(FadeIn(lambda_label), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("w of n is a sieve weight, "
                 "a sum over divisors of the product of all shifts. "
                 "The coefficients are chosen to optimize the sum."),
            subcaption="w of n is a sieve weight, "
                 "a sum over divisors of the product of all shifts. "
                 "The coefficients are chosen to optimize the sum."
        ):
            self.play(FadeIn(weight_def), run_time=1.5)
            self.play(FadeIn(weight_label), run_time=0.8)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Rho is a threshold parameter. "
                 "If the weighted sum is positive, "
                 "it means more than rho of the shifts are prime for some n. "
                 "By choosing rho carefully, "
                 "one can guarantee at least two shifts are prime simultaneously."),
            subcaption="Rho is a threshold parameter. "
                 "If the weighted sum is positive, "
                 "it means more than rho of the shifts are prime for some n. "
                 "By choosing rho carefully, "
                 "one can guarantee at least two shifts are prime simultaneously."
        ):
            self.play(FadeIn(rho_def), run_time=1.5)
            self.play(FadeIn(rho_label), run_time=0.8)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 6b: GPY Sieve Method — Conclusion and takeaway
    # ------------------------------------------------------------------
    def gpy_sieve_method_part2(self):
        header = Tex(
            r"\textbf{The GPY Sieve Method}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        conclusion = MathTex(
            r"S > 0 \implies \exists\, n \text{ with } > \rho \text{ primes among } \{n+h_i\}",
            font_size=24,
            color=GREEN,
        )
        takeaway = Tex(
            r"Set $\rho = 1$ to guarantee two primes simultaneously",
            font_size=22,
            color=TEAL,
        )
        barrier_note = Tex(
            r"But proving $S > 0$ requires $\theta > 1/2$",
            font_size=20,
            color=RED,
        )

        content = VGroup(conclusion, takeaway, barrier_note)
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)

        with self.voiceover(
            text=get_phonetic_text("So the conclusion is clear. "
                 "If we can make this weighted sum positive, "
                 "then there exists some n where more than rho of the shifts are prime."),
            subcaption="So the conclusion is clear. "
                 "If we can make this weighted sum positive, "
                 "then there exists some n where more than rho of the shifts are prime."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(conclusion), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("By setting rho equal to one, "
                 "we guarantee that at least two shifts are prime simultaneously, "
                 "which gives bounded gaps."),
            subcaption="By setting rho equal to one, "
                 "we guarantee that at least two shifts are prime simultaneously, "
                 "which gives bounded gaps."
        ):
            self.play(FadeIn(takeaway), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("But proving the sum is positive "
                 "requires the level of distribution theta to exceed one-half, "
                 "and that was the barrier no one could break."),
            subcaption="But proving the sum is positive "
                 "requires the level of distribution theta to exceed one-half, "
                 "and that was the barrier no one could break."
        ):
            self.play(FadeIn(barrier_note), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 7a: Level of Distribution — Arithmetic progressions
    # ------------------------------------------------------------------
    def level_of_distribution_part1(self):
        header = Tex(
            r"\textbf{Level of Distribution}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        ap_label = Tex(
            r"\textbf{Arithmetic progressions:} $a, a+q, a+2q, \dots$",
            font_size=24,
        )

        dirichlet_note = Tex(
            r"Dirichlet: each class has infinitely many primes",
            font_size=18,
            color=GRAY,
        )

        intuition_note = Tex(
            r"Primes split roughly evenly among the $\phi(q)$ classes",
            font_size=18,
            color=TEAL,
        )

        left_content = VGroup(ap_label, dirichlet_note, intuition_note)
        left_content.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        left_content.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Right side: residue class buckets mod 7
        q = 7
        coprime_classes = [1, 2, 3, 4, 5, 6]
        primes_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]

        buckets = VGroup()
        bucket_labels = VGroup()
        bucket_counts = VGroup()
        bucket_dots = VGroup()
        bar_colors = [BLUE, GREEN, YELLOW, TEAL, PURPLE, MAROON]

        for i, a in enumerate(coprime_classes):
            container = Rectangle(width=0.5, height=2.8, fill_color=BLACK, fill_opacity=0, stroke_width=2, stroke_color=GRAY)
            container.move_to([i * 0.7 - 1.8, 0, 0])
            buckets.add(container)

            lbl = MathTex(f"{a}", font_size=18)
            lbl.next_to(container, DOWN, buff=0.1)
            bucket_labels.add(lbl)

            cnt = Tex("0", font_size=14, color=bar_colors[i])
            cnt.next_to(container, UP, buff=0.05)
            bucket_counts.add(cnt)

        bucket_title = Tex(r"Primes mod $7$", font_size=18, color=GRAY)
        bucket_title.next_to(buckets, UP, buff=0.3)

        right_content = VGroup(bucket_title, buckets, bucket_labels, bucket_counts)
        right_content.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.8)

        dirichlet_eq = MathTex(
            r"\pi(x;q,a) \approx \frac{\pi(x)}{\phi(q)}",
            font_size=28,
        )
        dirichlet_card, dirichlet_rect, dirichlet_content = make_theorem_card(
            dirichlet_eq,
            color=GREEN,
            buff=0.3,
        )
        dirichlet_card.next_to(header, DOWN, buff=0.8).set_x(0)

        with self.voiceover(
            text=get_phonetic_text("To make the G P Y sum positive, "
                 "we need to understand how primes are distributed "
                 "in arithmetic progressions. "
                 "An arithmetic progression is a sequence like "
                 "A, A-plus q, A-plus two q, and so on."),
            subcaption="To make the G P Y sum positive, "
                 "we need to understand how primes are distributed "
                 "in arithmetic progressions. "
                 "An arithmetic progression is a sequence like "
                 "a, a plus q, a plus two q, and so on."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(left_content[0]), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Dirichlet's theorem tells us that each such progression "
                 "contains infinitely many primes. "
                 "But here is the key intuition: "
                 "primes behave almost like random numbers modulo q. "
                 "They spread out roughly evenly "
                 "among the phi of q residue classes that are coprime to q."),
            subcaption="Dirichlet's theorem tells us that each such progression "
                 "contains infinitely many primes. "
                 "But here is the key intuition: "
                 "primes behave almost like random numbers modulo q. "
                 "They spread out roughly evenly "
                 "among the phi of q residue classes that are coprime to q."
        ):
            self.play(FadeIn(left_content[1]), run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(buckets), FadeIn(bucket_labels), FadeIn(bucket_title), run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(left_content[2]), run_time=1.5)

        self.wait(0.5)

        # Animate primes falling into buckets
        with self.voiceover(
            text=get_phonetic_text("Watch what happens as primes arrive. "
                 "Each prime falls into one of the six residue classes modulo seven. "
                 "At first the counts are uneven, "
                 "but as more primes come in, "
                 "the buckets fill up at nearly the same rate. "
                 "This is the prime number theorem for arithmetic progressions: "
                 "each class gets approximately one over phi of q of all the primes."),
            subcaption="Watch what happens as primes arrive. "
                 "Each prime falls into one of the six residue classes modulo seven. "
                 "At first the counts are uneven, "
                 "but as more primes come in, "
                 "the buckets fill up at nearly the same rate. "
                 "This is the prime number theorem for arithmetic progressions: "
                 "each class gets approximately one over phi of q of all the primes."
        ):
            counts = [0] * len(coprime_classes)
            for p in primes_up_to_100:
                if p % q in coprime_classes:
                    idx = coprime_classes.index(p % q)
                    counts[idx] += 1

                    # Create a small dot for this prime
                    dot = Dot(radius=0.04, color=bar_colors[idx])
                    dot.move_to(buckets[idx].get_center() + DOWN * 0.8 + UP * (counts[idx] - 1) * 0.12)

                    # Update count label
                    new_cnt = Tex(str(counts[idx]), font_size=18, color=bar_colors[idx])
                    new_cnt.move_to(bucket_counts[idx].get_center())

                    self.play(
                        FadeIn(dot, scale=0.5),
                        ReplacementTransform(bucket_counts[idx], new_cnt),
                        run_time=0.15,
                    )
                    bucket_counts[idx] = new_cnt

            self.wait(0.5)
            self.play(FadeIn(dirichlet_card), run_time=2.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 7b: Level of Distribution — Theta definition
    # ------------------------------------------------------------------
    def level_of_distribution_part2(self):
        header = Tex(
            r"\textbf{Level of Distribution}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        error_label = Tex(
            r"\textbf{Error term:}",
            font_size=26,
        )
        error_def = MathTex(
            r"E(x;q,a) = \pi(x;q,a) - \frac{\pi(x)}{\phi(q)}",
            font_size=22,
        )
        error_note = Tex(
            r"Deviation from the expected count",
            font_size=18,
            color=GRAY,
        )
        error_content = VGroup(error_label, error_def, error_note)
        error_content.arrange(DOWN, buff=0.15)
        error_content.next_to(header, DOWN, buff=0.4)

        theta_label = Tex(
            r"\textbf{Level of distribution $\theta$:}",
            font_size=26,
        )
        theta_def = MathTex(
            r"\theta = \sup \left\{ \vartheta : \sum_{q \leq x^\vartheta} "
            r"\max_a |E(x;q,a)| \text{ is small} \right\}",
            font_size=18,
        )
        theta_note = Tex(
            r"Average error over all moduli $q$ up to $x^\vartheta$",
            font_size=16,
            color=GRAY,
        )
        theta_content = VGroup(theta_label, theta_def, theta_note)
        theta_content.arrange(DOWN, buff=0.15)

        imp1 = Tex(
            r"Larger $\theta$ $\Rightarrow$ control over larger moduli",
            font_size=20,
            color=TEAL,
        )
        imp2 = Tex(
            r"$\theta > 1/2$ $\Rightarrow$ bounded prime gaps",
            font_size=20,
            color=GREEN,
        )
        imp_group = VGroup(imp1, imp2)
        imp_group.arrange(DOWN, buff=0.2)

        importance_box = RoundedRectangle(
            width=5.5, height=1.2, corner_radius=0.15,
            color=TEAL, fill_opacity=0.08, stroke_width=2,
        )
        importance_box.set_width(imp_group.get_width() + 0.6)
        importance_box.set_height(imp_group.get_height() + 0.4)
        importance_box.next_to(theta_content, DOWN, buff=0.4)
        imp_group.move_to(importance_box.get_center())

        main_content = VGroup(error_content, theta_content, importance_box)
        main_content.arrange(DOWN, buff=0.35)
        main_content.set_x(0)

        with self.voiceover(
            text=get_phonetic_text("Now we can define the level of distribution precisely. "
                 "The error term E of x comma q comma a "
                 "measures the deviation between the actual count of primes "
                 "in the progression a mod q "
                 "and the expected count pi of x over phi of q."),
            subcaption="Now we can define the level of distribution precisely. "
                 "The error term E of x comma q comma a "
                 "measures the deviation between the actual count of primes "
                 "in the progression a mod q "
                 "and the expected count pi of x over phi of q."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.5)
            self.play(FadeIn(error_label), run_time=1.0)
            self.play(FadeIn(error_def), run_time=2.0)
            self.play(FadeIn(error_note), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The level of distribution theta "
                 "is the largest exponent such that "
                 "the average error, summed over all moduli q up to x to the theta, "
                 "remains small compared to x. "
                 "In other words, how far can we push q "
                 "before the approximation breaks down?"),
            subcaption="The level of distribution theta "
                 "is the largest exponent such that "
                 "the average error, summed over all moduli q up to x to the theta, "
                 "remains small compared to x. "
                 "In other words, how far can we push q "
                 "before the approximation breaks down?"
        ):
            self.play(FadeIn(theta_label), run_time=1.0)
            self.play(FadeIn(theta_def), run_time=2.5)
            self.play(FadeIn(theta_note), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("If theta is larger, we can control the error "
                 "for larger moduli, and the sieve becomes more powerful. "
                 "And if theta exceeds one-half, "
                 "we get bounded prime gaps."),
            subcaption="If theta is larger, we can control the error "
                 "for larger moduli, and the sieve becomes more powerful. "
                 "And if theta exceeds one-half, "
                 "we get bounded prime gaps."
        ):
            self.play(Create(importance_box), run_time=1.0)
            self.play(FadeIn(imp1), run_time=1.5)
            self.play(FadeIn(imp2), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 8a: GPY Sieve Barrier — The problem and BV theorem
    # ------------------------------------------------------------------
    def gpy_barrier_part1(self):
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

        with self.voiceover(
            text=get_phonetic_text("Here is the problem. "
                 "The G P Y method needs a level of distribution "
                 "strictly greater than one-half to prove bounded gaps."),
            subcaption="Here is the problem. "
                 "The G P Y method needs a level of distribution "
                 "strictly greater than one-half to prove bounded gaps."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(req_text), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("But the best known result is the Bombieri Vinogradov theorem, "
                 "which gives exactly one-half. "
                 "Let us understand what this theorem says. "
                 "It bounds the average error in the prime number theorem "
                 "for arithmetic progressions, "
                 "summed over all moduli q up to x to the theta."),
            subcaption="But the best known result is the Bombieri Vinogradov theorem, "
                 "which gives exactly one-half. "
                 "Let us understand what this theorem says. "
                 "It bounds the average error in the prime number theorem "
                 "for arithmetic progressions, "
                 "summed over all moduli q up to x to the theta."
        ):
            self.play(FadeIn(bv_text), run_time=1.0)
            self.play(FadeIn(bv_formula), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The error term is small compared to x divided by any power of log x, "
                 "but only when theta is at most one-half."),
            subcaption="The error term is small compared to x divided by any power of log x, "
                 "but only when theta is at most one-half."
        ):
            self.play(FadeIn(barrier), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 8b: GPY Sieve Barrier — Theta scale visualization
    # ------------------------------------------------------------------
    def gpy_barrier_part2(self):
        header = Tex(
            r"\textbf{The GPY Barrier}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        note = Tex(
            r"This was the fundamental barrier that blocked progress for years.",
            font_size=24,
            color=RED,
        )
        note.next_to(header, DOWN, buff=0.4).set_x(0)

        # Visual: theta scale — reduced length to fit better
        theta_line = NumberLine(
            x_range=[0, 1, 0.5],
            length=6,
            include_ticks=True,
            include_numbers=True,
            font_size=32,
        ).shift(DOWN * 0.3)

        # Half barrier line
        half_mark = DashedLine(
            start=theta_line.n2p(0.5) + UP * 1.8,
            end=theta_line.n2p(0.5) + DOWN * 1.8,
            color=RED,
            stroke_width=3,
            dash_length=0.1,
        )
        half_label = Tex(r"$\theta = 1/2$", font_size=28, color=RED)
        half_label.next_to(half_mark, UP, buff=0.1)

        # BV region — below the line
        bv_rect = Rectangle(
            width=3.0,
            height=0.5,
            fill_color=BLUE,
            fill_opacity=0.15,
            stroke_color=BLUE,
            stroke_width=2,
        )
        bv_rect.move_to(theta_line.n2p(0.25) + DOWN * 1.2)
        bv_label = Tex(r"Bombieri--Vinogradov", font_size=22, color=BLUE)
        bv_label.move_to(bv_rect.get_center())

        # GPY region — above the line
        gpy_rect = Rectangle(
            width=2.8,
            height=0.5,
            fill_color=GREEN,
            fill_opacity=0.15,
            stroke_color=GREEN,
            stroke_width=2,
        )
        gpy_rect.move_to(theta_line.n2p(0.75) + UP * 1.2)
        gpy_label = Tex(r"GPY needs this", font_size=22, color=GREEN)
        gpy_label.move_to(gpy_rect.get_center())

        # Delta gap indicator
        gap_brace = Brace(
            VGroup(
                Dot(theta_line.n2p(0.5)),
                Dot(theta_line.n2p(0.533)),
            ),
            direction=UP,
            color=YELLOW,
        )
        gap_label = Tex(r"$\delta$", font_size=22, color=YELLOW)
        gap_label.next_to(gap_brace, UP, buff=0.1)

        with self.voiceover(
            text=get_phonetic_text("The G P Y method was powerful enough to reduce bounded gaps "
                 "to this distribution problem, "
                 "but it could not break past the one-half threshold on its own."),
            subcaption="The G P Y method was powerful enough to reduce bounded gaps "
                 "to this distribution problem, "
                 "but it could not break past the one-half threshold on its own."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(note), run_time=1.0)
            self.play(Create(theta_line), run_time=1.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("The Bombieri Vinogradov theorem gives us everything up to one-half, "
                 "but GPY needs just a tiny bit more — some delta beyond one-half."),
            subcaption="The Bombieri Vinogradov theorem gives us everything up to one-half, "
                 "but GPY needs just a tiny bit more — some delta beyond one-half."
        ):
            self.play(Create(half_mark), Write(half_label), run_time=1.5)
            self.wait(0.3)
            self.play(FadeIn(bv_rect), FadeIn(bv_label), run_time=1.5)
            self.wait(0.3)
            self.play(FadeIn(gpy_rect), FadeIn(gpy_label), run_time=1.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("This tiny gap was the barrier that blocked progress for years."),
            subcaption="This tiny gap was the barrier that blocked progress for years."
        ):
            self.play(Create(gap_brace), FadeIn(gap_label), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 9: Zhang's Proof Roadmap
    # ------------------------------------------------------------------
    def zhang_roadmap(self):
        header = Tex(
            r"\textbf{Zhang's Proof Roadmap}",
            font_size=38,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step_colors = [BLUE, TEAL, GOLD, GREEN]
        steps_data = [
            ("Step 1", r"Restrict to smooth moduli", r"Only $q$ with prime factors $\leq x^\delta$"),
            ("Step 2", r"Type I / Type II decomposition", r"Split error terms by convolution structure"),
            ("Step 3", r"Deligne's bound on Kloosterman sums", r"Deep result from algebraic geometry"),
            ("Step 4", r"Distribution level $\theta = 1/2 + \delta$", r"$\delta \approx 1/584$"),
        ]

        step_mobs = []
        for i, (label, name, desc) in enumerate(steps_data):
            box = RoundedRectangle(
                width=6.0, height=1.0, corner_radius=0.15,
                color=step_colors[i],
                fill_opacity=0.12,
                stroke_width=2,
            )
            lab = Tex(
                rf"$\bullet$ \textbf{{{label}:}} {name}",
                font_size=24,
                color=step_colors[i],
            )
            d = Tex(desc, font_size=20, color=GRAY)
            content = VGroup(lab, d).arrange(DOWN, buff=0.1)
            content.move_to(box.get_center())
            step_mobs.append(VGroup(box, content))

        roadmap = VGroup(*step_mobs).arrange(DOWN, buff=0.35)
        roadmap.next_to(header, DOWN, buff=0.5)
        roadmap.set_x(0)

        # Arrows between steps
        arrows = VGroup()
        for i in range(len(step_mobs) - 1):
            a = Arrow(
                step_mobs[i].get_bottom(),
                step_mobs[i + 1].get_top(),
                buff=0.05,
                color=WHITE,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15,
            )
            arrows.add(a)

        with self.voiceover(
            text=get_phonetic_text("Zhang's proof follows a clear four-step roadmap."),
            subcaption="Zhang's proof follows a clear four-step roadmap."
        ):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Step one: instead of summing over all moduli q, "
                 "Zhang restricts to smooth moduli. "
                 "A smooth modulus is a number whose prime factors are all small — "
                 "bounded by some tiny power of x. "
                 "This restriction is mild, but it turns out to be crucial."),
            subcaption="Step one: instead of summing over all moduli q, "
                 "Zhang restricts to smooth moduli. "
                 "A smooth modulus is a number whose prime factors are all small — "
                 "bounded by some tiny power of x. "
                 "This restriction is mild, but it turns out to be crucial."
        ):
            self.play(FadeIn(step_mobs[0], shift=RIGHT * 0.3), run_time=1.0)
            self.play(Create(arrows[0]), run_time=0.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Step two: he decomposes the error terms "
                 "into Type one and Type two sums. "
                 "Type one sums have a simple convolution structure, "
                 "while Type two sums are bilinear forms."),
            subcaption="Step two: he decomposes the error terms "
                 "into Type one and Type two sums. "
                 "Type one sums have a simple convolution structure, "
                 "while Type two sums are bilinear forms."
        ):
            self.play(FadeIn(step_mobs[1], shift=RIGHT * 0.3), run_time=1.0)
            self.play(Create(arrows[1]), run_time=0.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Step three: for the Type two sums, "
                 "he applies Deligne's bound on Kloosterman sums. "
                 "This is a deep result from algebraic geometry, "
                 "proved as part of the Weil conjectures."),
            subcaption="Step three: for the Type two sums, "
                 "he applies Deligne's bound on Kloosterman sums. "
                 "This is a deep result from algebraic geometry, "
                 "proved as part of the Weil conjectures."
        ):
            self.play(FadeIn(step_mobs[2], shift=RIGHT * 0.3), run_time=1.0)
            self.play(Create(arrows[2]), run_time=0.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Step four: combining all estimates, "
                 "he shows the distribution level exceeds one-half "
                 "by a tiny amount — delta is approximately one over five hundred eighty-four. "
                 "That tiny gain is enough to break the G P Y barrier."),
            subcaption="Step four: combining all estimates, "
                 "he shows the distribution level exceeds one-half "
                 "by a tiny amount — delta is approximately one over five hundred eighty-four. "
                 "That tiny gain is enough to break the G P Y barrier."
        ):
            self.play(FadeIn(step_mobs[3], shift=RIGHT * 0.3), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 10a: Smooth Moduli — Definition and example
    # ------------------------------------------------------------------
    def zhang_breakthrough_part1(self):
        header = Tex(
            r"\textbf{Step 1: Smooth Moduli}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        # Left: definition
        def_label = Tex(
            r"\textbf{Definition:}",
            font_size=28,
        )

        smooth_def = MathTex(
            r"q \text{ is } y\text{-smooth if } p \mid q \implies p \leq y",
            font_size=22,
        )

        example = Tex(
            r"Example: $12 = 2^2 \cdot 3$ is 3-smooth",
            font_size=22,
            color=TEAL,
        )

        left_content = VGroup(def_label, smooth_def, example)
        left_content.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        left_content.next_to(header, DOWN, buff=0.5).shift(LEFT * 2.2)

        # Right: Zhang's choice
        zhang_label = Tex(
            r"\textbf{Zhang's choice:}",
            font_size=28,
        )

        zhang_choice = MathTex(
            r"y = x^\delta, \quad \delta \approx \frac{1}{584}",
            font_size=24,
        )

        zhang_note = Tex(
            r"Very small, but enough to break the barrier",
            font_size=18,
            color=GRAY,
        )

        right_content = VGroup(zhang_label, zhang_choice, zhang_note)
        right_content.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_content.next_to(header, DOWN, buff=0.5).shift(RIGHT * 2.2)

        with self.voiceover(
            text=get_phonetic_text("Let us look at each step in more detail, "
                 "starting with smooth moduli. "
                 "A number q is called y-smooth "
                 "if all of its prime factors are at most y. "
                 "For example, twelve is three-smooth "
                 "because twelve equals two squared times three."),
            subcaption="Let us look at each step in more detail, "
                 "starting with smooth moduli. "
                 "A number q is called y-smooth "
                 "if all of its prime factors are at most y. "
                 "For example, twelve is three-smooth "
                 "because twelve equals two squared times three."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.3)
            self.play(FadeIn(left_content), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Zhang restricts his sieve sum "
                 "to only include smooth moduli q. "
                 "He chooses y to be x to the power delta, "
                 "where delta is about one over five hundred eighty-four. "
                 "This is a very small exponent, but it is enough."),
            subcaption="Zhang restricts his sieve sum "
                 "to only include smooth moduli q. "
                 "He chooses y to be x to the power delta, "
                 "where delta is about one over five hundred eighty-four. "
                 "This is a very small exponent, but it is enough."
        ):
            self.play(FadeIn(right_content), run_time=2.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 10b: Smooth Moduli — Why this helps
    # ------------------------------------------------------------------
    def zhang_breakthrough_part2(self):
        header = Tex(
            r"\textbf{Step 1: Smooth Moduli}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        why_label = Tex(
            r"\textbf{Why this helps:}",
            font_size=28,
            color=TEAL,
        )

        crt_demo = MathTex(
            r"\mathbb{Z}/12\mathbb{Z} \cong \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}",
            font_size=22,
            color=TEAL,
        )

        benefit1 = Tex(
            r"$\bullet$ CRT factorization: $\mathbb{Z}/q\mathbb{Z} \cong \prod \mathbb{Z}/p_i^{e_i}\mathbb{Z}$",
            font_size=20,
        )
        benefit2 = Tex(
            r"$\bullet$ Kloosterman structure becomes visible",
            font_size=20,
        )
        benefit3 = Tex(
            r"$\bullet$ Error terms become tractable",
            font_size=20,
        )

        content = VGroup(why_label, crt_demo, benefit1, benefit2, benefit3)
        content.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        content.next_to(header, DOWN, buff=0.5)
        content.set_x(0)

        with self.voiceover(
            text=get_phonetic_text("Why does this help? "
                 "When q has only small prime factors, "
                 "the arithmetic structure of q is very special. "
                 "The Chinese Remainder Theorem lets us factor "
                 "problems modulo q "
                 "into problems modulo each prime power dividing q. "
                 "This factorization is the key "
                 "that unlocks the deeper analysis."),
            subcaption="Why does this help? "
                 "When q has only small prime factors, "
                 "the arithmetic structure of q is very special. "
                 "The Chinese Remainder Theorem lets us factor "
                 "problems modulo q "
                 "into problems modulo each prime power dividing q. "
                 "This factorization is the key "
                 "that unlocks the deeper analysis."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(why_label), run_time=0.8)
            self.play(FadeIn(crt_demo), run_time=1.5)
            self.play(FadeIn(benefit1, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(benefit2, shift=RIGHT * 0.3), run_time=1.0)
            self.play(FadeIn(benefit3, shift=RIGHT * 0.3), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 11a: Type I Sums
    # ------------------------------------------------------------------
    def type_sums_part1(self):
        header = Tex(
            r"\textbf{Step 2: Type I and Type II Sums}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        type1_label = Tex(
            r"\textbf{Type I:} one long variable",
            font_size=28,
            color=TEAL,
        )
        
        type1_eq = MathTex(
            r"\sum_{m \sim M} \alpha_m \sum_{n \sim N} \psi(mn)",
            font_size=24,
        )

        type1_cond = MathTex(
            r"M \leq x^{1/2 + \delta}, \quad N = x / M \text{ is long}",
            font_size=20,
            color=GRAY,
        )

        type1_note = Tex(
            r"$\bullet$ Easier: long range gives cancellation",
            font_size=20,
            color=GRAY,
        )

        left_content = VGroup(type1_label, type1_eq, type1_cond, type1_note)
        left_content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        left_content.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Right side: visual bar diagram
        short_bar = Rectangle(height=0.3, width=1.0, fill_color=TEAL, fill_opacity=0.7, stroke_width=1)
        long_bar = Rectangle(height=0.3, width=3.5, fill_color=TEAL, fill_opacity=0.35, stroke_width=1)
        short_label = Tex(r"short $M$", font_size=18)
        long_label = Tex(r"long $N = x/M$", font_size=18)
        short_label.move_to(short_bar)
        long_label.move_to(long_bar)
        type1_vis = VGroup(
            VGroup(short_bar, short_label),
            VGroup(long_bar, long_label),
        )
        type1_vis.arrange(RIGHT, buff=0.3)

        vis_label = Tex(r"Range sizes:", font_size=18, color=GRAY)
        vis_label_above = VGroup(vis_label, type1_vis)
        vis_label_above.arrange(DOWN, buff=0.15)
        vis_label_above.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.8)

        with self.voiceover(
            text=get_phonetic_text("After restricting to smooth moduli, "
                 "Zhang needs to estimate the error terms. "
                 "The error terms come from the difference "
                 "between the actual count of primes "
                 "in arithmetic progressions and the expected count. "
                 "Zhang decomposes these error terms into two types."),
            subcaption="After restricting to smooth moduli, "
                 "Zhang needs to estimate the error terms. "
                 "The error terms come from the difference "
                 "between the actual count of primes "
                 "in arithmetic progressions and the expected count. "
                 "Zhang decomposes these error terms into two types."
        ):
            self.play(Write(header), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Type one sums have the form of a single sum over m, "
                 "where the coefficients alpha sub m are arbitrary "
                 "but the other variable n is long. "
                 "Think of it as a weighted average "
                 "of a sequence psi over a long range. "
                 "These are easier to handle "
                 "because the long variable gives cancellation."),
            subcaption="Type one sums have the form of a single sum over m, "
                 "where the coefficients alpha sub m are arbitrary "
                 "but the other variable n is long. "
                 "Think of it as a weighted average "
                 "of a sequence psi over a long range. "
                 "These are easier to handle "
                 "because the long variable gives cancellation."
        ):
            self.play(FadeIn(left_content), run_time=2.0)
            self.play(FadeIn(vis_label), FadeIn(type1_vis), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 11b: Type II Sums
    # ------------------------------------------------------------------
    def type_sums_part2(self):
        header = Tex(
            r"\textbf{Step 2: Type I and Type II Sums}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        type2_label = Tex(
            r"\textbf{Type II:} bilinear form",
            font_size=28,
            color=GOLD,
        )

        type2_eq = MathTex(
            r"\sum_{m \sim M} \sum_{n \sim N} \alpha_m \beta_n \, \psi(mn)",
            font_size=24,
        )

        type2_cond = MathTex(
            r"x^\delta \leq M, N \leq x^{1/2 + \delta}",
            font_size=20,
            color=GRAY,
        )

        type2_note = Tex(
            r"$\bullet$ Harder: needs Cauchy-Schwarz + Kloosterman",
            font_size=20,
            color=GRAY,
        )

        left_content = VGroup(type2_label, type2_eq, type2_cond, type2_note)
        left_content.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        left_content.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=0.8)

        # Right side: visual bar diagram
        mod_bar1 = Rectangle(height=0.3, width=2.2, fill_color=GOLD, fill_opacity=0.6, stroke_width=1)
        mod_bar2 = Rectangle(height=0.3, width=2.2, fill_color=GOLD, fill_opacity=0.6, stroke_width=1)
        mod_label1 = Tex(r"moderate $M$", font_size=18)
        mod_label2 = Tex(r"moderate $N$", font_size=18)
        mod_label1.move_to(mod_bar1)
        mod_label2.move_to(mod_bar2)
        type2_vis = VGroup(
            VGroup(mod_bar1, mod_label1),
            VGroup(mod_bar2, mod_label2),
        )
        type2_vis.arrange(RIGHT, buff=0.3)

        vis_label = Tex(r"Both moderate:", font_size=18, color=GRAY)
        vis_label_above = VGroup(vis_label, type2_vis)
        vis_label_above.arrange(DOWN, buff=0.15)
        vis_label_above.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.8)

        with self.voiceover(
            text=get_phonetic_text("Type two sums are bilinear. "
                 "Both variables m and n are of moderate size, "
                 "and both have arbitrary coefficients alpha and beta. "
                 "These are harder because neither variable "
                 "is long enough to give easy cancellation. "
                 "But the bilinear structure is precisely what allows us "
                 "to use Cauchy-Schwarz "
                 "and reduce to estimating Kloosterman sums."),
            subcaption="Type two sums are bilinear. "
                 "Both variables m and n are of moderate size, "
                 "and both have arbitrary coefficients alpha and beta. "
                 "These are harder because neither variable "
                 "is long enough to give easy cancellation. "
                 "But the bilinear structure is precisely what allows us "
                 "to use Cauchy-Schwarz "
                 "and reduce to estimating Kloosterman sums."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(left_content), run_time=2.0)
            self.play(FadeIn(vis_label), FadeIn(type2_vis), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 12a: Deligne's Bound — Kloosterman definition
    # ------------------------------------------------------------------
    def deligne_bound_part1(self):
        header = Tex(
            r"\textbf{Step 3: Deligne's Bound on Kloosterman Sums}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        kl_def = MathTex(
            r"K(a, b; p) = \sum_{x \in \mathbb{F}_p^\times} "
            r"e\!\left(\frac{ax + b\overline{x}}{p}\right)",
            font_size=28,
        )
        kl_def.next_to(header, DOWN, buff=0.5)

        linear_label = Tex(r"linear term", font_size=16, color=TEAL)
        inverse_label = Tex(r"mult. inverse", font_size=16, color=GOLD)

        linear_label.next_to(kl_def, UP, buff=0.2)
        inverse_label.next_to(kl_def, DOWN, buff=0.2)
        linear_label.set_x(kl_def.get_x())
        inverse_label.set_x(kl_def.get_x())

        # Trivial bound - simplified
        trivial = MathTex(
            r"\text{Trivial: } |K| \leq p - 1",
            font_size=20,
            color=GRAY,
        )
        trivial.next_to(kl_def, DOWN, buff=0.4)

        # Right: unit circle visualization
        circle = Circle(radius=0.7, color=WHITE, stroke_width=1)
        circle_label = Tex(r"Unit circle", font_size=14, color=GRAY)
        circle_label.next_to(circle, DOWN, buff=0.1)

        angles = [0.3, 1.2, 2.5, 3.8, 4.7, 5.5]
        vec_colors = [RED, BLUE, GREEN, YELLOW, PURPLE, TEAL]
        vectors = VGroup()
        for angle, color in zip(angles, vec_colors):
            arrow = Arrow(
                ORIGIN,
                0.7 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=color,
                stroke_width=2,
                buff=0,
                max_tip_length_to_length_ratio=0.15,
            )
            vectors.add(arrow)

        cancel_note = Tex(r"cancellation", font_size=14, color=TEAL)
        cancel_note.next_to(circle_label, DOWN, buff=0.1)

        vis_group = VGroup(circle, circle_label, vectors, cancel_note)
        vis_group.arrange(DOWN, buff=0.1)
        vis_group.next_to(header, DOWN, buff=0.5).shift(RIGHT * 3.5)

        with self.voiceover(
            text=get_phonetic_text("Now we reach the deepest ingredient of Zhang's proof. "
                 "When estimating Type two sums, after applying Cauchy-Schwarz, "
                 "one encounters exponential sums called Kloosterman sums."),
            subcaption="Now we reach the deepest ingredient of Zhang's proof. "
                 "When estimating Type two sums, after applying Cauchy-Schwarz, "
                 "one encounters exponential sums called Kloosterman sums."
        ):
            self.play(Write(header), run_time=1.5)
            self.play(FadeIn(kl_def), run_time=3.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("A Kloosterman sum is a sum over the multiplicative group "
                 "of a finite field. "
                 "Inside the exponential, we have a linear term a x "
                 "plus b times the multiplicative inverse of x, "
                 "all divided by p."),
             subcaption="A Kloosterman sum is a sum over the multiplicative group "
                 "of a finite field. "
                 "Inside the exponential, we have a linear term a x "
                 "plus b times the multiplicative inverse of x, "
                 "all divided by p."
        ):
            pass

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Each term is a complex number on the unit circle. "
                 "As x varies, these complex numbers point in different directions "
                 "and cancel each other out."),
            subcaption="Each term is a complex number on the unit circle. "
                 "As x varies, these complex numbers point in different directions "
                 "and cancel each other out."
        ):
            # Show cancellation visualization: unit circle with vectors
            circle = Circle(radius=1.0, color=WHITE, stroke_width=1)
            circle_label = Tex(r"Unit circle in $\mathbb{C}$", font_size=16, color=GRAY)
            circle_label.next_to(circle, DOWN, buff=0.15)

            # Create several arrows pointing in different directions
            angles = [0.3, 1.2, 2.5, 3.8, 4.7, 5.5]
            vec_colors = [RED, BLUE, GREEN, YELLOW, PURPLE, TEAL]
            vectors = VGroup()
            for angle, color in zip(angles, vec_colors):
                arrow = Arrow(
                    ORIGIN,
                    1.0 * np.array([np.cos(angle), np.sin(angle), 0]),
                    color=color,
                    stroke_width=2,
                    buff=0,
                    max_tip_length_to_length_ratio=0.15,
                )
                vectors.add(arrow)

            cancel_note = Tex(r"Vectors point in different directions $\Rightarrow$ cancellation", font_size=18, color=TEAL)
            cancel_note.next_to(circle_label, DOWN, buff=0.2)

            vis_group = VGroup(circle, circle_label, vectors, cancel_note)
            vis_group.next_to(header, DOWN, buff=0.5).to_edge(RIGHT, buff=0.8)

            self.play(FadeIn(vis_group), run_time=2.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("This cancellation is what makes the sum much smaller "
                 "than the trivial bound of p minus one. "
                 "The trivial bound would give p minus one, "
                 "since there are p minus one terms each of size one."),
            subcaption="This cancellation is what makes the sum much smaller "
                 "than the trivial bound of p minus one. "
                 "The trivial bound would give p minus one, "
                 "since there are p minus one terms each of size one."
        ):
            self.play(FadeIn(trivial), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 12b: Deligne's Bound — Cauchy-Schwarz to Kloosterman
    # ------------------------------------------------------------------
    def deligne_bound_part2(self):
        header = Tex(
            r"\textbf{Step 3: From Cauchy-Schwarz to Deligne}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        pipeline_label = Tex(
            r"\textbf{The pipeline:}",
            font_size=24,
        )

        type2_reminder = MathTex(
            r"\sum_{m \sim M} \sum_{n \sim N} \alpha_m \beta_n \, \psi(mn)",
            font_size=18,
            color=GOLD,
        )

        cs_label = Tex(
            r"\textbf{Apply Cauchy-Schwarz}",
            font_size=18,
            color=TEAL,
        )

        cs_note = Tex(
            r"Square the sum $\rightarrow$ double sum over $n_1, n_2$",
            font_size=14,
            color=GRAY,
        )

        kl_reduced = MathTex(
            r"\sum_{n_1, n_2} \cdots \sum_{c} K(c, \overline{n_1}n_2; q)",
            font_size=16,
            color=ORANGE,
        )

        kl_note = Tex(
            r"Kloosterman sums appear from congruence",
            font_size=14,
            color=GRAY,
        )

        deligne_result = MathTex(
            r"|K(a, b; q)| \leq \tau(q) \cdot 2\sqrt{q}",
            font_size=18,
            color=GREEN,
        )

        deligne_note = Tex(
            r"Square-root cancellation! Error $\ll q^{1/2+\epsilon}$",
            font_size=14,
            color=GREEN,
        )

        pipeline = VGroup(
            pipeline_label, type2_reminder,
            cs_label, cs_note,
            kl_reduced, kl_note,
            deligne_result, deligne_note,
        )
        pipeline.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        pipeline.next_to(header, DOWN, buff=0.5).to_edge(LEFT, buff=1.2)

        # Right side: visual explanation
        cs_explain_label = Tex(
            r"\textbf{Why Cauchy-Schwarz works:}",
            font_size=24,
            color=TEAL,
        )
        cs_explain_label.set_x(2.5).shift(UP * 2.5)

        cs_idea1 = Tex(
            r"$\bullet$ Squaring creates correlations between shifts",
            font_size=18,
            color=GRAY,
        )
        cs_idea1.next_to(cs_explain_label, DOWN, buff=0.3, aligned_edge=LEFT)

        cs_idea2 = Tex(
            r"$\bullet$ Congruence $m n_1 \equiv m n_2 \pmod q$ forces structure",
            font_size=18,
            color=GRAY,
        )
        cs_idea2.next_to(cs_idea1, DOWN, buff=0.2, aligned_edge=LEFT)

        cs_idea3 = Tex(
            r"$\bullet$ The resulting exponential sums are Kloosterman",
            font_size=18,
            color=GRAY,
        )
        cs_idea3.next_to(cs_idea2, DOWN, buff=0.2, aligned_edge=LEFT)

        cs_idea4 = Tex(
            r"$\bullet$ Deligne bounds each one by $\sqrt{q}$",
            font_size=18,
            color=GREEN,
        )
        cs_idea4.next_to(cs_idea3, DOWN, buff=0.2, aligned_edge=LEFT)

        with self.voiceover(
            text=get_phonetic_text("Now let us see how Cauchy-Schwarz and Deligne work together. "
                 "We start with a Type two sum — a bilinear form with coefficients alpha and beta. "
                 "The key move is to apply Cauchy-Schwarz to eliminate one set of coefficients."),
            subcaption="Now let us see how Cauchy-Schwarz and Deligne work together. "
                 "We start with a Type two sum — a bilinear form with coefficients alpha and beta. "
                 "The key move is to apply Cauchy-Schwarz to eliminate one set of coefficients."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.3)
            self.play(FadeIn(pipeline_label), run_time=0.8)
            self.play(FadeIn(type2_reminder), run_time=2.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Applying Cauchy-Schwarz squares the sum, "
                 "which creates a double sum over two variables n one and n two. "
                 "This eliminates the coefficients alpha sub m "
                 "and forces a congruence relation between n one and n two."),
            subcaption="Applying Cauchy-Schwarz squares the sum, "
                 "which creates a double sum over two variables n one and n two. "
                 "This eliminates the coefficients alpha sub m "
                 "and forces a congruence relation between n one and n two."
        ):
            self.play(FadeIn(cs_label), run_time=1.0)
            self.play(FadeIn(cs_note), run_time=1.0)
            self.play(FadeIn(cs_explain_label), run_time=1.0)
            self.play(FadeIn(cs_idea1), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("The congruence structure that emerges "
                 "is precisely what produces Kloosterman sums. "
                 "These are exponential sums involving a linear term "
                 "and a multiplicative inverse modulo q."),
            subcaption="The congruence structure that emerges "
                 "is precisely what produces Kloosterman sums. "
                 "These are exponential sums involving a linear term "
                 "and a multiplicative inverse modulo q."
        ):
            self.play(FadeIn(kl_reduced), run_time=2.0)
            self.play(FadeIn(kl_note), run_time=1.0)
            self.play(FadeIn(cs_idea2), run_time=1.0)
            self.play(FadeIn(cs_idea3), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("And now Deligne's bound kicks in. "
                 "Each Kloosterman sum is bounded by two times the square root of q, "
                 "up to a small divisor function factor. "
                 "This square-root cancellation is the critical gain "
                 "that makes the entire argument work. "
                 "Without it, the error terms would be too large, "
                 "and Zhang's proof would collapse."),
            subcaption="And now Deligne's bound kicks in. "
                 "Each Kloosterman sum is bounded by two times the square root of q, "
                 "up to a small divisor function factor. "
                 "This square-root cancellation is the critical gain "
                 "that makes the entire argument work. "
                 "Without it, the error terms would be too large, "
                 "and Zhang's proof would collapse."
        ):
            self.play(FadeIn(deligne_result), run_time=2.0)
            self.play(FadeIn(deligne_note), run_time=1.0)
            self.play(FadeIn(cs_idea4), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 13a: Putting It All Together — Steps 1-2
    # ------------------------------------------------------------------
    def putting_it_together_part1(self):
        header = Tex(
            r"\textbf{Putting It All Together}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step1_title = Tex(r"\textbf{(1) Start with the GPY weighted sum}", font_size=24)
        step1_eq = MathTex(r"S = \sum_{n \leq x} \left(\sum_{i=1}^k \Lambda(n+h_i) - \rho\right) w(n)^2", font_size=20)
        step1_goal = Tex(r"Goal: show $S > 0$ for some admissible $\mathcal{H}$", font_size=20)

        step_labels = VGroup(step1_title, step1_eq, step1_goal)
        step_labels.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        step2_title = Tex(r"\textbf{(2) Decompose the error}", font_size=24)
        step2_b1 = Tex(r"Restrict to smooth moduli $q$", font_size=20)
        step2_b2 = Tex(r"Split into Type I sums (one long variable)", font_size=20)
        step2_b3 = Tex(r"Split into Type II sums (bilinear form)", font_size=20)

        step_analysis = VGroup(step2_title, step2_b1, step2_b2, step2_b3)
        step_analysis.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        main_content = VGroup(step_labels, step_analysis)
        main_content.arrange(DOWN, buff=0.5)
        main_content.next_to(header, DOWN, buff=0.5).set_x(0)
        center_mathtex(main_content)

        with self.voiceover(
            text=get_phonetic_text("Now let us see how all the pieces fit together. "
                 "We start with the G P Y weighted sum. "
                 "The goal is to show this sum is positive "
                 "for some admissible tuple H. "
                 "If it is positive, then for some integer n, "
                 "at least two of the shifted values n plus h i are prime."),
            subcaption="Now let us see how all the pieces fit together. "
                 "We start with the G P Y weighted sum. "
                 "The goal is to show this sum is positive "
                 "for some admissible tuple H. "
                 "If it is positive, then for some integer n, "
                 "at least two of the shifted values n plus h i are prime."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(step_labels), run_time=2.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Step two: decompose the error. "
                 "First, we restrict the sum to smooth moduli only. "
                 "This means we only consider q whose prime factors are small."),
            subcaption="Step two: decompose the error. "
                 "First, we restrict the sum to smooth moduli only. "
                 "This means we only consider q whose prime factors are small."
        ):
            self.play(FadeIn(step_analysis[0]), run_time=0.8)
            self.play(FadeIn(step_analysis[1]), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Then we split the remaining error terms "
                 "into Type one sums, where one variable is long, "
                 "and Type two sums, which have a bilinear structure."),
            subcaption="Then we split the remaining error terms "
                 "into Type one sums, where one variable is long, "
                 "and Type two sums, which have a bilinear structure."
        ):
            self.play(FadeIn(step_analysis[2]), run_time=1.0)
            self.play(FadeIn(step_analysis[3]), run_time=1.0)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 13b: Putting It All Together — Step 3
    # ------------------------------------------------------------------
    def putting_it_together_part2(self):
        header = Tex(
            r"\textbf{Putting It All Together}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step3_title = Tex(r"\textbf{(3) Estimate each type}", font_size=24)
        step3_b1 = Tex(r"Type I: use smooth modulus factorization", font_size=20)
        step3_b2 = Tex(r"Type II: Cauchy-Schwarz to Kloosterman sums", font_size=20)
        step3_b3 = Tex(r"Apply Deligne: $|K| \leq 2\sqrt{p}$", font_size=20, color=GREEN)

        step_estimate = VGroup(step3_title, step3_b1, step3_b2, step3_b3)
        step_estimate.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_estimate.next_to(header, DOWN, buff=0.5).set_x(0)

        with self.voiceover(
            text=get_phonetic_text("Step three: estimate each type. "
                 "For Type one sums, the smooth modulus structure "
                 "lets us factor the problem using the Chinese Remainder Theorem, "
                 "and the long variable gives us cancellation."),
            subcaption="Step three: estimate each type. "
                 "For Type one sums, the smooth modulus structure "
                 "lets us factor the problem using the Chinese Remainder Theorem, "
                 "and the long variable gives us cancellation."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(step_estimate[0]), run_time=0.8)
            self.play(FadeIn(step_estimate[1]), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("For Type two sums, we apply Cauchy-Schwarz, "
                 "which reduces the problem to bounding Kloosterman sums. "
                 "And here we use Deligne's bound: "
                 "the absolute value is at most two times the square root of p."),
            subcaption="For Type two sums, we apply Cauchy-Schwarz, "
                 "which reduces the problem to bounding Kloosterman sums. "
                 "And here we use Deligne's bound: "
                 "the absolute value is at most two times the square root of p."
        ):
            self.play(FadeIn(step_estimate[2]), run_time=1.0)
            self.play(FadeIn(step_estimate[3]), run_time=1.5)

        self.wait(1.0)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 13c: Putting It All Together — Step 4 conclusion
    # ------------------------------------------------------------------
    def putting_it_together_part3(self):
        header = Tex(
            r"\textbf{Putting It All Together}",
            font_size=32,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        step4_title = Tex(r"\textbf{(4) Conclusion}", font_size=24)
        step4_theta = MathTex(r"\theta = 1/2 + \delta \quad (\delta \approx 1/584)", font_size=22, color=GREEN)
        step4_pos = Tex(r"$S > 0$ for large enough $k$", font_size=22, color=GREEN)
        step4_inf = Tex(r"Infinitely many $n$ with 2+ primes in $\{n+h_i\}$", font_size=20, color=GREEN)

        step_conclude = VGroup(step4_title, step4_theta, step4_pos, step4_inf)
        step_conclude.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        step_conclude.next_to(header, DOWN, buff=0.5).set_x(0)
        center_mathtex(step_conclude)

        with self.voiceover(
            text=get_phonetic_text("Step four: putting the estimates together, "
                 "we find that the distribution level exceeds one-half "
                 "by a tiny amount delta, about one over five hundred eighty-four."),
            subcaption="Step four: putting the estimates together, "
                 "we find that the distribution level exceeds one-half "
                 "by a tiny amount delta, about one over five hundred eighty-four."
        ):
            self.play(Write(header), run_time=1.0)
            self.play(FadeIn(step_conclude[0]), run_time=0.8)
            self.play(FadeIn(step_conclude[1]), run_time=1.5)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("This is just enough to make the G P Y sum positive, "
                 "which guarantees that there are infinitely many integers n "
                 "such that at least two of the shifts n plus h i are prime."),
            subcaption="This is just enough to make the G P Y sum positive, "
                 "which guarantees that there are infinitely many integers n "
                 "such that at least two of the shifts n plus h i are prime."
        ):
            self.play(FadeIn(step_conclude[2]), run_time=1.5)
            self.play(FadeIn(step_conclude[3]), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Since the tuple is finite, the gap between these two primes "
                 "is bounded by the diameter of the tuple."),
            subcaption="Since the tuple is finite, the gap between these two primes "
                 "is bounded by the diameter of the tuple."
        ):
            self.wait(1.0)

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

        # Individual pieces shown one by one
        piece1 = Tex(
            r"$\bullet$ Smooth moduli: error terms become manageable",
            font_size=22,
            color=TEAL,
        )
        piece2 = Tex(
            r"$\bullet$ Type I/II decomposition: organizes the analysis",
            font_size=22,
            color=TEAL,
        )
        piece3 = Tex(
            r"$\bullet$ Deligne's bound: square-root cancellation",
            font_size=22,
            color=GREEN,
        )
        pieces = VGroup(piece1, piece2, piece3)
        pieces.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        pieces.next_to(card, DOWN, buff=0.5)

        sub_note = Tex(
            r"First finite bound on prime gaps in history",
            font_size=26,
            color=GRAY,
        )
        sub_note.next_to(pieces, DOWN, buff=0.4)

        with self.voiceover(
            text=get_phonetic_text("Putting all the pieces together, "
                 "Zhang proved his main theorem."),
            subcaption="Putting all the pieces together, "
                 "Zhang proved his main theorem."
        ):
            self.play(Write(theorem_title), run_time=1.5)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The smooth moduli restriction makes the error terms manageable."),
            subcaption="The smooth moduli restriction makes the error terms manageable."
        ):
            self.play(FadeIn(content), Create(rect), run_time=2.0)
            self.play(FadeIn(piece1), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("The Type one and Type two decomposition organizes the analysis."),
            subcaption="The Type one and Type two decomposition organizes the analysis."
        ):
            self.play(FadeIn(piece2), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Deligne's bound provides the crucial square-root cancellation "
                 "for the hardest terms."),
            subcaption="Deligne's bound provides the crucial square-root cancellation "
                 "for the hardest terms."
        ):
            self.play(FadeIn(piece3), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("And the result is that the distribution level exceeds one-half "
                 "by a tiny but positive amount. "
                 "This is enough to make the G P Y sum positive, "
                 "which guarantees that some pair of shifts "
                 "is prime infinitely often."),
            subcaption="And the result is that the distribution level exceeds one-half "
                 "by a tiny but positive amount. "
                 "This is enough to make the G P Y sum positive, "
                 "which guarantees that some pair of shifts "
                 "is prime infinitely often."
        ):
            self.play(
                rect.animate.set_stroke(YELLOW, width=6),
                run_time=0.5,
            )
            self.play(
                rect.animate.set_stroke(GREEN, width=4),
                run_time=0.5,
            )

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("The bound he obtained was seventy million. "
                 "This was the first time anyone proved "
                 "that prime gaps are bounded by any finite number."),
            subcaption="The bound he obtained was seventy million. "
                 "This was the first time anyone proved "
                 "that prime gaps are bounded by any finite number."
        ):
            self.play(FadeIn(sub_note), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)

    # ------------------------------------------------------------------
    # Scene 15: Afterstory — Polymath, Maynard, and open problems
    # ------------------------------------------------------------------
    def conclusion_part1(self):
        header = Tex(
            r"\textbf{Afterstory}",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.5)

        left_title = Tex(r"\textbf{Improving the bound:}", font_size=26)
        left_zhang = Tex(r"Zhang (2014): $H \leq 70,\!000,\!000$", font_size=20)
        left_poly = Tex(r"Polymath8: $H \leq 4,\!680$", font_size=20, color=TEAL)
        left_maynard = Tex(r"Maynard (2013): $H \leq 600$", font_size=20, color=GREEN)
        left_combined = Tex(r"Maynard + Zhang: $H \leq 246$", font_size=20, color=GREEN)

        left_items = VGroup(left_title, left_zhang, left_poly, left_maynard, left_combined)
        left_items.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        right_title = Tex(r"\textbf{Where we stand:}", font_size=26)
        right_geh = Tex(r"Under GEH: $H \leq 6$", font_size=20, color=TEAL)
        right_open = MathTex(r"\liminf (p_{n+1} - p_n) = 2", font_size=20, color=YELLOW)
        right_twin = Tex(r"Twin Prime Conjecture remains open", font_size=18, color=GRAY)

        right_items = VGroup(right_title, right_geh, right_open, right_twin)
        right_items.arrange(DOWN, buff=0.25, aligned_edge=LEFT)

        main_content = VGroup(left_items, right_items)
        main_content.arrange(RIGHT, buff=2.0)
        main_content.next_to(header, DOWN, buff=0.5).set_x(0)

        with self.voiceover(
            text=get_phonetic_text("Zhang's result sparked an explosion of activity. "
                 "The Polymath project, a collaborative online effort, "
                 "quickly improved the bound from seventy million "
                 "down to four thousand six hundred eighty."),
            subcaption="Zhang's result sparked an explosion of activity. "
                 "The Polymath project, a collaborative online effort, "
                 "quickly improved the bound from seventy million "
                 "down to four thousand six hundred eighty."
        ):
            self.play(Write(header), run_time=1.5)
            self.wait(0.3)
            self.play(FadeIn(left_items[0]), run_time=0.8)
            self.play(FadeIn(left_items[1]), run_time=1.5)
            self.play(FadeIn(left_items[2]), run_time=1.0)

        self.wait(0.3)

        with self.voiceover(
            text=get_phonetic_text("Then James Maynard, working independently, "
                 "introduced a new sieve method "
                 "that brought the bound down to six hundred, "
                 "and later to two hundred forty-six "
                 "when combined with Zhang's smooth moduli idea."),
            subcaption="Then James Maynard, working independently, "
                 "introduced a new sieve method "
                 "that brought the bound down to six hundred, "
                 "and later to two hundred forty-six "
                 "when combined with Zhang's smooth moduli idea."
        ):
            self.play(FadeIn(left_items[3]), run_time=1.0)
            self.play(FadeIn(left_items[4]), run_time=1.0)

        self.wait(0.5)

        with self.voiceover(
            text=get_phonetic_text("Assuming the Generalized Elliott Halberstam conjecture, "
                 "the bound can be reduced to six. "
                 "But the original Twin Prime Conjecture, "
                 "which claims the gap is exactly two, "
                 "remains wide open."),
            subcaption="Assuming the Generalized Elliott Halberstam conjecture, "
                 "the bound can be reduced to six. "
                 "But the original Twin Prime Conjecture, "
                 "which claims the gap is exactly two, "
                 "remains wide open."
        ):
            self.play(FadeIn(right_items[0]), run_time=1.0)
            self.play(FadeIn(right_items[1]), run_time=1.5)
            self.play(FadeIn(right_items[2]), run_time=2.0)
            self.play(FadeIn(right_items[3]), run_time=1.0)

        self.wait(1.5)
        clear_screen(self)
