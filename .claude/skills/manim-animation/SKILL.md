---
description: Best practices for writing Manim Community animations for math explainer videos. Use when creating or editing .py files that use manim, VoiceoverScene, or MathTex.
globs: ["*.py"]
---

# Manim Animation Best Practices

## Environment

- Manim Community v0.20.1 with `manim_voiceover` and custom `kokoro_mv` module (KokoroService).
- Conda environment: `my-manim-environment` (hyphens, not underscores).
- Activate: `source activate my-manim-environment`
- Render: `manim render <file>.py <SceneName> -ql --disable_caching`

## Scene Structure

- Use `VoiceoverScene` as the base class (from `manim_voiceover`).
- Initialize TTS in `construct()`: `self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))`
- Organize content into clearly commented scene blocks with `# ===` separators.
- Split scenes that overflow the screen into sub-scenes (e.g., Scene 2a, 2b).

## LaTeX and Math

- Use `MathTex` for pure math formulas, `Tex` for text with inline math.
- `Tex` is a subclass of `MathTex` — to select only pure math objects, use:
  `isinstance(child, MathTex) and not isinstance(child, Tex)`
- Use `tex_environment="flushleft"` for multi-line Tex that should be left-aligned internally.
- **LaTeX concatenation bug**: When Python implicitly concatenates raw strings like `r"\quad"` followed by `r"Q = ..."`, LaTeX sees `\quadQ` (undefined control sequence). Always add a trailing space: `r"\quad "`.

### LaTeX Pitfalls — MUST AVOID

1. **`\textcolor{red}{...}`**: Causes LaTeX compilation errors because the default Manim LaTeX template does not include the `xcolor` package. Use Manim's `color=` parameter instead:
   ```python
   # WRONG — will crash
   MathTex(r"\textcolor{red}{x^2}")
   
   # CORRECT
   MathTex(r"x^2", color=RED)
   ```

2. **`\ll` and `\gg`**: These render as parallel lines (like `‖`) in Manim's default LaTeX template, not as "much less than" / "much greater than" symbols. Use plain text in voiceover and avoid in displayed math, or use the word form:
   ```python
   # WRONG — renders as parallel lines
   MathTex(r"n \gg k")
   
   # CORRECT — use Tex with words
   Tex(r"$n$ much larger than $k$", font_size=28)
   ```

3. **`$\quad$` for bullet continuation indentation**: Too wide. Use `$\phantom{\bullet}$\;` instead for continuation lines that align under bulleted text.

4. **`\quad` concatenation**: `r"\quad"` followed by `r"Q = ..."` produces `\quadQ` (undefined). Always add trailing space: `r"\quad "`.

## Geometric Diagrams

- Use absolute coordinates for geometry (cones, planes, dots), then reposition the group with `.next_to()`.
- **Critical**: Create dots and labels AFTER the group is positioned, otherwise they end up at wrong locations.
- For animated dots on lines, use `line.point_from_proportion()` to get points along the line.

### Arc Positioning — `shift()` vs `move_to()`

**`Arc` with `move_to()` misaligns** because `move_to` centers the bounding box, not the arc center. For half-circles and arcs, use `shift()` instead:

```python
# WRONG — arc center ends up in the wrong place
arc = Arc(radius=1, start_angle=0, angle=PI)
arc.move_to(center_point)

# CORRECT — shift from origin to desired center
arc = Arc(radius=1, start_angle=0, angle=PI)
arc.shift(center_point - arc.get_arc_center())
```

## Boxed Theorem Cards

Use `make_theorem_card()` from `latent_utils`:

```python
from latent_utils import make_theorem_card
card, rect, content = make_theorem_card(text1, text2, color=GREEN, buff=0.3)
# Animate: self.play(FadeIn(content), Create(rect))
```

## Proof Roadmaps

- Use `RoundedRectangle` boxes with color-coded steps.
- Add `Arrow` objects between steps for flow.
- Animate step-by-step with `FadeIn(step, shift=RIGHT * 0.3)`.

## Color Conventions

| Purpose | Color |
|---------|-------|
| Step 1 / titles | BLUE |
| Step 2 / Gram | TEAL |
| Step 3 / Krein | GOLD |
| Step 4 / result | GREEN |
| Warnings / problems | YELLOW / RED |
| Notes / secondary | GREY_B |
| Examples | YELLOW |

## Graph Theory Animations

### Random Colorings

When generating random 2-colorings of complete graphs (e.g., K6 edge colorings for Ramsey theory), **test your random seed** to ensure the coloring does not accidentally contain a monochromatic clique you're trying to show doesn't exist. For K6 with red/blue edge colorings, seeds 1, 0, and 5 produce colorings with monochromatic triangles — avoid these if demonstrating triangle-free colorings.
