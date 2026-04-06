---
description: Workarounds for KokoroService TTS mispronunciations and voiceover best practices. Use when writing voiceover text in Manim scripts.
globs: ["*.py"]
---

# Manim Voiceover & TTS Pitfalls

## TTS Engine

- Uses `KokoroService` from custom `kokoro_mv` module.
- Voice: `af_heart`, Language: `en-us`
- Initialize: `self.set_speech_service(KokoroService(voice="af_heart", lang="en-us"))`

## Known Mispronunciations — MUST AVOID

### The letter "A" as a variable name
- **Problem**: TTS reads the single letter "A" as the article "a" (uh/ay), not as "the matrix A".
- **Fix**: Use other letters for matrix variables in voiceover text: X, Y, Z, W, M.
- Example: Instead of "matrix A", say "matrix W" or "matrix M".

### The word "eigenvalue"
- **Problem**: TTS mispronounces any word with the prefix "eigen" — including "eigenvalue", "eigenvector", "eigenspace", etc.
- **Fix**: Use alternatives:
  - "eigenvalue" → "spectral value", "value in the spectrum", or just "spectrum"
  - "eigenvector" → "characteristic vector"
  - "eigenspace" → "characteristic subspace"
- Example: Instead of "the eigenvalues are nonnegative", say "every value in its spectrum is nonnegative".
- Example: Instead of "pick the eigenvector entry", say "pick the characteristic vector entry".

### The suffix "-th" after numbers or symbols
- **Problem**: TTS has trouble pronouncing "-th" when appended to a number or symbol to form an index/ordinal — e.g., "i-th", "k-th", "5-th", "(r+1)-th". It may read "i-th" as three separate letters "i t h", or garble "(r+1)-th".
- **Fix**: Rephrase to avoid the "-th" suffix entirely.
- Example: Instead of "the i-th bit", say "bit i" or "the bit at position i" or "coordinate i".
- Example: Instead of "the k-th entry", say "entry k" or "the entry at position k".
- Example: Instead of "the (r+1)-th point", say "the next point" or "the additional point".
- Example: Instead of "the 5-th vertex", say "vertex 5" or "the fifth vertex" (spelled-out ordinals like "fifth" are fine).

### Names
- **Always verify author names.** For Helton's theorem, the first name is **John**, not William.
- When unsure about a name, look it up before writing voiceover text.

## Voiceover Writing Style

- Write in natural spoken English, not mathematical notation.
- Spell out math: "X 1 transpose X 2" not "$X_1^T X_2$".
- Use spaces between variable names: "X 1" not "X1".
- Spell out operations: "times", "plus", "minus", "transpose", "inverse".
- Read matrices by entries: "the matrix 2, 1, 1, 2" not "the matrix [[2,1],[1,2]]".
- Use "succeeds or equals zero" for $\succeq 0$ (positive semidefinite).
- Use "nonnegative" not "non-negative" (TTS handles single words better).

### Function/Notation Voicing

- Voice function notation naturally:
  - `r(3,3)` → "r of three and three"
  - `r(l, Cl)` → "r of l and C l"
  - `f(x)` → "f of x"
- Voice Ramsey notation:
  - `R(s,t)` → "R of s and t" or "the Ramsey number R s t"
  - `K_n` → "K n" or "the complete graph on n vertices"
- Voice exponents and subscripts:
  - `2^{n/2}` → "two to the n over two"
  - `κ_r` → "kappa sub r" or "kappa r"

## Voiceover + Animation Sync

### CRITICAL: `self.wait()` Inside vs. Outside Voiceover Blocks

**The most important rule in this entire skill file:**

`self.wait()` inside a `with self.voiceover()` block does NOT create a real pause if the voiceover audio is shorter than the total animation + wait time. The wait gets **clipped to the voiceover duration**. This means end-of-block waits inside voiceover blocks are often silently ignored.

**To create a real pause after a voiceover finishes, place `self.wait()` OUTSIDE the block:**

```python
# CORRECT — pause is real and audible
with self.voiceover(text="Here is the theorem."):
    self.play(Write(theorem))

self.wait(1.0)  # Real pause AFTER voiceover ends
```

```python
# WRONG — wait may be clipped to zero if TTS audio is short
with self.voiceover(text="Here is the theorem."):
    self.play(Write(theorem))
    self.wait(2.0)  # This wait may never happen!
```

**When to use `self.wait()` inside a block:** Only for pacing between multiple animations within the same voiceover, when the voiceover text is long enough to accommodate them. The wait acts as a fill during the TTS audio.

**When to use `self.wait()` outside a block:** For breathing pauses between voiceover blocks, scene-end pauses before `clear_screen()`, and any pause that must produce actual silence.

### Post-Voiceover Wait Durations

Since waits outside voiceover blocks are **real silence** (no TTS audio playing), keep them short:

| Context | Duration |
|---------|----------|
| Between consecutive voiceover blocks | `0.5` - `1.0` |
| After a voiceover block with only `pass` (no animations) | `0.5` |
| Scene-end pause before `clear_screen()` | `1.0` - `1.5` |
| After a key result or theorem voiceover | `1.0` - `1.5` |
| After the final voiceover of the entire video | `1.5` - `2.0` |

**Do NOT use long waits (2-8s) outside voiceover blocks.** These create awkward dead silence.

### Basic Pattern

```python
with self.voiceover(
    text="Step one is the Gram representation..."
):
    self.play(Write(title))
    self.play(FadeIn(content))
    self.wait(0.5)           # Fill time during TTS audio
    self.play(Write(equation))

self.wait(1.0)               # Real breathing pause after TTS ends
```

- Place animations inside the `with self.voiceover():` block.
- The voiceover auto-waits until speech finishes.
- Add `self.wait()` calls **inside** the block only between animation groups for pacing during speech.
- Add a scene-end pause **outside** the voiceover block before `clear_screen()`.

## Voiceover Text Formatting

- Use plain strings, not raw strings (no LaTeX in voiceover text).
- Use Python string concatenation for long voiceovers:
  ```python
  text="First sentence. "
       "Second sentence. "
       "Third sentence."
  ```
- Keep individual voiceover blocks to 3-5 sentences max.
