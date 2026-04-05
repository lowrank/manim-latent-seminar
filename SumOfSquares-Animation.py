
from manim_voiceover import VoiceoverScene
from kokoro_mv import KokoroService
import numpy as np
import random

from manim import *
from latent_utils import (
    center_mathtex,
    make_content_group,
    make_theorem_card,
    LatentPrelude,
    SEMINAR_BLUE,
)

class RefinedHeltonProof(LatentPrelude, VoiceoverScene):
    def construct(self):
        self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))

        # ==========================================
        # PRELUDE: Latent Seminar branding
        # ==========================================
        self.play_prelude()

        # ==========================================
        # SCENE 0: MOTIVATION — WHY SOS?
        # ==========================================

        # --- Title card ---
        title = Text("Helton's Sum-of-Squares Theorem", color=BLUE, font_size=46)
        subtitle = Text("Annals of Mathematics, 2002", color=GREY_B, font_size=24)
        subtitle.next_to(title, DOWN, buff=0.3)

        with self.voiceover(
            text="Welcome to Latent Seminar! Today we explore a beautiful theorem by John Helton, "
                 "published in the Annals of Mathematics in 2002."
        ):
            self.play(Write(title), FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1)
        self.play(FadeOut(title, subtitle))

        # --- The big question ---
        big_q = Text("The Big Question", color=YELLOW, font_size=40).to_edge(UP, buff=0.6)

        commutative_line = Tex(
            r"In \textbf{commutative} algebra (ordinary variables $x, y, \ldots$):",
            font_size=30
        )
        comm_fact = MathTex(
            r"p(x) \ge 0 \;\forall\, x \in \mathbb{R}"
            r"\quad\stackrel{?}{\Longrightarrow}\quad "
            r"p = \sum_i f_i^2",
            font_size=34, color=RED_B
        )
        comm_note = Tex(
            r"This is \textbf{false} in general! (Motzkin 1967: degree-6 counter-example)",
            font_size=26, color=RED
        )

        nc_line = Tex(
            r"In \textbf{noncommutative} algebra (matrix variables $X_1, X_2, \ldots$):",
            font_size=30
        )
        nc_fact = MathTex(
            r"Q(X) \succeq 0 \;\forall\text{ matrices } X"
            r"\quad\Longrightarrow\quad "
            r"Q = \sum_i p_i^T p_i",
            font_size=34, color=GREEN
        )
        nc_note = Tex(
            r"This is \textbf{true}! \quad (Helton 2002)",
            font_size=26, color=GREEN
        )

        comm_group = VGroup(commutative_line, comm_fact, comm_note).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        nc_group = VGroup(nc_line, nc_fact, nc_note).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        both = VGroup(comm_group, nc_group).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        both.next_to(big_q, DOWN, buff=0.5).set_x(0)
        # Center MathTex in each sub-group
        center_mathtex(comm_group)
        center_mathtex(nc_group)

        with self.voiceover(
            text="Let us start with the big question. In classical, commutative algebra, "
                 "we can ask: if a polynomial is nonnegative everywhere, can we write it as "
                 "a sum of squares? Surprisingly, the answer is no. Motzkin found a "
                 "counter-example in 1967."
        ):
            self.play(Write(big_q))
            self.play(FadeIn(comm_group[0]))
            self.play(Write(comm_fact))
            self.wait(1)
            self.play(FadeIn(comm_note))
        self.wait(1)

        with self.voiceover(
            text="But here is the surprise. In the noncommutative world, where variables "
                 "are matrices that do not commute, the situation is completely different. "
                 "If a symmetric polynomial evaluates to a positive semidefinite matrix for "
                 "every possible matrix input, then it must be a sum of squares. This is "
                 "Helton's theorem, and today we will understand why it is true."
        ):
            self.play(FadeIn(nc_group[0]))
            self.play(Write(nc_fact))
            self.wait(1)
            self.play(FadeIn(nc_note))
            self.play(Circumscribe(nc_fact, color=GREEN, time_width=2))
        self.wait(2)

        self.play(FadeOut(big_q, both))

        # --- Proof roadmap ---
        roadmap_title = Text("Proof Roadmap", color=BLUE, font_size=38).to_edge(UP, buff=0.5)
        steps_data = [
            ("Step 1", "Gram Representation", "Write Q as a quadratic form: $Q = V^T M V$"),
            ("Step 2", "Non-Uniqueness", "The Gram matrix lives on an affine plane $\\mathcal{M}$"),
            ("Step 3", "Krein's Theorem", "Prove $\\mathcal{M}$ intersects the PSD cone"),
            ("Step 4", "Cholesky", "Factor $M = L^T L$ to get the SOS decomposition"),
        ]
        step_mobs = []
        for i, (label, name, desc) in enumerate(steps_data):
            box = RoundedRectangle(
                width=5.5, height=1.1, corner_radius=0.15,
                color=[BLUE, TEAL, GOLD, GREEN][i],
                fill_opacity=0.15, stroke_width=2
            )
            lab = Text(f"{label}: {name}", font_size=24, color=[BLUE, TEAL, GOLD, GREEN][i])
            d = Tex(desc, font_size=20)
            content = VGroup(lab, d).arrange(DOWN, buff=0.12)
            content.move_to(box.get_center())
            step_mobs.append(VGroup(box, content))

        roadmap = VGroup(*step_mobs).arrange(DOWN, buff=0.3).next_to(roadmap_title, DOWN, buff=0.4)

        # Add arrows between steps
        arrows = []
        for i in range(len(step_mobs) - 1):
            a = Arrow(
                step_mobs[i].get_bottom(), step_mobs[i + 1].get_top(),
                buff=0.05, color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.15
            )
            arrows.append(a)

        with self.voiceover(
            text="Before diving in, here is the roadmap. The proof has four main steps. "
                 "First, we represent the polynomial as a quadratic form using a Gram matrix. "
                 "Second, we observe that the Gram matrix is not unique; it lives on an affine plane. "
                 "Third, we use Krein's extension theorem to show this plane intersects the cone "
                 "of positive semidefinite matrices. "
                 "Fourth, we apply Cholesky factorization to recover the sum-of-squares decomposition."
        ):
            self.play(Write(roadmap_title))
            for i, s in enumerate(step_mobs):
                self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.6)
                if i < len(arrows):
                    self.play(Create(arrows[i]), run_time=0.3)
        self.wait(2)

        self.play(FadeOut(roadmap_title, roadmap, *arrows))

        # ==========================================
        # SCENE 1: FOUNDATIONS — KEY DEFINITIONS
        # ==========================================
        scene1_title = Text("Preliminaries", color=BLUE, font_size=40).to_edge(UP, buff=0.5)

        # --- Part A: Non-commutativity ---
        nc_header = Tex(r"\textbf{1. The Free Algebra } $\mathbb{R}\langle X_1, \ldots, X_n \rangle$",
                        font_size=32)
        nc_explain = Tex(
            r"Variables are \textit{formal symbols}; no commutativity assumed.\\",
            r"We can \textit{evaluate} them at real matrices of any size $d$.",
            font_size=26, tex_environment="flushleft"
        )

        mat_label = Tex(r"\textbf{Example with $2 \times 2$ matrices:}", font_size=26, color=GREY_B)
        X1_def = MathTex(
            r"X_1 = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}",
            font_size=30, color=YELLOW
        )
        X2_def = MathTex(
            r"X_2 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}",
            font_size=30, color=YELLOW
        )
        X1X2 = MathTex(
            r"X_1 X_2 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}",
            font_size=30
        )
        X2X1 = MathTex(
            r"X_2 X_1 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}",
            font_size=30
        )
        neq = MathTex(r"\neq", font_size=36, color=RED)

        mats_row1 = VGroup(X1_def, X2_def).arrange(RIGHT, buff=1.0)
        mats_row2 = VGroup(X1X2, neq, X2X1).arrange(RIGHT, buff=0.4)
        mats = VGroup(mat_label, mats_row1, mats_row2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        part_a = VGroup(nc_header, nc_explain, mats).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        part_a.next_to(scene1_title, DOWN, buff=0.5).set_x(0)

        with self.voiceover(
            text="Let us set up the key definitions. First, the free algebra. "
                 "We work with polynomials in formal noncommuting variables "
                 "X 1 through X n. Think of them as placeholder symbols, "
                 "where the order of multiplication matters."
        ):
            self.play(Write(scene1_title))
            self.play(FadeIn(nc_header), FadeIn(nc_explain))
        self.wait(1)

        with self.voiceover(
            text="We can evaluate these symbols at real matrices of any size. "
                 "For example, let X 1 and X 2 be specific 2-by-2 matrices. "
                 "Then X 1 times X 2 gives the matrix with 1 in the top-left, "
                 "while X 2 times X 1 gives the matrix with 1 in the bottom-right. "
                 "These are different! Order matters."
        ):
            self.play(FadeIn(mat_label))
            self.play(Write(mats_row1))
            self.wait(0.5)
            self.play(Write(X1X2))
            self.play(Write(neq), Write(X2X1))
            self.play(Indicate(neq, scale_factor=1.5, color=RED))
        self.wait(2)

        self.play(FadeOut(part_a))

        # --- Part B: PSD ---
        psd_header = Tex(r"\textbf{2. Positive Semidefinite (PSD) Matrices}", font_size=32)
        psd_def = Tex(
            r"A symmetric matrix $W$ is \textbf{positive semidefinite} ($W \succeq 0$) if:",
            font_size=28
        )
        psd_equiv = MathTex(
            r"v^T W\, v \ge 0 \quad \text{for every vector } v",
            font_size=30, color=TEAL
        )
        psd_eigen = Tex(
            r"Equivalently: every entry in the spectrum of $W$ is $\ge 0$.",
            font_size=26, color=GREY_B
        )
        psd_example_label = Tex(r"\textbf{Example:}", font_size=26)
        psd_example = MathTex(
            r"W = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix},"
            r"\quad \lambda_1 = 3,\; \lambda_2 = 1 \;\ge 0"
            r"\quad\Rightarrow\quad W \succeq 0",
            font_size=28, color=YELLOW
        )

        psd_group = VGroup(psd_header, psd_def, psd_equiv, psd_eigen,
                           psd_example_label, psd_example).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        psd_group.next_to(scene1_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(psd_group)

        with self.voiceover(
            text="Second, let us recall positive semidefinite matrices. "
                 "A symmetric matrix W is positive semidefinite, "
                 "written W succeeds or equals zero, if for every vector v, "
                 "the quadratic form v transpose W v is nonnegative. "
                 "Equivalently, every value in its spectrum is nonnegative."
        ):
            self.play(FadeIn(psd_header, psd_def))
            self.play(Write(psd_equiv))
            self.play(FadeIn(psd_eigen))
        self.wait(1)

        with self.voiceover(
            text="For instance, the matrix 2, 1, 1, 2 has spectrum 3 and 1, "
                 "both nonnegative, so it is PSD."
        ):
            self.play(FadeIn(psd_example_label), Write(psd_example))
            self.play(Indicate(psd_example, color=ORANGE))
        self.wait(1)

        self.play(FadeOut(psd_group))

        # --- Part C: Symmetric polynomials ---
        sym_header = Tex(r"\textbf{3. Symmetric NC Polynomials}", font_size=32)
        sym_def = Tex(
            r"A noncommutative polynomial $Q$ is \textbf{symmetric} if $Q = Q^*$,\\",
            r"where ${}^*$ reverses word order and transposes each variable.",
            font_size=26, tex_environment="flushleft"
        )
        sym_example_label = Tex(r"\textbf{Example:}", font_size=26)
        sym_example = MathTex(
            r"Q(X_1, X_2) = X_1^T X_2 + X_2^T X_1",
            font_size=32, color=YELLOW
        )
        sym_check = MathTex(
            r"Q^* = (X_1^T X_2)^T + (X_2^T X_1)^T = X_2^T X_1 + X_1^T X_2 = Q \;\checkmark",
            font_size=28, color=GREEN
        )

        sym_group = VGroup(sym_header, sym_def, sym_example_label, sym_example, sym_check
                           ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        sym_group.next_to(scene1_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(sym_group)

        with self.voiceover(
            text="Third, symmetric noncommutative polynomials. "
                 "A polynomial Q is symmetric if applying the star involution, "
                 "which reverses word order and transposes each variable, "
                 "gives back Q itself."
        ):
            self.play(FadeIn(sym_header, sym_def))
        self.wait(1)

        with self.voiceover(
            text="For example, Q equals X 1 transpose X 2 plus X 2 transpose X 1. "
                 "Taking the star, we swap the order and transpose each factor, "
                 "and we get back the same expression. So Q is symmetric."
        ):
            self.play(FadeIn(sym_example_label), Write(sym_example))
            self.wait(0.5)
            self.play(Write(sym_check))
            self.play(Indicate(sym_check, color=GREEN))
        self.wait(1)

        self.play(FadeOut(sym_group))

        # --- Part D: Main theorem statement ---
        thm_header = Tex(r"\textbf{Helton's Theorem (2002)}", font_size=36, color=GREEN)
        thm_box_text = MathTex(
            r"Q \text{ symmetric}, \quad Q(X_1, \ldots, X_n) \succeq 0 "
            r"\;\forall\, d \in \mathbb{N},\;\forall\, X_i \in \mathbb{R}^{d \times d}",
            font_size=28
        )
        thm_box_text2 = MathTex(
            r"\Longrightarrow \quad Q = \sum_{i=1}^k p_i^* \, p_i "
            r"\quad\text{(a Sum of Squares in the free algebra)}",
            font_size=28, color=GREEN
        )
        thm_card, thm_rect, thm_content = make_theorem_card(thm_box_text, thm_box_text2, color=GREEN)

        thm_note = Tex(
            r"Key point: the decomposition is \textit{algebraic} — "
            r"it holds as a polynomial identity,\\not just for specific matrix sizes.",
            font_size=24, color=GREY_B, tex_environment="flushleft"
        )

        thm_all = VGroup(thm_header, thm_card, thm_note).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        thm_all.next_to(scene1_title, DOWN, buff=0.5).set_x(0)
        # Center the boxed theorem card
        thm_card.set_x(0)

        with self.voiceover(
            text="Now we can state Helton's theorem precisely. "
                 "If Q is a symmetric noncommutative polynomial, "
                 "and Q evaluates to a positive semidefinite matrix "
                 "for all matrix inputs of every size d, "
                 "then Q can be written as a sum of squares "
                 "in the free algebra. That is, Q equals the sum of "
                 "p i star times p i for some polynomials p i."
        ):
            self.play(Write(thm_header))
            self.play(FadeIn(thm_content), Create(thm_rect))
            self.play(Circumscribe(thm_card, color=GREEN, time_width=2))
        self.wait(1)

        with self.voiceover(
            text="Crucially, this is a purely algebraic identity. "
                 "It does not depend on the matrix size; it holds "
                 "as a formal polynomial equation."
        ):
            self.play(FadeIn(thm_note))
        self.wait(2)

        self.play(FadeOut(scene1_title, thm_all))

        # ==========================================
        # SCENE 2a: THE GRAM REPRESENTATION — Idea & Basis Vector
        # ==========================================
        step1_title = Text("Step 1: The Gram Representation", font_size=36, color=BLUE).to_edge(UP, buff=0.5)

        # --- Intuition first ---
        intuition_text = Tex(
            r"\textbf{Key Idea:} Rewrite $Q(X)$ as a \textit{quadratic form} in noncommuting monomials.",
            font_size=28
        )
        analogy = Tex(
            r"Analogy: just as $ax^2 + bxy + cy^2 = "
            r"\begin{bmatrix} x \\ y \end{bmatrix}^T "
            r"\begin{bmatrix} a & b/2 \\ b/2 & c \end{bmatrix} "
            r"\begin{bmatrix} x \\ y \end{bmatrix}$",
            font_size=26, color=GREY_B
        )

        # --- Basis vector ---
        basis_header = Tex(r"$\bullet$ \textbf{Basis vector } $V(X)$:", font_size=28)
        basis_explain = Tex(
            r"List all noncommutative monomials up to half the degree of $Q$.",
            font_size=26
        )
        basis_example = MathTex(
            r"V(X) = \begin{bmatrix} 1 \\ X_1 \\ X_2 \\ X_1^2 \\ X_1 X_2 \\ \vdots \end{bmatrix}",
            font_size=30, color=TEAL
        )

        step1a_content = VGroup(intuition_text, analogy, basis_header, basis_explain, basis_example
                                ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        step1a_content.next_to(step1_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(step1a_content)

        with self.voiceover(
            text="Step one is the Gram representation. The key idea is to rewrite "
                 "our polynomial Q as a quadratic form in noncommuting monomials. "
                 "This is analogous to how, in commutative algebra, a quadratic polynomial "
                 "in x and y can be written as a vector-matrix-vector product."
        ):
            self.play(Write(step1_title))
            self.play(FadeIn(intuition_text, analogy))
        self.wait(1)

        with self.voiceover(
            text="We build a basis vector V of X, listing all noncommutative monomials "
                 "up to half the degree of Q. For instance, if Q has degree 4, "
                 "V contains monomials of degree up to 2: the identity, X 1, X 2, "
                 "X 1 squared, X 1 X 2, and so on."
        ):
            self.play(FadeIn(basis_header, basis_explain))
            self.play(Write(basis_example))
        self.wait(1)

        self.play(FadeOut(step1a_content))

        # ==========================================
        # SCENE 2b: THE GRAM REPRESENTATION — Gram Matrix
        # ==========================================
        gram_header = Tex(r"$\bullet$ \textbf{Gram matrix } $M_Q$:", font_size=28)
        gram_explain = Tex(
            r"A \textit{real symmetric} matrix of coefficients such that:",
            font_size=26
        )
        eq_gram = MathTex(r"Q(X) = V(X)^T \; M_Q \; V(X)", font_size=38, color=TEAL)
        gram_card, gram_box, _ = make_theorem_card(eq_gram, color=TEAL, buff=0.2, stroke_width=2)

        gram_note = Tex(
            r"Each entry $(M_Q)_{ij}$ is chosen so that expanding $V^T M_Q V$\\",
            r"reproduces every monomial of $Q$ with the correct coefficient.",
            font_size=26, color=GREY_B, tex_environment="flushleft"
        )

        step1b_content = VGroup(
            gram_header, gram_explain,
            gram_card,
            gram_note
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step1b_content.next_to(step1_title, DOWN, buff=0.5).set_x(0)
        # Center the boxed equation
        gram_card.set_x(0)

        with self.voiceover(
            text="Then we find a real symmetric matrix M Q, the Gram matrix, "
                 "such that Q of X equals V transpose times M Q times V. "
                 "Each entry of M Q is chosen so that expanding the product "
                 "reproduces every monomial of Q with the correct coefficient."
        ):
            self.play(FadeIn(gram_header, gram_explain))
            self.play(Write(eq_gram), Create(gram_box))
            self.play(Indicate(gram_card, color=TEAL))
            self.play(FadeIn(gram_note))
        self.wait(1)

        self.play(FadeOut(step1b_content))

        # --- Concrete example part 1 ---
        ex_header = Tex(r"\textbf{Worked Example:}", font_size=30, color=YELLOW)
        ex_poly = MathTex(
            r"Q = X_1 X_1^T + X_1 X_2 + X_2^T X_1^T + 2\, X_2^T X_1^T X_1 X_2",
            font_size=30
        )
        ex_step1_label = Tex(r"Identify monomials up to degree 2:", font_size=26)
        ex_v = MathTex(
            r"V = \begin{bmatrix} 1 \\ X_1^T \\ X_1 X_2 \end{bmatrix}",
            font_size=32, color=TEAL
        )
        ex_step2_label = Tex(r"Find Gram matrix so that $V^T M V = Q$:", font_size=26)
        ex_m = MathTex(
            r"M_Q = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 2 \end{bmatrix}",
            font_size=32, color=TEAL
        )

        ex_group_top = VGroup(
            ex_header, ex_poly, ex_step1_label, ex_v, ex_step2_label, ex_m,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ex_group_top.next_to(step1_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(ex_group_top)

        with self.voiceover(
            text="Let us work through a concrete example. Consider the polynomial "
                 "Q equals X 1 times X 1 transpose, plus X 1 X 2, "
                 "plus X 2 transpose X 1 transpose, plus 2 times X 2 transpose X 1 transpose X 1 X 2."
        ):
            self.play(FadeIn(ex_header))
            self.play(Write(ex_poly))
        self.wait(1)

        with self.voiceover(
            text="First, we identify the monomials. The highest-degree terms are degree 4, "
                 "so we need monomials up to degree 2. We choose V equals the column vector "
                 "with entries 1, X 1 transpose, and X 1 X 2."
        ):
            self.play(FadeIn(ex_step1_label))
            self.play(Write(ex_v))
        self.wait(1)

        with self.voiceover(
            text="Next, we find the Gram matrix. M Q is the 3-by-3 matrix "
                 "with entries 0, 0, 1, 0, 1, 0, 1, 0, 2."
        ):
            self.play(FadeIn(ex_step2_label))
            self.play(Write(ex_m))
        self.wait(1)

        self.play(FadeOut(ex_group_top))

        # --- Concrete example part 2: Verification ---
        ex_verify_label = Tex(r"\textbf{Verify:}", font_size=28, color=YELLOW)
        ex_verify = MathTex(
            r"V^T M_Q V = "
            r"\begin{bmatrix} 1 & X_1 & X_2^T X_1^T \end{bmatrix}"
            r"\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 2 \end{bmatrix}"
            r"\begin{bmatrix} 1 \\ X_1^T \\ X_1 X_2 \end{bmatrix}",
            font_size=26
        )
        ex_expand = MathTex(
            r"= X_1 X_2 + X_2^T X_1^T + X_1 X_1^T + 2\,X_2^T X_1^T X_1 X_2 = Q \;\checkmark",
            font_size=28, color=GREEN
        )

        ex_verify_group = VGroup(
            ex_verify_label, ex_verify, ex_expand
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        ex_verify_group.next_to(step1_title, DOWN, buff=0.6).set_x(0)
        center_mathtex(ex_verify_group)

        with self.voiceover(
            text="Let us verify: V transpose M V expands to exactly our polynomial Q. "
                 "The Gram representation works!"
        ):
            self.play(FadeIn(ex_verify_label))
            self.play(Write(ex_verify))
            self.play(Write(ex_expand))
            self.play(Circumscribe(ex_expand, color=GREEN, time_width=2))
        self.wait(2)

        self.play(FadeOut(step1_title, ex_verify_group))

        # ==========================================
        # SCENE 3a: NON-UNIQUENESS — Ghost matrices
        # ==========================================
        step2_title = Text("Step 2: Non-Uniqueness & Affine Spaces", font_size=36, color=TEAL).to_edge(UP, buff=0.5)

        nonuniq_text = Tex(
            r"\textbf{Problem:} The Gram matrix $M_Q$ is \textit{not unique}!",
            font_size=30, color=YELLOW
        )
        nonuniq_explain = Tex(
            r"In noncommutative algebra, there are ``word relations'' — identities\\",
            r"like $Z \cdot Z^{-1} = I$ — that create hidden cancellations among monomials.",
            font_size=26, tex_environment="flushleft"
        )
        ghost_header = Tex(
            r"\textbf{Ghost matrices:} Matrices $B$ such that $V^T B\, V = 0$ identically.",
            font_size=28
        )
        ghost_explain = Tex(
            r"Adding $B$ to $M_Q$ does not change $Q$, but changes the Gram matrix!",
            font_size=26
        )
        ghost_eq = MathTex(
            r"Q(X) = V^T (M_Q + B) V = V^T M_Q V + \underbrace{V^T B V}_{=\,0} = Q(X)",
            font_size=30, color=TEAL
        )

        ghost_group = VGroup(
            nonuniq_text, nonuniq_explain, ghost_header, ghost_explain, ghost_eq,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ghost_group.next_to(step2_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(ghost_group)

        with self.voiceover(
            text="Step two addresses a crucial subtlety: the Gram matrix is not unique. "
                 "In the noncommutative world, there are algebraic identities among monomials, "
                 "like Z times Z inverse equals the identity, that create hidden cancellations."
        ):
            self.play(Write(step2_title))
            self.play(FadeIn(nonuniq_text, nonuniq_explain))
        self.wait(1)

        with self.voiceover(
            text="This means there exist ghost matrices B, such that V transpose B V "
                 "equals zero identically. Adding such a B to the Gram matrix does not "
                 "change the polynomial, but does change the matrix."
        ):
            self.play(FadeIn(ghost_header, ghost_explain))
            self.play(Write(ghost_eq))
        self.wait(2)

        self.play(FadeOut(ghost_group))

        # ==========================================
        # SCENE 3b: NON-UNIQUENESS — Ghost example
        # ==========================================
        ghost_ex_label = Tex(r"\textbf{Example of a ghost matrix:}", font_size=28, color=YELLOW)
        ghost_ex = MathTex(
            r"\begin{bmatrix} Z \\ Z^2 \end{bmatrix}^{\!T}"
            r"\underbrace{\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}}_{B}"
            r"\begin{bmatrix} Z \\ Z^2 \end{bmatrix}"
            r"= Z^3 - Z^3 = 0",
            font_size=30, color=YELLOW
        )
        ghost_ex_note = Tex(
            r"$B$ is skew-symmetric, so $V^T B V$ cancels. This is a ghost matrix.",
            font_size=26, color=GREY_B
        )

        ghost_ex_group = VGroup(
            ghost_ex_label, ghost_ex, ghost_ex_note,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        ghost_ex_group.next_to(step2_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(ghost_ex_group)

        with self.voiceover(
            text="For instance, pair the vector Z, Z squared with the skew-symmetric matrix "
                 "0 1 negative 1 0. The result is Z cubed minus Z cubed, which is zero. "
                 "So this B is a ghost matrix."
        ):
            self.play(FadeIn(ghost_ex_label))
            self.play(Write(ghost_ex))
            self.play(FadeIn(ghost_ex_note))
            self.play(Indicate(ghost_ex, color=ORANGE))
        self.wait(2)

        self.play(FadeOut(ghost_ex_group))

        # ==========================================
        # SCENE 3c: NON-UNIQUENESS — Geometric picture
        # ==========================================
        geom_header = Tex(
            r"\textbf{Geometric picture:} The set of all valid Gram matrices is an affine plane.",
            font_size=28
        )
        affine_eq = MathTex(
            r"\mathcal{M} = \{ M_Q^0 + B \;:\; B \in \mathcal{B}_V \}",
            font_size=32, color=TEAL
        )
        affine_explain = Tex(
            r"$\mathcal{B}_V$ = space of ghost matrices (a linear subspace). \quad",
            r"$\mathcal{M}$ = affine plane of valid Gram matrices.",
            font_size=24, tex_environment="flushleft"
        )
        geom_text = VGroup(geom_header, affine_eq, affine_explain).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        geom_text.next_to(step2_title, DOWN, buff=0.35).set_x(0)
        center_mathtex(geom_text)

        # Key question
        key_question = Tex(
            r"\textbf{Key Question:} Does $\mathcal{M}$ intersect $\mathbb{S}_+^N$? "
            r"If yes $\Rightarrow$ $Q$ is SOS!",
            font_size=26, color=GREEN
        )
        key_question.next_to(geom_text, DOWN, buff=0.3)

        # Geometric visualization — compact, fits below text
        cone_apex = DOWN * 0.3
        cone = Polygon(
            cone_apex + DOWN * 0.8,
            cone_apex + UP * 1.0 + RIGHT * 2.0,
            cone_apex + UP * 1.0 + LEFT * 2.0,
            color=BLUE, fill_opacity=0.15, stroke_width=2.5
        )
        cone_label = MathTex(r"\mathbb{S}_+^N", font_size=22, color=BLUE)
        cone_label.next_to(cone, DOWN, buff=0.05)

        plane_start = cone_apex + LEFT * 2.8 + UP * 0.1
        plane_end = cone_apex + RIGHT * 2.8 + UP * 0.7
        plane_line = Line(plane_start, plane_end, color=YELLOW, stroke_width=3)
        plane_label = MathTex(r"\mathcal{M}", font_size=22, color=YELLOW)
        plane_label.next_to(plane_line, LEFT, buff=0.1)

        geom_viz = VGroup(cone, cone_label, plane_line, plane_label)
        geom_viz.next_to(key_question, DOWN, buff=0.3)

        with self.voiceover(
            text="Geometrically, the set of all valid Gram matrices for Q forms an affine plane, "
                 "which we call M. It is a translate of the linear subspace of ghost matrices."
        ):
            self.play(FadeIn(geom_text))
        self.wait(1)

        with self.voiceover(
            text="Now the entire proof reduces to one geometric question: "
                 "does this affine plane M intersect the positive semidefinite cone? "
                 "If it does, then we have a positive semidefinite Gram matrix, "
                 "and Q is a sum of squares."
        ):
            self.play(FadeIn(key_question))
            self.play(Create(cone), FadeIn(cone_label), run_time=0.8)
            self.play(Create(plane_line), FadeIn(plane_label), run_time=0.8)

            # Animate a dot sliding to intersection
            # intersect_point must lie on the plane line
            intersect_point = plane_line.point_from_proportion(0.5)
            dot = Dot(plane_line.point_from_proportion(0.05), color=GREEN, radius=0.08)
            self.play(FadeIn(dot))
            self.play(dot.animate.move_to(intersect_point), run_time=1.5)
            q_mark = MathTex(r"?", font_size=28, color=GREEN).next_to(dot, UP, buff=0.1)
            self.play(Write(q_mark))
            self.play(Flash(dot, color=GREEN, num_lines=8))
        self.wait(2)

        self.play(FadeOut(step2_title, geom_text, key_question, geom_viz, dot, q_mark))

        # ==========================================
        # SCENE 4a: KREIN'S THEOREM — Duality
        # ==========================================
        step3_title = Text("Step 3: Krein's Extension Theorem", font_size=36, color=GOLD).to_edge(UP, buff=0.5)

        dual_header = Tex(r"\textbf{The Dual Viewpoint:}", font_size=30)
        dual_explain = Tex(
            r"Instead of searching for a PSD matrix on $\mathcal{M}$ directly,\\",
            r"we use \textit{duality}: study linear functionals on symmetric matrices.",
            font_size=26, tex_environment="flushleft"
        )
        L_header = Tex(r"\textbf{Define a linear functional $L$:}", font_size=28)
        L_def = MathTex(
            r"L(W) = \operatorname{tr}(M_Q^0 \cdot W)",
            font_size=32, color=GOLD
        )
        L_explain = Tex(
            r"This functional ``evaluates'' $W$ against our reference Gram matrix $M_Q^0$.",
            font_size=26
        )
        L_positivity = Tex(
            r"Because $Q$ is matrix-positive, $L$ is \textbf{nonnegative} on\\",
            r"$\mathcal{B}_V^\perp \cap \mathbb{S}_+^N$ (PSD matrices orthogonal to ghost matrices).",
            font_size=26, tex_environment="flushleft"
        )
        L_pos_eq = MathTex(
            r"L(W) = \operatorname{tr}(M_Q^0 \, W) \ge 0 \quad "
            r"\forall\, W \in \mathcal{B}_V^\perp \cap \mathbb{S}_+^N",
            font_size=28, color=GOLD
        )

        dual_group = VGroup(
            dual_header, dual_explain, L_header, L_def, L_explain, L_positivity, L_pos_eq
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        dual_group.next_to(step3_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(dual_group)

        with self.voiceover(
            text="Step three is the analytic heart of the proof. Instead of directly "
                 "searching for a PSD matrix on the affine plane, "
                 "we switch to the dual viewpoint and study linear functionals."
        ):
            self.play(Write(step3_title))
            self.play(FadeIn(dual_header, dual_explain))
        self.wait(1)

        with self.voiceover(
            text="Define a linear functional L of W as the trace of our reference "
                 "Gram matrix M Q zero times W. This functional evaluates W "
                 "against the Gram matrix."
        ):
            self.play(FadeIn(L_header, L_explain))
            self.play(Write(L_def))
        self.wait(1)

        with self.voiceover(
            text="Because Q is matrix-positive, this functional L is nonnegative "
                 "on the set of PSD matrices that are orthogonal to the ghost matrices. "
                 "This is the key positivity condition."
        ):
            self.play(FadeIn(L_positivity))
            self.play(Write(L_pos_eq))
            self.play(Indicate(L_pos_eq, color=ORANGE))
        self.wait(2)

        self.play(FadeOut(dual_group))

        # ==========================================
        # SCENE 4b: KREIN'S THEOREM — Statement & Consequence
        # ==========================================
        krein_header = Tex(r"\textbf{Krein's Extension Theorem:}", font_size=32, color=GOLD)
        krein_statement = Tex(
            r"If a linear functional is nonnegative on the PSD matrices\\",
            r"within a subspace, it can be extended to a linear functional\\",
            r"that is nonnegative on \textit{all} PSD matrices.",
            font_size=26, tex_environment="flushleft"
        )
        krein_card, krein_box, _ = make_theorem_card(krein_statement, color=GOLD, buff=0.25)

        krein_intuition_label = Tex(r"\textbf{Intuition:}", font_size=28, color=GREY_B)
        krein_intuition = Tex(
            r"Think of it like the Hahn--Banach theorem: a positive functional\\",
            r"on a subspace can be ``spread out'' to the whole space while\\",
            r"preserving positivity.",
            font_size=24, color=GREY_B, tex_environment="flushleft"
        )

        consequence_header = Tex(r"\textbf{Consequence for our proof:}", font_size=28)
        consequence = Tex(
            r"The extended functional $\tilde{L}$ corresponds to a PSD matrix\\",
            r"$\tilde{M} \succeq 0$ on the affine plane $\mathcal{M}$.",
            font_size=26, tex_environment="flushleft"
        )

        krein_group = VGroup(
            krein_header, krein_card,
            krein_intuition_label, krein_intuition,
            consequence_header, consequence,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        krein_group.next_to(step3_title, DOWN, buff=0.4).set_x(0)
        # Center the boxed Krein statement
        krein_card.set_x(0)

        with self.voiceover(
            text="Now we invoke Krein's extension theorem. It states that if a linear "
                 "functional is nonnegative on the PSD matrices within a subspace, "
                 "it can be extended to a linear functional that is nonnegative on all PSD matrices."
        ):
            self.play(Write(krein_header))
            self.play(FadeIn(krein_statement), Create(krein_box))
            self.play(Indicate(krein_card, color=GOLD))
        self.wait(1)

        with self.voiceover(
            text="You can think of this as a cousin of the Hahn-Banach theorem. "
                 "Any positive functional on a subspace can be spread out to the whole space "
                 "while preserving its positivity."
        ):
            self.play(FadeIn(krein_intuition_label, krein_intuition))
        self.wait(1)

        with self.voiceover(
            text="The consequence is decisive. The extended functional corresponds to a "
                 "PSD matrix M tilde that lives on our affine plane M. "
                 "In other words, the plane does intersect the PSD cone! "
                 "We have found our positive semidefinite Gram matrix."
        ):
            self.play(FadeIn(consequence_header, consequence))
        self.wait(1)

        self.play(FadeOut(krein_group))

        # ==========================================
        # SCENE 4c: KREIN'S THEOREM — Geometric flashback
        # ==========================================
        geom_recap_label = Tex(
            r"\textbf{Geometric conclusion:} The intersection exists!",
            font_size=28, color=GREEN
        )
        geom_recap_eq = MathTex(
            r"\exists\, \tilde{M} \in \mathcal{M} \cap \mathbb{S}_+^N"
            r"\quad\Longleftrightarrow\quad \tilde{M} \succeq 0",
            font_size=30, color=GREEN
        )
        geom_recap_text = VGroup(geom_recap_label, geom_recap_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        geom_recap_text.next_to(step3_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(geom_recap_text)

        # Compact geometry
        cone2_apex = DOWN * 0.5
        cone2 = Polygon(
            cone2_apex + DOWN * 0.8,
            cone2_apex + UP * 1.0 + RIGHT * 2.0,
            cone2_apex + UP * 1.0 + LEFT * 2.0,
            color=BLUE, fill_opacity=0.15, stroke_width=2.5
        )
        cone2_label = MathTex(r"\mathbb{S}_+^N", font_size=22, color=BLUE).next_to(cone2, DOWN, buff=0.05)
        plane2 = Line(
            cone2_apex + LEFT * 2.8 + UP * 0.1,
            cone2_apex + RIGHT * 2.8 + UP * 0.7,
            color=YELLOW, stroke_width=3
        )
        plane2_label = MathTex(r"\mathcal{M}", font_size=22, color=YELLOW)

        geom2_viz = VGroup(cone2, cone2_label, plane2, plane2_label)
        geom2_viz.next_to(geom_recap_text, DOWN, buff=0.4)

        # Position labels and dot AFTER the group has been placed
        cone2_label.next_to(cone2, DOWN, buff=0.05)
        plane2_label.next_to(plane2, LEFT, buff=0.1)
        intersect_pt = plane2.point_from_proportion(0.5)
        dot2 = Dot(intersect_pt, color=GREEN, radius=0.12)
        dot_label2 = MathTex(r"\tilde{M} \succeq 0", font_size=24, color=GREEN).next_to(dot2, UR, buff=0.1)

        with self.voiceover(
            text="Geometrically, Krein's theorem guarantees the green intersection point exists."
        ):
            self.play(FadeIn(geom_recap_text))
            self.play(Create(cone2), FadeIn(cone2_label), Create(plane2), FadeIn(plane2_label), run_time=0.8)
            self.play(FadeIn(dot2, scale=0.5), run_time=0.5)
            self.play(Write(dot_label2))
            self.play(Flash(dot2, color=GREEN, num_lines=12))
        self.wait(2)

        self.play(FadeOut(step3_title, geom_recap_text, geom2_viz, dot2, dot_label2))

        # ==========================================
        # SCENE 5a: CHOLESKY — Setup & factorization
        # ==========================================
        step4_title = Text("Step 4: Cholesky Factorization", font_size=36, color=GREEN).to_edge(UP, buff=0.5)

        chol_setup = Tex(
            r"\textbf{We now have:} A positive semidefinite Gram matrix $M \succeq 0$\\",
            r"with $Q(X) = V(X)^T M\, V(X)$.",
            font_size=28, tex_environment="flushleft"
        )
        chol_header = Tex(r"\textbf{Cholesky Factorization:}", font_size=30)
        chol_explain = Tex(
            r"Every PSD matrix $M$ can be factored as $M = L^T L$\\",
            r"where $L$ is an upper triangular matrix (with nonneg.\ diagonal).",
            font_size=26, tex_environment="flushleft"
        )
        chol_eq = MathTex(r"M = L^T L", font_size=40, color=GREEN)

        sub_header = Tex(r"\textbf{Substitute into the Gram form:}", font_size=28)
        sub_eq1 = MathTex(
            r"Q(X) = V^T M\, V = V^T (L^T L)\, V = (LV)^T (LV)",
            font_size=32
        )

        chol_group_a = VGroup(
            chol_setup, chol_header, chol_explain, chol_eq, sub_header, sub_eq1,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        chol_group_a.next_to(step4_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(chol_group_a)

        with self.voiceover(
            text="Step four is the algebraic payoff. We now possess a positive semidefinite "
                 "Gram matrix M. Every PSD matrix admits a Cholesky factorization: "
                 "M equals L transpose times L."
        ):
            self.play(Write(step4_title))
            self.play(FadeIn(chol_setup))
            self.play(FadeIn(chol_header, chol_explain))
            self.play(Write(chol_eq))
        self.wait(1)

        with self.voiceover(
            text="Substituting into the Gram form, Q equals V transpose L transpose "
                 "L V, which equals L V transpose times L V."
        ):
            self.play(FadeIn(sub_header))
            self.play(Write(sub_eq1))
        self.wait(1)

        self.play(FadeOut(chol_group_a))

        # ==========================================
        # SCENE 5b: CHOLESKY — SOS result
        # ==========================================
        sos_header = Tex(r"\textbf{Each row of $L$ gives a polynomial:}", font_size=28)
        sub_eq2 = MathTex(
            r"(LV)^T (LV) = \sum_{i=1}^k (L_i \cdot V)^* \, (L_i \cdot V)",
            font_size=32
        )
        sub_note = Tex(
            r"where $p_i = L_i \cdot V$ is a noncommutative polynomial\\",
            r"(the $i$-th row of $L$ dotted with $V$).",
            font_size=24, color=GREY_B, tex_environment="flushleft"
        )
        sub_result = MathTex(
            r"\boxed{Q = \sum_{i=1}^k p_i^* \, p_i}",
            font_size=42, color=GREEN
        )

        chol_group_b = VGroup(
            sos_header, sub_eq2, sub_note, sub_result,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        chol_group_b.next_to(step4_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(chol_group_b)

        with self.voiceover(
            text="Each row of L, dotted with the basis vector V, gives a noncommutative "
                 "polynomial p i. And so Q is exactly the sum of p i star times p i. "
                 "This is the sum-of-squares decomposition! The proof is complete."
        ):
            self.play(FadeIn(sos_header))
            self.play(Write(sub_eq2))
            self.play(FadeIn(sub_note))
            self.wait(0.5)
            self.play(Write(sub_result), run_time=1.0)
            self.play(Circumscribe(sub_result, color=GREEN, time_width=2.5))
            self.play(Indicate(sub_result, scale_factor=1.1, color=GREEN))
        self.wait(2)

        self.play(FadeOut(step4_title, chol_group_b))

        # ==========================================
        # SCENE 6a: APPLICATION — Commutator squared setup
        # ==========================================
        app_title = Text("Application: A Purely Noncommutative Inequality", font_size=34, color=GREEN).to_edge(UP, buff=0.5)

        app_setup = Tex(
            r"Consider the following degree-4 polynomial in two symmetric variables:",
            font_size=28
        )
        app_poly = MathTex(
            r"Q(X, Y) = XY^2X + YX^2Y - XYXY - YXYX",
            font_size=32, color=YELLOW
        )
        app_note = Tex(
            r"Note: if $X$ and $Y$ commute, every term cancels and $Q = 0$.\\",
            r"This polynomial is \textit{invisible} in commutative algebra!",
            font_size=26, color=GREY_B, tex_environment="flushleft"
        )
        app_check1 = Tex(r"$\bullet$ $Q$ is symmetric? \textbf{Yes:} $Q^* = Q$ (each term is self-adjoint)", font_size=24)
        app_check2 = Tex(
            r"$\bullet$ $Q \succeq 0$ for all symmetric matrix inputs? "
            r"\textbf{Yes} (not obvious!)",
            font_size=24
        )
        app_check3 = Tex(
            r"$\bullet$ Therefore by Helton's theorem: $Q$ must be a sum of squares!",
            font_size=24, color=GREEN
        )

        app_group_a = VGroup(
            app_setup, app_poly, app_note,
            app_check1, app_check2, app_check3,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        app_group_a.next_to(app_title, DOWN, buff=0.4).set_x(0)
        center_mathtex(app_group_a)

        with self.voiceover(
            text="Let us see Helton's theorem in action with a striking example. "
                 "Consider the polynomial Q of X, Y equals "
                 "X Y squared X, plus Y X squared Y, minus X Y X Y, minus Y X Y X."
        ):
            self.play(Write(app_title))
            self.play(FadeIn(app_setup))
            self.play(Write(app_poly))
        self.wait(1)

        with self.voiceover(
            text="Notice something remarkable: if X and Y commute, every term cancels "
                 "and Q is identically zero. This polynomial is invisible in commutative algebra. "
                 "It only comes alive when the variables do not commute."
        ):
            self.play(FadeIn(app_note))
        self.wait(1)

        with self.voiceover(
            text="One can check that Q is symmetric, and that Q evaluates to a "
                 "positive semidefinite matrix for every symmetric matrix input, "
                 "though this is far from obvious. "
                 "So by Helton's theorem, Q must have a sum-of-squares decomposition. "
                 "But what is it?"
        ):
            self.play(FadeIn(app_check1, app_check2, app_check3), run_time=1.0)
            self.play(Indicate(app_check3, color=GREEN))
        self.wait(1)

        self.play(FadeOut(app_group_a))

        # ==========================================
        # SCENE 6b: APPLICATION — SOS decomposition reveal
        # ==========================================
        decomp_label = Tex(r"\textbf{The SOS decomposition:}", font_size=28, color=YELLOW)
        decomp_key = Tex(
            r"Define the \textbf{commutator}: $[X, Y] = XY - YX$",
            font_size=28
        )
        decomp_eq = MathTex(
            r"Q(X, Y) = [X, Y]^T \, [X, Y]",
            font_size=36, color=GREEN
        )
        decomp_card, decomp_box, _ = make_theorem_card(decomp_eq, color=GREEN, buff=0.2, stroke_width=2)

        decomp_verify_label = Tex(r"\textbf{Verify:}", font_size=26)
        decomp_verify = MathTex(
            r"[X,Y]^T [X,Y] = (YX - XY)(XY - YX)",
            font_size=28
        )
        decomp_expand = MathTex(
            r"= YX^2Y - YXYX - XYXY + XY^2X = Q \;\checkmark",
            font_size=28, color=GREEN
        )

        app_group_b = VGroup(
            decomp_label, decomp_key,
            decomp_card,
            decomp_verify_label, decomp_verify, decomp_expand,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        app_group_b.next_to(app_title, DOWN, buff=0.5).set_x(0)
        # Center the boxed equation and standalone MathTex
        decomp_card.set_x(0)
        center_mathtex(app_group_b)

        with self.voiceover(
            text="The answer is elegant. Define the commutator, X Y minus Y X. "
                 "Then Q equals the commutator transpose times the commutator."
        ):
            self.play(FadeIn(decomp_label, decomp_key))
            self.play(Write(decomp_eq), Create(decomp_box))
            self.play(Circumscribe(decomp_card, color=GREEN, time_width=2))
        self.wait(1)

        with self.voiceover(
            text="Let us verify. Expanding the product Y X minus X Y times X Y minus Y X, "
                 "we get Y X squared Y, minus Y X Y X, minus X Y X Y, plus X Y squared X. "
                 "That is exactly Q."
        ):
            self.play(FadeIn(decomp_verify_label))
            self.play(Write(decomp_verify))
            self.play(Write(decomp_expand))
            self.play(Indicate(decomp_expand, color=GREEN))
        self.wait(1)

        self.play(FadeOut(app_group_b))

        # ==========================================
        # SCENE 6c: APPLICATION — Numerical verification
        # ==========================================
        num_label = Tex(r"\textbf{Numerical check} ($2 \times 2$ matrices):", font_size=28, color=YELLOW)
        num_X = MathTex(
            r"X = \begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}",
            font_size=28
        )
        num_Y = MathTex(
            r"Y = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}",
            font_size=28
        )
        num_comm = MathTex(
            r"[X, Y] = XY - YX = \begin{bmatrix} 0 & -4 \\ 4 & 0 \end{bmatrix}",
            font_size=28
        )
        num_result = MathTex(
            r"Q(X,Y) = [X,Y]^T[X,Y] = \begin{bmatrix} 16 & 0 \\ 0 & 16 \end{bmatrix} \succeq 0 \;\checkmark",
            font_size=28, color=YELLOW
        )

        num_XY = VGroup(num_X, num_Y).arrange(RIGHT, buff=1.0)

        app_group_c = VGroup(
            num_label, num_XY, num_comm, num_result,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        app_group_c.next_to(app_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(app_group_c)

        with self.voiceover(
            text="Let us verify numerically. Take X equals the matrix 1, 2, 2, 3, "
                 "and Y equals 2, 1, 1, 1. Their commutator is the skew-symmetric matrix "
                 "0, negative 4, 4, 0. "
                 "Then Q equals the commutator transpose times the commutator, "
                 "which is 16 times the identity — clearly positive semidefinite. "
                 "Helton's theorem works beautifully."
        ):
            self.play(FadeIn(num_label))
            self.play(Write(num_XY))
            self.play(Write(num_comm))
            self.play(Write(num_result))
            self.play(Indicate(num_result, color=YELLOW))
        self.wait(2)

        self.play(FadeOut(app_title, app_group_c))

        # ==========================================
        # SCENE 7: SUMMARY & PROOF RECAP
        # ==========================================
        summary_title = Text("Summary", color=BLUE, font_size=40).to_edge(UP, buff=0.5)

        summary_steps = [
            (r"\checkmark\; \text{Step 1: Gram Representation}", r"Q = V^T M_Q V", BLUE),
            (r"\checkmark\; \text{Step 2: Non-Uniqueness}", r"\mathcal{M} = M_Q^0 + \mathcal{B}_V", TEAL),
            (r"\checkmark\; \text{Step 3: Krein's Theorem}", r"\mathcal{M} \cap \mathbb{S}_+^N \neq \emptyset", GOLD),
            (r"\checkmark\; \text{Step 4: Cholesky}", r"M = L^T L \;\Rightarrow\; Q = \sum p_i^* p_i", GREEN),
        ]
        summary_mobs = []
        for label_tex, eq_tex, col in summary_steps:
            lab = MathTex(label_tex, font_size=28, color=col)
            eq = MathTex(eq_tex, font_size=26)
            row = VGroup(lab, eq).arrange(RIGHT, buff=0.5)
            summary_mobs.append(row)

        summary_col = VGroup(*summary_mobs).arrange(DOWN, aligned_edge=LEFT, buff=0.35)

        final_thm = MathTex(
            r"\boxed{Q \succeq 0 \;\forall\text{ matrices} \quad\Longrightarrow\quad "
            r"Q = \sum p_i^* p_i}",
            font_size=38, color=GREEN
        )

        takeaway = Tex(
            r"\textbf{Takeaway:} Noncommutativity is a \textit{feature}, not a bug.\\",
            r"It provides enough rigidity that positivity $\Leftrightarrow$ sum of squares.",
            font_size=26, tex_environment="flushleft"
        )

        summary_all = VGroup(summary_col, final_thm, takeaway).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        summary_all.next_to(summary_title, DOWN, buff=0.5).set_x(0)
        center_mathtex(summary_all)

        with self.voiceover(
            text="Let us recap. In step one, we wrote Q as a quadratic form using a Gram matrix. "
                 "In step two, we observed the Gram matrix is not unique, forming an affine plane. "
                 "In step three, Krein's extension theorem proved this plane intersects the PSD cone. "
                 "In step four, Cholesky factorization gave us the sum-of-squares decomposition."
        ):
            self.play(Write(summary_title))
            for mob in summary_mobs:
                self.play(FadeIn(mob, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1)

        with self.voiceover(
            text="The final result: if a symmetric noncommutative polynomial is "
                 "positive semidefinite for all matrix inputs, it is a sum of squares. "
                 "The deep insight is that noncommutativity is a feature, not a bug. "
                 "It provides enough algebraic rigidity that positivity is equivalent "
                 "to being a sum of squares."
        ):
            self.play(Write(final_thm))
            self.play(Circumscribe(final_thm, color=GREEN, time_width=2.5))
            self.play(FadeIn(takeaway))
        self.wait(1)

        with self.voiceover(
            text="Thank you for watching. This elegant connection between analysis, "
                 "algebra, and geometry is what makes Helton's theorem one of the "
                 "jewels of noncommutative real algebraic geometry."
        ):
            self.wait(2)

        self.wait(2)
