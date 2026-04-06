---
description: Pacing and timing guidelines for Manim voiceover animations. Defines named pause durations for consistent rhythm across scenes. Use when writing self.wait() calls, spacing animations, or reviewing timing in Manim scripts.
globs: ["*.py"]
---

# Manim Pacing — Pause Timing Guide

## Named Pause Durations

Use these semantic names when deciding `self.wait()` values. Every pause in a scene should fall into one of these categories.

| Name | Duration | When to Use |
|------|----------|-------------|
| `PAUSE_BRIEF` | `0.5` | Between tightly coupled animations (e.g., label after its object, subtitle after title) |
| `PAUSE_ELEMENT` | `1.0` | After fading in a single definition, bullet point, or timeline entry |
| `PAUSE_READ` | `1.5` | After showing a multi-line block the viewer needs to read (induced subgraph def, lemma statement) |
| `PAUSE_ABSORB` | `2.0` | After a moderately important result or a worked example step |
| `PAUSE_KEY_RESULT` | `3.0` | After a key theorem, main formula, or highlighted result (post-Circumscribe, post-Write on important equation) |
| `PAUSE_BREATHE` | `3.5` | After a dense proof step or complex derivation the viewer needs time to digest |
| `PAUSE_SCENE_END` | `1.5` | Final pause before `clear_screen(self)` at the end of every scene |
| `PAUSE_FINALE` | `4.0` | After the final result or closing statement of the entire video |

## Where Each Pause Goes

**IMPORTANT:** Read the `self.wait()` inside-vs-outside rule in the **manim-voiceover-tts** skill first. Waits inside voiceover blocks behave differently from waits outside them.

### Within a Voiceover Block (Fill During TTS Audio)

Waits inside voiceover blocks serve as **pacing between animations while TTS audio is playing**. They may be clipped if the voiceover audio is shorter than the total animation + wait time.

```python
with self.voiceover(text="..."):
    self.play(FadeIn(definition))
    self.wait(1.0)          # PAUSE_ELEMENT: pacing during speech
    self.play(FadeIn(example))
    self.wait(1.5)          # PAUSE_READ: multi-line example to read
    self.play(Write(formula))
    self.wait(3.0)          # PAUSE_KEY_RESULT: important formula
```

### Outside Voiceover Blocks (Real Silence)

Waits outside voiceover blocks are **real silence with no audio**. Keep them short to avoid awkward dead air.

```python
with self.voiceover(text="Here is the theorem..."):
    self.play(Write(theorem))

self.wait(1.0)              # Real breathing pause — actual silence

with self.voiceover(text="The proof is short..."):
    self.play(FadeIn(proof))

self.wait(1.0)              # Real breathing pause
```

### Pass-Only Voiceover Blocks

When a voiceover block has only `pass` inside (no animations — the TTS plays on its own), the post-block wait should be very short since the TTS audio already provides natural pacing:

```python
with self.voiceover(text="Let's think about why this is true..."):
    pass

self.wait(0.5)              # Short — TTS already played fully
```

### At Scene Boundaries

```python
with self.voiceover(text="And that completes the proof."):
    self.play(Write(qed))

self.wait(1.0)              # PAUSE_SCENE_END: breathing room before transition
clear_screen(self)
```

## Pacing Rules

### 1. One Concept Per Voiceover Block

Each `with self.voiceover():` block should introduce exactly one idea. If you're explaining two distinct things, split into two blocks with appropriate pauses.

### 2. Don't Stack Animations Without Pauses

**Bad:**
```python
self.play(FadeIn(def1))
self.play(FadeIn(def2))
self.play(FadeIn(def3))
```

**Good:**
```python
self.play(FadeIn(def1))
self.wait(1.0)              # PAUSE_ELEMENT
self.play(FadeIn(def2))
self.wait(1.0)              # PAUSE_ELEMENT
self.play(FadeIn(def3))
self.wait(2.0)              # PAUSE_ABSORB: let viewer see the full set
```

### 3. Emphasis Animations Need Post-Pauses

After `Circumscribe`, `Indicate`, or `Flash`, always add a key-result pause so the viewer registers the highlight:

```python
self.play(Circumscribe(card, color=GREEN, time_width=2))
self.wait(3.0)              # PAUSE_KEY_RESULT
```

### 4. Proof Steps Get More Time Than Definitions

Definitions are read; proof steps require thought. Scale pauses accordingly:
- Definition bullet: `1.0` (PAUSE_ELEMENT)
- Proof computation: `3.5` (PAUSE_BREATHE)
- Final QED result: `3.0` (PAUSE_KEY_RESULT)

### 5. Scene-End Pauses Are Mandatory

Every scene must end with `PAUSE_SCENE_END` (1.5s) before `clear_screen()`. This prevents the feeling of content being yanked away.

### 6. Transitions Between Topic Shifts

When changing topic (e.g., from proof roadmap to boolean sensitivity), add a dedicated transition screen with `PAUSE_KEY_RESULT` (3.0s) to let the viewer mentally reset.

## Voiceover Text Pacing

The voiceover text itself affects pacing. Longer, more deliberate voiceover text naturally slows the scene. Prefer:

**Too fast:**
```python
text="Sensitivity counts bit flips that change f. At 0 0 0, all 3 flips change it, so sensitivity is 3."
```

**Better:**
```python
text="Sensitivity at an input x counts how many single-bit flips change the output. "
     "Let's see this in action. At x equals 0 0 0, the OR function outputs 0. "
     "Flip the first bit: we get 1 0 0, and the output becomes 1. That's a change. "
     "Flip the second bit: 0 1 0, output is 1. Another change. "
     "Flip the third bit: 0 0 1, output is 1. Again a change. "
     "All 3 flips change the output, so the sensitivity at this input is 3."
```

## Anti-Patterns

- **`self.wait(0.3)`**: Too short to register. Minimum meaningful pause is `0.5` (PAUSE_BRIEF).
- **No pause after `Write(equation)`**: The viewer can't read what was just written.
- **`self.wait(2)` after everything**: Monotonous rhythm. Vary pauses by importance.
- **Skipping `PAUSE_SCENE_END`**: Makes transitions feel jarring.
- **Long pause after trivial content**: A simple label doesn't need 3 seconds.
- **Long waits (2-8s) outside voiceover blocks**: Creates awkward dead silence. Outside-block waits should be 0.5-1.5s max.
- **`self.wait()` at the end of a voiceover block expecting it to pause**: Waits at the end of a voiceover block are often silently clipped. Move them outside the block. See the **manim-voiceover-tts** skill for the full explanation.
