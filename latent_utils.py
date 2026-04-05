"""
latent_utils.py — Reusable utilities for Latent Seminar Manim videos.

Provides:
  - center_mathtex(group)        Center standalone MathTex items within a VGroup.
  - make_content_group(...)      Build a left-aligned, centered content block.
  - make_theorem_card(...)       Boxed theorem / key-equation card.
  - LatentPrelude                Mixin class adding the Latent Seminar prelude.
  - clear_screen(scene)          Fade out all mobjects from a scene.

Usage:
    from latent_utils import (
        center_mathtex,
        make_content_group,
        make_theorem_card,
        LatentPrelude,
        clear_screen,
        SEMINAR_BLUE,
    )
"""

from manim import *

# ── Constants ──────────────────────────────────────────────────────────

SEMINAR_BLUE = "#6fa8dc"
"""The signature blue used by Latent Seminar branding."""


# ── Helpers ────────────────────────────────────────────────────────────

def center_mathtex(group):
    """Center standalone MathTex items within a VGroup on the scene (set_x(0)),
    while leaving Tex items at their left-aligned position.

    Only acts on *direct* children that are MathTex (not plain Tex), since
    Tex is a subclass of MathTex.

    Returns the group for chaining.
    """
    for child in group:
        if isinstance(child, MathTex) and not isinstance(child, Tex):
            child.set_x(0)
    return group


def make_content_group(
    *items,
    reference=None,
    buff_between=0.3,
    buff_below=0.5,
    aligned_edge=LEFT,
    center_math=True,
):
    """Build a left-aligned, horizontally centered content block.

    Parameters
    ----------
    *items : Mobject
        The mobjects to stack vertically.
    reference : Mobject | None
        If given, the group is placed below this mobject using
        ``.next_to(reference, DOWN, buff=buff_below)``.
    buff_between : float
        Vertical spacing between items (passed to ``VGroup.arrange``).
    buff_below : float
        Gap between *reference* and the top of the group.
    aligned_edge : np.ndarray
        Edge for internal alignment (default LEFT).
    center_math : bool
        If True, call ``center_mathtex`` on the result.

    Returns
    -------
    VGroup
        The arranged, positioned, and (optionally) math-centered group.
    """
    group = VGroup(*items).arrange(DOWN, aligned_edge=aligned_edge, buff=buff_between)
    if reference is not None:
        group.next_to(reference, DOWN, buff=buff_below)
    group.set_x(0)
    if center_math:
        center_mathtex(group)
    return group


def make_theorem_card(
    *content_items,
    color=GREEN,
    buff=0.3,
    corner_radius=0.1,
    stroke_width=2.5,
    content_buff=0.2,
):
    """Create a boxed theorem / equation card.

    Parameters
    ----------
    *content_items : Mobject
        One or more mobjects to stack inside the box.
    color : Color
        Border color for the SurroundingRectangle.
    buff : float
        Padding between the content and the rectangle border.
    corner_radius : float
        Rounded corner radius.
    stroke_width : float
        Border thickness.
    content_buff : float
        Vertical spacing between content items if more than one.

    Returns
    -------
    tuple[VGroup, SurroundingRectangle, VGroup]
        ``(card, rect, content)`` where *card* = ``VGroup(rect, content)``.
    """
    if len(content_items) == 1:
        content = content_items[0]
    else:
        content = VGroup(*content_items).arrange(DOWN, buff=content_buff)

    rect = SurroundingRectangle(
        content,
        color=color,
        buff=buff,
        corner_radius=corner_radius,
        stroke_width=stroke_width,
    )
    card = VGroup(rect, content)
    return card, rect, content


def clear_screen(scene, run_time=0.5):
    """Fade out every mobject currently on screen.

    Parameters
    ----------
    scene : Scene
        The Manim scene instance (typically ``self``).
    run_time : float
        Duration of the fade-out animation.
    """
    if scene.mobjects:
        scene.play(*[FadeOut(mob) for mob in scene.mobjects], run_time=run_time)


# ── Prelude Mixin ──────────────────────────────────────────────────────

class LatentPrelude:
    """Mixin for VoiceoverScene that plays the Latent Seminar prelude.

    Usage::

        class MyScene(LatentPrelude, VoiceoverScene):
            def construct(self):
                self.play_prelude()          # default settings
                # ... rest of the animation
    """

    def play_prelude(
        self,
        music_file="prelude_music.mp3",
        font_size=60,
        letter_time=0.08,
        latent_run_time=0.6,
        seminar_run_time=0.7,
        pause_between=0.5,
        glow_run_time=1.5,
        hold_after_glow=1.4,
        dissolve_run_time=1.0,
        post_wait=0.3,
    ):
        """Play the Latent Seminar branding sequence.

        "Latent" appears in black (invisible on white/default BG), then
        "Seminar" in SEMINAR_BLUE.  A glow pulse reveals "Latent" via a
        blue outline stroke.  Background music plays for ~5 seconds with
        built-in fade-out.

        Parameters
        ----------
        music_file : str
            Path to the opening music clip (expects ~5 s with fade-out).
        font_size : int
            Size for the branding text.
        letter_time : float
            Seconds per character in AddTextLetterByLetter.
        latent_run_time : float
            Duration for "Latent" letter-by-letter animation.
        seminar_run_time : float
            Duration for "Seminar" letter-by-letter animation.
        pause_between : float
            Pause after "Latent" before "Seminar" appears.
        glow_run_time : float
            Duration of the glow-pulse animation.
        hold_after_glow : float
            Wait time after glow before dissolving (syncs with music).
        dissolve_run_time : float
            Duration of the final fade-out.
        post_wait : float
            Brief pause after dissolve before the next scene.
        """
        ls_latent = Text("Latent", font_size=font_size, color=BLACK, weight=BOLD)
        ls_seminar = Text("Seminar", font_size=font_size, color=SEMINAR_BLUE, weight=BOLD)
        ls_text = VGroup(ls_latent, ls_seminar).arrange(RIGHT, buff=0.3)
        ls_glow = ls_text.copy().set_opacity(0)

        # Blue outline sitting on top of "Latent" — starts invisible
        ls_latent_outline = ls_latent.copy().set_fill(opacity=0)
        ls_latent_outline.set_stroke(color=SEMINAR_BLUE, width=1.5, opacity=0)
        ls_latent_outline.move_to(ls_latent)

        # Opening music
        self.add_sound(music_file)

        # Fade in letter by letter
        self.play(
            AddTextLetterByLetter(ls_latent, time_per_char=letter_time),
            run_time=latent_run_time,
        )
        self.wait(pause_between)
        self.play(
            AddTextLetterByLetter(ls_seminar, time_per_char=letter_time),
            run_time=seminar_run_time,
        )

        # Glow pulse — reveal "Latent" with blue outline
        self.add(ls_latent_outline)
        self.play(
            ls_glow.animate.set_opacity(0.5).scale(1.05),
            ls_latent_outline.animate.set_stroke(opacity=1),
            run_time=glow_run_time,
            rate_func=there_and_back,
        )
        self.remove(ls_latent_outline)

        # Hold until music fades away
        self.wait(hold_after_glow)

        # Elegant dissolve
        self.play(
            FadeOut(ls_text, shift=UP * 0.3, run_time=dissolve_run_time),
            FadeOut(ls_glow, run_time=dissolve_run_time),
        )
        self.wait(post_wait)
